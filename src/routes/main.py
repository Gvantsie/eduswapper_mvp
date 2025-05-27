from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/conference')
@login_required
def conference():
    return render_template('conference.html')

@main_bp.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')
