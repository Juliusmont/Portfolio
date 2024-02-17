from flask import Flask, render_template
from controllers import *

app = Flask(__name__)

# http://127.0.0.1:5000/matrice_priorite/auth/ - the following will be our login page, which will use both GET and POST requests
@app.route('/matrice_priorite/auth/', methods=['GET', 'POST']) 
def login() : return app_login()
    

# http://127.0.0.1:5000/matrice_priorite/auth/logout - this will be the logout page
@app.route('/matrice_priorite/auth/logout')
def logout() : return app_logout()

# http://127.0.0.1:5000/matrice_priorite/auth/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/matrice_priorite/auth/register', methods=['GET', 'POST'])
def register() : return app_register()

# http://127.0.0.1:5000/matrice_priorite/auth/home - this will be the home page, only accessible for loggedin users
@app.route('/matrice_priorite/home')
def home() : return app_home()

# http://127.0.0.1:5000/matrice_priorite/auth/profile - this will be the profile page, only accessible for loggedin users
@app.route('/matrice_priorite/auth/profile')
def profile() : return app_profile()

# http://127.0.0.1:5000/matrice_priorite/users
@app.route('/matrice_priorite/users')
def list_users():
    users = get_users()
    return render_template('users.html', users=users)

# http://127.0.0.1:5000/matrice_priorite/tasks
@app.route('/matrice_priorite/tasks')
def tasks():
    tasks = get_tasks()
    return render_template('tasks.html', tasks=tasks)

# http://127.0.0.1:5000/matrice_priorite/auth/create_task - this will be the page to create a new task
@app.route('/matrice_priorite/auth/create_task', methods=['GET', 'POST'])
def create_task():
    return app_create_task()

# http://127.0.0.1:5000/matrice_priorite/auth/read_tasks - this will be the page to display the list of tasks
@app.route('/matrice_priorite/auth/read_tasks')
def read_tasks():
    tasks = get_tasks()
    return render_template('read_tasks.html', tasks=tasks)

# http://127.0.0.1:5000/matrice_priorite/auth/update_task - this will be the page to update a task
@app.route('/matrice_priorite/auth/update_task', methods=['GET', 'POST'])
def update_task():
    return app_update_task()

# http://127.0.0.1:5000/matrice_priorite/auth/delete_task - this will be the page to delete a task
@app.route('/matrice_priorite/auth/delete_task', methods=['GET', 'POST'])
def delete_task():
    return app_delete_task()