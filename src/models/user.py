from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from src.main import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    bio = db.Column(db.Text)
    location = db.Column(db.String(100))
    token_balance = db.Column(db.Integer, default=10)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    education = db.relationship('Education', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    experience = db.relationship('Experience', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    skills_to_share = db.relationship('SkillToShare', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    skills_to_acquire = db.relationship('SkillToAcquire', backref='user', lazy='dynamic', cascade='all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Education(db.Model):
    __tablename__ = 'education'

    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(100), nullable=False)
    degree = db.Column(db.String(100), nullable=False)
    year_range = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Education {self.degree} at {self.institution}>'


class Experience(db.Model):
    __tablename__ = 'experience'

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    period = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Experience {self.position} at {self.company}>'


class SkillToShare(db.Model):
    __tablename__ = 'skills_to_share'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<SkillToShare {self.name} ({self.level})>'


class SkillToAcquire(db.Model):
    __tablename__ = 'skills_to_acquire'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<SkillToAcquire {self.name} ({self.level})>'
