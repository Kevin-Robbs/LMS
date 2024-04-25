from flaskApp import app
from flaskApp.models.user import User
from bson import ObjectId
from flask import render_template, redirect, url_for, flash, session, request
from flaskApp import bcrypt

@app.route('/')
def main():
    return render_template('login.html')

@app.post('/login')
def login_user():
    data = request.form.to_dict()
    user = User.findUserByEmail(data['email'])
    pwdHash = bcrypt.check_password_hash(password=data['password'], pw_hash=user.password)
    return redirect('/')