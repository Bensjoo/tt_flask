from flask import render_template, request, Blueprint
from flaskapp.models import Post

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('home.html', posts=posts, title='Home')


@main.route("/about")
def about():
    return render_template('about.html')




@main.route("/employees")
def employees():
    return "<h1>Employees Page</h1>"


@main.route("/customers")
def customers():
    return "<h1>Customers Page </h1>"
