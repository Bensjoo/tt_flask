from tt_app import db
from tt_app import User, Post

user_1 = User(username='Bengt', email='b@mail.com',password='password')
db.session.add(user_1)

user_2 = User(username='Bengt2', email='b2@mail.com',password='password')

User.query.all()
