"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash, session 
from models import db, connect_db,User,Post
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


app.app_context().push()
connect_db(app)


@app.route('/')
def main():
    return redirect('/users')

@app.route('/users')
def list_users():
    '''show list of users'''
    users = User.query.all()
    return render_template('list.html', users=users)

@app.route('/users/new', methods=['GET'])
def create_new_user_form():
    return render_template('new.html')

@app.route('/users/new', methods=['POST'])
def create_new_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url or None)


    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('details.html', user=user)



@app.route('/users/<int:user_id>/edit')
def show_update_form(user_id):
    user = User.query.get_or_404(user_id)

    return render_template('update.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=['POST'])
def submit_update_form(user_id):
    user = User.query.get_or_404(user_id)

    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>/posts/new')
def add_post_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('forms-post.html', user=user)

@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def add_post(user_id):
    user = User.query.get_or_404(user_id)
    new_post = Post(title=request.form['title'], content=request.form['content'],user=user)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/users/{user_id}")

    


@app.route('/posts/<int:post_id>')
def show_posts(post_id):
    post = Post.query.get_or_404(post_id)

    return render_template('post.html', post=post)

@app.route('/posts/<int:post_id>/edit')
def show_edit_form(post_id):
    post = Post.query.get_or_404(post_id)

    return render_template('edit.html', post=post)

