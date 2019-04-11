from flask import render_template, url_for, flash, redirect
from flaskblog import app, db #bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
    {
        'author':'Eyamin Khan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 18 , 2017'
    },
    {
        'author':'neshat Mahee',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 20 , 2017'
    }
]


@app.route("/")
def start():
    return render_template('start.html')

@app.route("/Home")
def home():
    return render_template('home.html', posts = posts, title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in','success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html', title='Login', form=form)