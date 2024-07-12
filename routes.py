# import tensorflow as tf
# print("TensorFlow version:", tf.__version__)

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", requests=["POST", "GET"])
def index():
    if request.method == "POST":
        preferred_genre = request.form.get("genre")
        preferred_episodes = request.form.get("episode")
        return render_template("index.html", message="Data Submitted!", genre=preferred_genre,
                               episodes=preferred_episodes)
    return render_template("index.html")


@app.route("/templates/recommendation.html", requests=["POST", "GET"])
def recommendation():
    #  query = flask.request.args
    return render_template("recommendation.html")


@app.route("/index.html")
def genre():
    return render_template("index.html")


@app.route("/submission.html", request=["POST", "GET"])
def submission():
    return render_template("submission.html")


if __name__ == '__main__':
    app.run(debug=True)
