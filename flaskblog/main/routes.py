from flask import    Blueprint,request,render_template, url_for,flash,redirect,abort
from flaskblog.models import User,Post

main=Blueprint('main',__name__)


@main.route('/')
@main.route('/home')
def home():
    page=request.args.get('page',1,type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)
    name = request.args.get("name", "World")
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    name = request.args.get("name", "World")
    return render_template('about.html', title='About')



