# import tensorflow as tf
# print("TensorFlow version:", tf.__version__)

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", requests=["POST", "GET"])
def index():
    if request.method == "POST":
        return render_template("index.html", message="Hello World!")


@app.route("/templates/recommendation.html", requests=["POST", "GET"])
def recommendation():
    #  query = flask.request.args
    return render_template("recommendation.html")


@app.route("/index.html")
def genre():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
