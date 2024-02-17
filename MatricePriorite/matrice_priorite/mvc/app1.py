from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import User, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/PriorityDB'
#app.config.from_object('config')
db = SQLAlchemy(app)

# Routes and views go here...

if __name__ == '__main__':
    #db.init_app(app)
    db.create_all()
    app.run(debug=True)
