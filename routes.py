from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager, login_user, logout_user
from sqlalchemy.sql import func
from sqlalchemy.testing.pickleable import User

#create extension
db = SQLAlchemy()

#create the app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

#initialize app with extension
db.init_app(app)


class Users(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.string(25), unique=True, nullable=False)
    email = db.column(db.string(250), nullable=False)
    password = db.column(db.string(250), nullable=False)


with app.app_context():
    db.create_all()


# Creates a user loader callback that returns the user object give an id.
@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        preferred_genre = request.form.get("genre")
        preferred_episodes = request.form.get("episode")
        return render_template("index.html", message="Data Submitted!", genre=preferred_genre,
                               episodes=preferred_episodes)
    return render_template("index.html")


@app.route("/templates/recommendation.html", methods=["POST", "GET"])
def recommendation():
    #  query = flask.request.args
    return render_template("recommendation.html")


@app.route("/submission.html", methods=["POST", "GET"])
def submission():
    if request.method == "POST":
        genre_recommendation = request.form.get("genre")
        episode_length = request.form.get("episode")
        recommendations = []
        return render_template("submission.html")


@app.route("/templates/register.html", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        user = Users(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("register.html")


@app.route("/templates/login.html", methods=["GET", "POST"])
def login():
    #post request was made, find user by
    # filtering for the username
    if request.method == "POST":
        user = Users.query.filter_by(email=request.form.get("email")).first()

        if user.password == request.form.get("password"):
            login_user(user)
            return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login.html"))


@app.route("/templates/delete.html", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        email = request.form.get("email")
        # query by email
        user = Users.query.filter_by(email=email).first()

        if user:
            db.session.delete(user)
            db.session.commit()
            message = "User is Deleted"
        else:
            message = "User not Found"

    return render_template("delete.html", message=message)


@app.route("/templates/result.html", methods=["GET", "POST"])
def result():
    return render_template("result.html")


if __name__ == '__main__':
    app.run(debug=True)
