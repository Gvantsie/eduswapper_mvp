from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from src.forms import RegistrationForm, LoginForm, ProfileForm, EducationForm, ExperienceForm, SkillForm
from src.models.user import User, Education, Experience, SkillToShare, SkillToAcquire
from src.main import db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.index'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm(original_username=current_user.username, original_email=current_user.email)

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        current_user.location = form.location.data
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('auth.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.bio.data = current_user.bio
        form.location.data = current_user.location

    education = current_user.education.all()
    experience = current_user.experience.all()
    skills_to_share = current_user.skills_to_share.all()
    skills_to_acquire = current_user.skills_to_acquire.all()

    return render_template('auth/profile.html', form=form,
                           education=education,
                           experience=experience,
                           skills_to_share=skills_to_share,
                           skills_to_acquire=skills_to_acquire)


@auth_bp.route('/add_education', methods=['GET', 'POST'])
@login_required
def add_education():
    form = EducationForm()
    if form.validate_on_submit():
        education = Education(
            institution=form.institution.data,
            degree=form.degree.data,
            year_range=form.year_range.data,
            user_id=current_user.id
        )
        db.session.add(education)
        db.session.commit()
        flash('Education added successfully!', 'success')
        return redirect(url_for('auth.profile'))

    return render_template('auth/add_education.html', form=form)


@auth_bp.route('/delete_education/<int:id>', methods=['POST'])
@login_required
def delete_education(id):
    education = Education.query.get_or_404(id)
    if education.user_id != current_user.id:
        flash('You do not have permission to delete this item.', 'danger')
        return redirect(url_for('auth.profile'))

    db.session.delete(education)
    db.session.commit()
    flash('Education deleted successfully!', 'success')
    return redirect(url_for('auth.profile'))


@auth_bp.route('/add_experience', methods=['GET', 'POST'])
@login_required
def add_experience():
    form = ExperienceForm()
    if form.validate_on_submit():
        experience = Experience(
            company=form.company.data,
            position=form.position.data,
            period=form.period.data,
            user_id=current_user.id
        )
        db.session.add(experience)
        db.session.commit()
        flash('Experience added successfully!', 'success')
        return redirect(url_for('auth.profile'))

    return render_template('auth/add_experience.html', form=form)


@auth_bp.route('/delete_experience/<int:id>', methods=['POST'])
@login_required
def delete_experience(id):
    experience = Experience.query.get_or_404(id)
    if experience.user_id != current_user.id:
        flash('You do not have permission to delete this item.', 'danger')
        return redirect(url_for('auth.profile'))

    db.session.delete(experience)
    db.session.commit()
    flash('Experience deleted successfully!', 'success')
    return redirect(url_for('auth.profile'))


@auth_bp.route('/add_skill_to_share', methods=['GET', 'POST'])
@login_required
def add_skill_to_share():
    form = SkillForm()
    if form.validate_on_submit():
        skill = SkillToShare(
            name=form.name.data,
            level=form.level.data,
            user_id=current_user.id
        )
        db.session.add(skill)
        db.session.commit()
        flash('Skill to share added successfully!', 'success')
        return redirect(url_for('auth.profile'))

    return render_template('auth/add_skill.html', form=form, skill_type='share')


@auth_bp.route('/delete_skill_to_share/<int:id>', methods=['POST'])
@login_required
def delete_skill_to_share(id):
    skill = SkillToShare.query.get_or_404(id)
    if skill.user_id != current_user.id:
        flash('You do not have permission to delete this item.', 'danger')
        return redirect(url_for('auth.profile'))

    db.session.delete(skill)
    db.session.commit()
    flash('Skill to share deleted successfully!', 'success')
    return redirect(url_for('auth.profile'))


@auth_bp.route('/add_skill_to_acquire', methods=['GET', 'POST'])
@login_required
def add_skill_to_acquire():
    form = SkillForm()
    if form.validate_on_submit():
        skill = SkillToAcquire(
            name=form.name.data,
            level=form.level.data,
            user_id=current_user.id
        )
        db.session.add(skill)
        db.session.commit()
        flash('Skill to acquire added successfully!', 'success')
        return redirect(url_for('auth.profile'))

    return render_template('auth/add_skill.html', form=form, skill_type='acquire')


@auth_bp.route('/delete_skill_to_acquire/<int:id>', methods=['POST'])
@login_required
def delete_skill_to_acquire(id):
    skill = SkillToAcquire.query.get_or_404(id)
    if skill.user_id != current_user.id:
        flash('You do not have permission to delete this item.', 'danger')
        return redirect(url_for('auth.profile'))

    db.session.delete(skill)
    db.session.commit()
    flash('Skill to acquire deleted successfully!', 'success')
    return redirect(url_for('auth.profile'))

@auth_bp.route("/matching", methods=["GET"])
@login_required
def matching():
    # This is a placeholder for the matching logic.
    # In a real application, you would implement the logic to find matches based on shared skills.
    matches = []
    user_skills = current_user.skills_to_share.all()
    user_acquire_skills = current_user.skills_to_acquire.all()
    if user_skills or user_acquire_skills:
        # Example logic: find users with at least one matching skill to share or acquire
        for user in User.query.all():
            if user.id != current_user.id:
                shared_skills = set(user.skills_to_share.all()) & set(user_skills)
                acquire_skills = set(user.skills_to_acquire.all()) & set(user_acquire_skills)
                if shared_skills or acquire_skills:
                    matches.append({
                        'user': user,
                        'shared_skills': shared_skills,
                        'acquire_skills': acquire_skills
                    })
    else:
        flash('You have no skills to share or acquire. Please add some skills to find matches.', 'info')
    if not matches:
        flash('No matches found based on your skills.', 'info')
    # Render the matching page with the found matches
    return render_template('matching.html', matches=matches)

