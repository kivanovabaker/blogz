from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:foxes@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

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

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    post_id = request.args.get('id')
    if post_id:
        ind_post = Blog.query.filter_by(id=post_id).first()
        return render_template('ind_post.html', post=ind_post)
    posts = Blog.query.all()
    return render_template('blog.html', title = 'Thoughts and Musings', posts=posts)

@app.route('/newpost', methods=['GET', 'POST'])
def newpost():
    if request.method == 'POST':
        user = User.query.filter_by(username=session['username']).first()
        title = request.form['title']
        body = request.form['body']
        existing_title = Blog.query.filter_by(title=title).first()
        title_error = ""
        body_error = ""
        
        if not title:
            title_error = "Please enter a title."
        if existing_title:
            title_error = "Please enter a previously unused title."
            title = ""
        if not body:
            body_error = "Please enter content into your blog post."

        if not title_error and not body_error:
            new_post = Blog(title, body, user)
            db.session.add(new_post)
            db.session.commit()
            new_post = Blog.query.filter_by(title=title).first()
            post_id = new_post.id
            return redirect('/blog?id={0}'.format(post_id))
        else:
            return render_template('newpost.html', title="What's on Your Mind?", post_title=title, body=body, 
            title_error=title_error, body_error=body_error)

    return render_template('newpost.html', title="What's on Your Mind?")

@app.route('/signup', methods['POST'])
#@app.route('/login')
#@app.route('/index')
if __name__ == '__main__':
    app.run()