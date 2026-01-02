from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/name", methods = ["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("get_details.html")
    elif request.method == "POST":
        showname = request.form["user_name"]
        return render_template("show_details.html", show_name = showname)
    else:
        print("error")

if __name__ == '__main__':
    app.debug = True
    app.run()