from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from app import db, bcrypt
from app.models import User, Task, TaskPriority
from sqlalchemy import func

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.application'))
    return redirect(url_for('main.login'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.application'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.application'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@bp.route('/application')
@login_required
def application():
    return render_template('application.html')


@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/api/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    if request.method == 'POST':
        data = request.json
        new_task = Task(
            title=data['title'],
            description=data['description'],
            category=data['category'],
            priority_id=data['priority_id'],
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task created successfully'}), 201
    else:
        tasks = Task.query.filter_by(user_id=current_user.id).all()
        return jsonify([{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'category': task.category,
            'priority': task.priority.priority_name,
            'is_completed': task.is_completed,
            'created_at': task.created_at.isoformat()
        } for task in tasks])


@bp.route('/api/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
@login_required
def update_delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    if request.method == 'PUT':
        data = request.json
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.category = data.get('category', task.category)
        task.priority_id = data.get('priority_id', task.priority_id)
        task.is_completed = data.get('is_completed', task.is_completed)
        db.session.commit()
        return jsonify({'message': 'Task updated successfully'})

    elif request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'})


@bp.route('/api/task_stats')
@login_required
def task_stats():
    completed_vs_pending = db.session.query(
        Task.is_completed,
        func.count(Task.id)
    ).filter_by(user_id=current_user.id).group_by(Task.is_completed).all()

    priority_distribution = db.session.query(
        TaskPriority.priority_name,
        func.count(Task.id)
    ).join(Task).filter(Task.user_id == current_user.id).group_by(TaskPriority.priority_name).all()

    category_distribution = db.session.query(
        Task.category,
        func.count(Task.id)
    ).filter_by(user_id=current_user.id).group_by(Task.category).all()

    return jsonify({
        'completed_vs_pending': dict(completed_vs_pending),
        'priority_distribution': dict(priority_distribution),
        'category_distribution': dict(category_distribution)
    })