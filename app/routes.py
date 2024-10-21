from flask import Blueprint, render_template, url_for, redirect,\
    flash, request, jsonify, send_file
from flask_login import login_user, current_user, logout_user,\
    login_required


from app import db, bcrypt
from app.models import User, Mentors, Students
from app.forms import RegistrationForm, LoginForm

from bot import ProgressReportGenerator

main_routes = Blueprint('main_routes', __name__)

generator = ProgressReportGenerator()

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

            return redirect(next_page) if next_page else redirect(url_for('main_routes.dashboard'))

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
    students = [i.students for i in Students.query.all()]
    mentors = [i.mentors for i in Mentors.query.all()]

    return render_template('index.html', members=students+mentors, mentors=mentors)

# API endpoints

## Process form
@main_routes.route('/api/v1/processData', methods=['POST'])
@login_required
def process_data():
    if request.method == 'POST':
        json_data = request.json
        json_data['team_member_contributions'] = tuple([f"{k}\n\n{v}" for k, v in json_data['team_member_contributions'].items()])
        report = generator.generate_and_save_report(json_data)

    return jsonify({"success": True})

## Download PDF
@main_routes.route('/api/v1/downloadPDF', methods=['POST'])
@login_required
def download_pdf():
    file_path = 'progress_report.docx'
    return send_file(file_path, as_attachment=True)