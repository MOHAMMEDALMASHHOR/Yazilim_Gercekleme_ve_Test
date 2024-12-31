from app import create_app, db
from app.models import User, TaskPriority, Task
from app import bcrypt

app = create_app()

with app.app_context():
    # Create tables
    db.create_all()

    # Add task priorities
    priorities = ['High', 'Medium', 'Low']
    for priority in priorities:
        if not TaskPriority.query.filter_by(priority_name=priority).first():
            db.session.add(TaskPriority(priority_name=priority))

    # Add a test user
    if not User.query.filter_by(email='test@example.com').first():
        hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
        test_user = User(name='Test User', email='test@example.com', password=hashed_password)
        db.session.add(test_user)

    db.session.commit()

print("Database setup complete.")