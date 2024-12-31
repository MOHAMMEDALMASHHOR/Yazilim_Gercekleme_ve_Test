document.addEventListener('DOMContentLoaded', function() {
    const taskForm = document.getElementById('add-task-form');
    const taskList = document.getElementById('tasks');
    const filterCategory = document.getElementById('filter-category');
    const filterPriority = document.getElementById('filter-priority');
    const filterStatus = document.getElementById('filter-status');

    // Load tasks
    function loadTasks() {
        fetch('/api/tasks')
            .then(response => response.json())
            .then(tasks => {
                taskList.innerHTML = '';
                tasks.forEach(task => {
                    const li = document.createElement('li');
                    li.innerHTML = `
                        <h3>${task.title}</h3>
                        <p>${task.description}</p>
                        <p>Category: ${task.category}</p>
                        <p>Priority: ${task.priority}</p>
                        <p>Status: ${task.is_completed ? 'Completed' : 'Pending'}</p>
                        <button class="edit-task" data-id="${task.id}">Edit</button>
                        <button class="delete-task" data-id="${task.id}">Delete</button>
                        <button class="toggle-status" data-id="${task.id}">${task.is_completed ? 'Mark as Pending' : 'Mark as Completed'}</button>
                    `;
                    taskList.appendChild(li);
                });
                updateFilters(tasks);
                updateCharts();
            });
    }

    // Add new task
    taskForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const title = document.getElementById('task-title').value;
        const description = document.getElementById('task-description').value;
        const category = document.getElementById('task-category').value;
        const priorityId = document.getElementById('task-priority').value;

        fetch('/api/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, description, category, priority_id: priorityId }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            taskForm.reset();
            loadTasks();
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });

    // Edit task
    taskList.addEventListener('click', function(e) {
        if (e.target.classList.contains('edit-task')) {
            const taskId = e.target.getAttribute('data-id');
            const taskElement = e.target.closest('li');
            const title = taskElement.querySelector('h3').textContent;
            const description = taskElement.querySelectorAll('p')[0].textContent;
            const category = taskElement.querySelectorAll('p')[1].textContent.replace('Category: ', '');
            const priority = taskElement.querySelectorAll('p')[2].textContent.replace('Priority: ', '');

            // Replace task display with edit form
            taskElement.innerHTML = `
                <input type="text" class="edit-title" value="${title}">
                <textarea class="edit-description">${description}</textarea>
                <input type="text" class="edit-category" value="${category}">
                <select class="edit-priority">
                    <option value="1" ${priority === 'High' ? 'selected' : ''}>High</option>
                    <option value="2" ${priority === 'Medium' ? 'selected' : ''}>Medium</option>
                    <option value="3" ${priority === 'Low' ? 'selected' : ''}>Low</option>
                </select>
                <button class="save-edit" data-id="${taskId}">Save</button>
                <button class="cancel-edit">Cancel</button>
            `;
        }
    });

    // Save edited task
    taskList.addEventListener('click', function(e) {
        if (e.target.classList.contains('save-edit')) {
            const taskId = e.target.getAttribute('data-id');
            const taskElement = e.target.closest('li');
            const title = taskElement.querySelector('.edit-title').value;
            const description = taskElement.querySelector('.edit-description').value;
            const category = taskElement.querySelector('.edit-category').value;
            const priorityId = taskElement.querySelector('.edit-priority').value;

            fetch(`/api/tasks/${taskId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ title, description, category, priority_id: priorityId }),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                loadTasks();
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }
    });

    // Delete task
    taskList.addEventListener('click', function(e) {
        if (e.target.classList.contains('delete-task')) {
            const taskId = e.target.getAttribute('data-id');
            fetch(`/api/tasks/${taskId}`, {
                method: 'DELETE',
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                loadTasks();
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }
    });

    // Toggle task status
    taskList.addEventListener('click', function(e) {
        if (e.target.classList.contains('toggle-status')) {
            const taskId = e.target.getAttribute('data-id');
            const isCompleted = e.target.textContent === 'Mark as Pending';
            fetch(`/api/tasks/${taskId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ is_completed: !isCompleted }),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                loadTasks();
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }
    });

    // Update filters
    function updateFilters(tasks) {
        const categories = [...new Set(tasks.map(task => task.category))];
        filterCategory.innerHTML = '<option value="">All Categories</option>';
        categories.forEach(category => {
            filterCategory.innerHTML += `<option value="${category}">${category}</option>`;
        });
    }

    // Apply filters
    function applyFilters() {
        const category = filterCategory.value;
        const priority = filterPriority.value;
        const status = filterStatus.value;

        Array.from(taskList.children).forEach(li => {
            const taskCategory = li.querySelector('p:nth-child(3)').textContent.replace('Category: ', '');
            const taskPriority = li.querySelector('p:nth-child(4)').textContent.replace('Priority: ', '');
            const taskStatus = li.querySelector('p:nth-child(5)').textContent.replace('Status: ', '');

            const categoryMatch = !category || taskCategory === category;
            const priorityMatch = !priority || taskPriority === priority;
            const statusMatch = !status ||
                (status === 'completed' && taskStatus === 'Completed') ||
                (status === 'pending' && taskStatus === 'Pending');

            li.style.display = categoryMatch && priorityMatch && statusMatch ? '' : 'none';
        });
    }

    filterCategory.addEventListener('change', applyFilters);
    filterPriority.addEventListener('change', applyFilters);
    filterStatus.addEventListener('change', applyFilters);

    // Update charts
    function updateCharts() {
        fetch('/api/task_stats')
            .then(response => response.json())
            .then(data => {
                createCompletedVsPendingChart(data.completed_vs_pending);
                createPriorityDistributionChart(data.priority_distribution);
                createCategoryDistributionChart(data.category_distribution);
            });
    }

    function createCompletedVsPendingChart(data) {
        const ctx = document.getElementById('completed-vs-pending-chart').getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Completed', 'Pending'],
                datasets: [{
                    data: [data['true'] || 0, data['false'] || 0],
                    backgroundColor: ['#4CAF50', '#FFC107']
                }]
            },
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: 'Completed vs Pending Tasks'
                }
            }
        });
    }

    function createPriorityDistributionChart(data) {
        const ctx = document.getElementById('priority-distribution-chart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: Object.keys(data),
                datasets: [{
                    label: 'Tasks',
                    data: Object.values(data),
                    backgroundColor: ['#F44336', '#FFC107', '#4CAF50']
                }]
            },
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: 'Task Priority Distribution'
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    }

    function createCategoryDistributionChart(data) {
        const ctx = document.getElementById('category-distribution-chart').getContext('2d');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: Object.keys(data),
                datasets: [{
                    data: Object.values(data),
                    backgroundColor: [
                        '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'
                    ]
                }]
            },
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: 'Task Category Distribution'
                }
            }
        });
    }

    // Initial load
    loadTasks();
});