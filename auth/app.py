from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User,Feedback
from forms import RegisterForm, LoginForm, FeedbackForm
from werkzeug.exceptions import Unauthorized


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///auth_exer"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.app_context().push()
connect_db(app)

toolbar = DebugToolbarExtension(app)

@app.route('/')
def redirect_register():
    return redirect('/register')

@app.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        new_user =  User.register(username,password,email,first_name,last_name)
        db.session.commit()
        session['username'] = new_user.username
        flash('You created an account')
        return redirect(f'/users/{new_user.username}')

    
    return render_template('register.html', form=form)


@app.route('/login', methods=["GET","POST"])
def login_form():
    # if "username" in session:
    #     return redirect(f'/users/{session['username']}')
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.authenticate(username,password)
        if user:
            flash("welcome back")
            session['username'] = user.username
            return redirect(f'/users/{user.username}')
        else:
            form.username.errors = ['Invalid username/password']
    return render_template('login.html', form=form)


@app.route('/users/<username>')
def show_user(username):
    if "username" in session:
        user = User.query.get_or_404(username)
        feedback = Feedback.query.filter_by(username=username)
        return render_template('user.html', user=user, feedback=feedback)
    else:
        flash('You need to log in first', 'danger')
        return redirect('/')
    

@app.route('/users/<username>/feedback/add', methods=["GET", "POST"])
def add_feedback(username):
    if "username" in session:
        form = FeedbackForm()
        return render_template('feedback.html', form=form)
    else:
        flash('you need to login first', 'danger')
        return redirect('/login')


@app.route('/users/<username>/delete', methods=["POST"])
def delete_user(username):
    if "username" in session:
        user = User.query.get(username)
        db.session.delete(user)
        db.session.commit()
        return redirect('/')
    else:
        flash('you need to login first', 'danger')
        return redirect('/login')


@app.route('/logout')
def logout_user():
    session.pop('username')
    flash('Goodbye', 'info')
    return redirect('/')