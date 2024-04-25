from flaskApp import app
from flaskApp.models.user import User
from bson import ObjectId
from flask import render_template, redirect, url_for, flash, session, request

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    user_info = User.findUserByID({'_id': ObjectId('66253ecada2ee74c6b6d0b4d')})
    return render_template('dashboard.html', user=user_info)

@app.post('/login_user')
def login_user():
    data = request.form.to_dict()
    return redirect(url_for('dashboard'))
