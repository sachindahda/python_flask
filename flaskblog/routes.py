from flask import    request,render_template, url_for,flash,redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User,Post
from flaskblog import app

posts = [
    {
        'author': 'test',
        'title': 'blog post1',
        'content': 'fdlsajkfdsa',
        'date_posted': '20-9-2019'

    },
    {
        'author': 'test 2',
        'title': 'blog post 2',
        'content': 'fdlsajkfdsfgsfdsa',
        'date_posted': '24-9-2019'

    }
] 


@app.route('/')
@app.route('/home')
def home():
    name = request.args.get("name", "World")
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    name = request.args.get("name", "World")
    return render_template('about.html', title='About')


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account Created for {}!'.format(form.username.data),'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@admin.com' and form.password.data=='password':
            flash('You have been logged in','success')
            return redirect(url_for('home'))
        else:
            flash('An error occured','danger')

    return render_template('login.html', title='Register', form=form)
