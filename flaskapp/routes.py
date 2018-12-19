from flask import render_template, url_for, flash, redirect
from flaskapp import app
from flaskapp.models import User, Post
from flaskapp.forms import RegistrationForm, LoginForm

posts = [
    {
        'author' : 'Bengt Sjögren',
        'title' : 'Blog Post 1',
        'content' : 'First post!',
        'date_posted' : '20 december, 2018'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post! Nice!',
        'date_posted' : '21 december, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='Home')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == "pass":
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful.', 'danger')

    return render_template('login.html', title='Log in', form=form)

@app.route("/employees")
def employees():
    return "<h1>Employees Page</h1>"

@app.route("/customers")
def customers():
    return "<h1>Customers Page </h1>"