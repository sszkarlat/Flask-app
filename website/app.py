from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        return render_template("login.html", name=name)
    return render_template("index.html")
