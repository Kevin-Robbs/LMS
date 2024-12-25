from flaskApp import app
from flaskApp.models.user import User
from flask import render_template, redirect, url_for, flash, session, request

@app.route('/')
def main():
    return render_template('login.html')

@app.post('/login')
def login_user():
    data = request.form.to_dict()
    
    try:
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            flash('Invalid email', 'email')
            return redirect('/')
        pwdHash = User.validatePassword(user.password, data['password'])
        if not pwdHash:
            flash('Invalid password', 'password')
            return redirect('/')
        session['user'] = user.id
        return redirect('/dashboard')
    except Exception as e:
        print(e)
        flash('An error occurred', 'error')
        return redirect('/')