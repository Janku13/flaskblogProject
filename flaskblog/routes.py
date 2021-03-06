from flask import render_template, url_for, flash, redirect
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app


posts = [
    {
        "author": "Mohammed",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20,2022",
    },
    {
        "author": "Jone",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "mai 20,2022",
    },
]

# roter Decoratores
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


# register and login routes
# validate if form was submeted and send a flash and redirect if it did
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f"Welcom !", "success")
            return redirect(url_for("home"))
        else:
            flash("login Unsuccessful. Please check email and password!", "danger")
    return render_template("login.html", title="Login", form=form)
