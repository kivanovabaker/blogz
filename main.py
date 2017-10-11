from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:foxes@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), unique = True)
    body = db.Column(db.String(5000))

    def __init__(self,title,body):
        self.title = title
        self.body = body

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    posts = Blog.query.all()
    return render_template('blog.html', title = 'Thoughts and Musings', posts=posts)

@app.route('/newpost', methods=['GET', 'POST'])
def newpost():
    if request.method == 'POST':
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
            new_post = Blog(title,body)
            db.session.add(new_post)
            db.session.commit()
            return redirect('/blog')
        else:
            return render_template('newpost.html', title="What's on Your Mind?", post_title=title, body=body, 
            title_error=title_error, body_error=body_error)

    return render_template('newpost.html', title="What's on Your Mind?")

if __name__ == '__main__':
    app.run()