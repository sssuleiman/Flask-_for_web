from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    # return '<h1>Hello, World! </h1>'
    return render_template("home.html")

@app.route('/about')
def about():
    # return '<h1>Hello, World! </h1>'
    return render_template("about.html")
