from sqlite3 import connect
from flask import render_template, redirect, request
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User

@app.route('/')
def index():
    users = User.get_all()
    return render_template("index.html", all_users = users)

@app.route('/user/new')
def new():
    return render_template("create_user.html")

@app.route('/create/user', methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect('/')