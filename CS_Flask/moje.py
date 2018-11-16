from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def start():
    return render_template("start_m.html")


@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    #     if jeśli udostępnimy method GET albo nie wpiszemy nic w form
    if request.method == "GET":
        return "Please submit form"
    else:
        name = request.form.get("name")
        if not name:
            name = "Nieznajomy"
        return render_template("hello.html", name=name)