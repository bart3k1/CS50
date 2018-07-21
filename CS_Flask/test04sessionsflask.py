from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# notki = [] /- bez session["notki"]


@app.route("/notes", methods=["GET", "POST"])
def notes():
    if session.get("notki") is None:
        session["notki"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notki"].append(note)
    return render_template("notes.html", notki=session["notki"])