from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from models import Blog, User

@app.before_request
def require_login():
    allowed_routes = ['index', 'blog', 'login', 'signup']
    if request.endpoint not in allowed_routes and 'user' not in session:
        return redirect('/login')

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/blog', methods=['GET', 'POST'])
#TODO modify to accommodate all desired requests
def blog():
    post_id = request.args.get('id')
    user_id = request.args.get('user_id')

    #If the query parameter is an individual post
    if post_id:
        ind_post = Blog.query.filter_by(id=post_id).first()
        return render_template('ind_post.html', post=ind_post)

    #If the query parameter is a user
    if user_id:
        user_posts = Blog.query.filter_by(user_id=user_id).all()
        return render_template('blog.html', title="Thoughts and Musings", posts=user_posts)

    #If no parameters, display all
    posts = Blog.query.all()
    return render_template('blog.html', title = 'Thoughts and Musings', posts=posts)

@app.route('/newpost', methods=['GET', 'POST'])
def newpost():
    if request.method == 'POST':
        user = User.query.filter_by(username=session['user']).first()
        title = request.form['title']
        body = request.form['body']
        existing_title = Blog.query.filter_by(title=title).first()
        title_error = ""
        body_error = ""
        
        #Post Validation
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

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        existing_username = User.query.filter_by(username=username).first()

        user_error = ""
        password_error = ""
        match_error = ""

        #Registration Validation
        if existing_username:
            user_error = "Oops, that username is taken. Log in or choose a different pen name"
        if len(username)<3 or len(username)>40:
            user_error = "Please enter a valid username, 3 to 40 characters in length"
        if len(password)<3 or len(password)>40:
            password_error = "Please enter a valid password, 3 to 40 characters in length"
        if password != verify:
            match_error = "Please enter matching passwords"

        if user_error or password_error or match_error:
           return render_template('signup.html', title="Sign Up", user_error=user_error, 
            password_error=password_error, match_error=match_error)
        else:
            new_user = User(username,password)
            db.session.add(new_user)
            db.session.commit()
            session['user'] = username
            flash('Logged in')
            return redirect('/newpost')

    return render_template('signup.html', title="Sign Up!")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        #Login validation
        if not user:
            flash("Oops, this username doesn't exist")
            return redirect('/login')
        elif user.password != password:
            flash("Invalid password")
            return redirect('/login')
        else:
            session['user'] = username
            flash('Logged in')
            return redirect('/newpost')

    return render_template('login.html', title="Login")

@app.route('/logout')
def logout():
    del session['user']
    flash('Logged out')
    return redirect('/blog')

if __name__ == '__main__':
    app.run()