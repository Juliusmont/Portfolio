from flask import Flask, render_template, request, redirect, url_for, session
from models import User, Task
import mysql.connector
import re

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="PriorityDB"
)
cursor = conn.cursor()

# Définition de la fonction de connexion login()
def app_login():
    # Output message if something goes wrong...
    msg = ''
     # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
       # Check if account exists using MySQL
        cursor =  conn.cursor() #mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()    
         # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            # Redirect to home page
            return redirect(url_for('home')) #return 'Logged in successfully!'
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)

#
def app_logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

#
def app_register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
         # Check if account exists using MySQL
        cursor = conn.cursor() 
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s)', (username, password, email,))
            conn.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

#
def app_home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        tasks = get_tasks()
        return render_template('home.html', username=session['username'], tasks=tasks)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

#
def app_profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor =  conn.cursor() 
        cursor.execute('SELECT * FROM users WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

def get_users():
    cursor.execute("SELECT * FROM users")
    users = []
    for row in cursor.fetchall():
        users.append(User(*row))
    return users

def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = []
    for row in cursor.fetchall():
        tasks.append(Task(*row))
    return tasks

def app_create_task():
    msg = ''
    if request.method == 'POST':
        # Récupérer les données du formulaire
        description = request.form['description']
        duration = request.form['duration']
        importance = request.form['importance']
        urgency = request.form['urgency']
        deadline = request.form['deadline']
        monetary_cost = request.form['monetary_cost']
        completion_percentage = 0  # Initialisé à 0%
        status = False  # Initialisé à False
        user_id = session['id']  # Remplacez 1 par l'ID de l'utilisateur approprié

        # Insérer la tâche dans la base de données
        cursor.execute('INSERT INTO tasks VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (description, duration, importance, urgency, deadline, monetary_cost, completion_percentage, status, user_id, 'ponctuelle'))
        conn.commit()
        msg = 'La tâche a été créée avec succès!'

    return render_template('create_task.html', msg=msg)

def read_tasks():
    # Récupérer toutes les tâches de l'utilisateur
    user_id = session['id']  # Remplacez 1 par l'ID de l'utilisateur approprié
    cursor.execute('SELECT * FROM tasks WHERE user_id = %s', (user_id,))
    tasks = cursor.fetchall()
    return render_template('read_tasks.html', tasks=tasks)

def home_tasks():
    # Récupérer toutes les tâches de l'utilisateur
    user_id = session['id']  # Remplacez 1 par l'ID de l'utilisateur approprié
    cursor.execute('SELECT * FROM tasks WHERE user_id = %s', (user_id,))
    tasks = cursor.fetchall()
    return render_template('home.html', tasks=tasks)

def app_update_task(task_id):
    msg = ''
    if request.method == 'POST':
        # Récupérer les données du formulaire
        completion_percentage = request.form['completion_percentage']
        status = request.form['status']

        # Mettre à jour la tâche dans la base de données
        cursor.execute('UPDATE tasks SET completion_percentage = %s, status = %s WHERE id = %s',
                       (completion_percentage, status, task_id))
        conn.commit()
        msg = 'La tâche a été mise à jour avec succès!'

    # Récupérer les détails de la tâche pour l'affichage sur le formulaire de mise à jour
    cursor.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
    task = cursor.fetchone()
    return render_template('update_task.html', task=task, msg=msg)

def app_delete_task(task_id):
    # Supprimer la tâche de la base de données
    cursor.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    conn.commit()
    msg = 'La tâche a été supprimée avec succès!'
    return render_template('delete_task.html', msg=msg)
