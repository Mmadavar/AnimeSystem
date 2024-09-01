# import tensorflow as tf
# print("TensorFlow version:", tf.__version__)

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

#create extension
db = SQLAlchemy()

#create the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

#initialize app with extension
db.init_app(app)


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


if __name__ == '__main__':
    app.run(debug=True)
