from flask import Flask, render_template
import datetime


app = Flask(__name__)


@app.route("/")
def index():
    print("XXX")
    return "Hello flask"


@app.route("/xxx")
def xxx():
    return "xxxxxxxxxxxxxxx"


# @app.route("/<string:name>")
# def hello(name):
#     return f"<h1>Hello {name}</h1>"

#
@app.route("/index")
def start():
    return render_template("index.html")


@app.route("/index2")
def start2():
    headline = "traytatatta"
    return render_template("index2.html", headline=headline)

@app.route("/newyear")
def newyear_checker():
    now = datetime.datetime.now()
    newyear = now.month == 1 and now.day == 1
    if newyear is False:
        a = "Nie"
    else:
        a = "Tak!"
    headline = "Czy mamy Nowy Rok?"
    return render_template("index2.html", a=a, headline=headline)
    # return render_template("index3.html", newyear=newyear, headline=headline) //mozna ifem w templatce

@app.route("/xtend")
def xtend():
    headline = "traytatatta"
    return render_template("xtend.html", headline=headline)