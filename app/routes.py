from flask import Blueprint, render_template, url_for, redirect, flash, request
from app import db, bcrypt
from app.models import User
from app.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

main_routes = Blueprint('main_routes', __name__)

# Home route
@main_routes.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)

# Registration route
@main_routes.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.create_user(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('main_routes.login'))
    return render_template('register.html', form=form)

# Login route
@main_routes.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_routes.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            flash('Login successful!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main_routes.home'))
        else:
            flash('Login failed. Check your email and password.', 'danger')
    return render_template('login.html', form=form)

# Logout route
@main_routes.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main_routes.login'))

# Protected route
@main_routes.route('/dashboard')
@login_required
def dashboard():
    return render_template('index.html')
