from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, UserMixin
from Recommendation_Algorithm import anime_recommendation
from werkzeug.security import generate_password_hash, check_password_hash
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
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


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
        total = 30
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
        user_check = Users.query.filter(Users.email == email, Users.name == name).first()
        if not user_check:
            user = Users(name=name, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("index"))
        else:
            flash("User already exists!", 'error')

    return render_template("register.html")




@app.route("/templates/login.html", methods=["GET", "POST"])
def login():
    #post request was made, find user by
    # filtering for the username
    if request.method == "POST":
        user = Users.query.filter_by(email=request.form.get("email")).first()
        password = request.form.get("password")
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash("Invalid email or password", 'error')

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
            flash("User is Deleted", 'success')
            return render_template("delete.html")
        else:
            flash("User not found", 'error')

    return render_template("delete.html")


if __name__ == '__main__':
    app.run(debug=True)



