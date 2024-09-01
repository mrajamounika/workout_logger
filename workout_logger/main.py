from flask import Blueprint, flash,render_template,url_for,redirect,request
from flask_login import login_required, current_user
from . import db
from . import models

main= Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
    
@main.route('/profile')
@login_required
def profile():
    return render_template('Profile.html', name=current_user.name)

@main.route('/new')
@login_required
def new_workout():
    return render_template('create_workout.html')

@main.route('/new', methods=['POST'])
@login_required
def new_workout_post():
    sets= request.form.get('sets')
    workout_name=request.form.get('workout_name')
    
    workout=models.Workout(sets=sets,workout_name=workout_name, author=current_user)
    db.session.add(workout)
    db.session.commit()
    
    flash('Your workout has been added!')
    return redirect(url_for('main.user_workouts'))

@main.route('/all')
@login_required
def user_workouts():
    user=models.User.query.filter_by(email=current_user.email).first_or_404()
    workouts =user.workouts
    return render_template('all_workouts.html', workouts=workouts, user=user)

@main.route("/workout/<int:workout_id>/update", methods=['GET','POST'])
@login_required
def update_workout(workout_id):
    workout=models.Workout.query.get_or_404(workout_id)
    if request.method=='POST':
        workout.sets = request.form['sets']
        workout.workout_name =request.form['workout_name']
        db.session.commit()
        flash('Your workout has been updated!')
        return redirect(url_for('main.user_workouts'))
    return render_template('update_workout.html', workout=workout)

@main.route("/workout/<int:workout_id>/delete", methods=['GET','POST'])
@login_required
def delete_workout(workout_id):
    workout=models.Workout.query.get_or_404(workout_id)
    db.session.delete(workout)
    db.session.commit()
    return redirect(url_for('main.user_workouts'))
    
    