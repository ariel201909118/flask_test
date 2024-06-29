from flask import render_template, flash, redirect, url_for
from . import app, db 
from .models import User
from .forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

def create_admin_if_not_exists():
    admin = User.query.filter_by(username='Admin').first()
    if not admin:
        admin = User(username='Admin', password=generate_password_hash('admin123'))
        db.session.add(admin)
        db.session.commit()
        
        
@app.route('/admin')
def before_request():
    create_admin_if_not_exists()
    return 'Admin Created'
@app.route('/', methods=['POST', 'GET'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            flash('Login successfull', 'success')
            return redirect(url_for('index'))
    return render_template('index.html', form=form)