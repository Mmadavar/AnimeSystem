from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, UserMixin
from Recommendation_Algorithm import anime_recommendation
import os


#create extension
db = SQLAlchemy()

#create the app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = os.urandom(24)
#initialize app with extension
db.init_app(app)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


login_manager = LoginManager()
login_manager.init_app(app)
# Creates a user loader callback that returns the user object give an id.
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        preferred_genre = request.form.get("genre", "").lower()
        preferred_episodes = request.form.get("episode")
        total = 10
        recommendations = anime_recommendation(preferred_episodes, preferred_genre, total)
        return render_template("recommendation.html", message="Data Submitted!", recommendations=recommendations.to_dict(orient="records"))
    return render_template("form.html")


@app.route("/templates/recommendation.html", methods=["POST", "GET"])
def recommendation():
    return render_template("recommendation.html")


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

        if user and user.password == request.form.get("password"):
            login_user(user)
            return redirect(url_for("index"))
        else:
            print("Invalid email or password")

    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


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
            return redirect(url_for("index"))
        else:
            message = "User not Found"
            return render_template("delete.html", message=message)


if __name__ == '__main__':
    app.run(debug=True)



