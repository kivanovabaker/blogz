from app import db

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique = True)
    body = db.Column(db.String(5000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, body, user):
        self.title = title
        self.body = body
        self.user = user

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(40))
    blogs = db.relationship('Blog', backref='user')

    def __init__(self, username,password):
        self.username = username
        self.password = password

    def __repr__(self):
        return self.username