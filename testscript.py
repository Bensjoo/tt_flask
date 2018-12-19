from tt_app import db
from tt_app import User, Post

db.create_all()

user_1 = User(username='Bengt', email='b@mail.com',password='pass')
db.session.add(user_1)

user_2 = User(username='Bengt2', email='b2@mail.com',password='pass2')
db.session.add(user_2)

db.session.commit()
User.query.all()
