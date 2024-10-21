from app import db
from flask_login import UserMixin
from app import login_manager, bcrypt

# User loader callback function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=db.func.now())

    def __repr__(self):
        return f"<User {self.username}>"

    @classmethod
    def create_user(cls, username, email, password):
        """Hash the password and create a new user."""
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        return cls(username=username, email=email, password=hashed_password)

class Mentors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mentors = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Mentors {self.mentors}>"

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    students = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Students {self.students}>"