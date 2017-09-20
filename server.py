from flask import Flask, render_template, request, flash, redirect, session, jsonify

app = Flask(__name__)
app.secret_key = "secret"

USERS = {"jhacker": "superseekritpw", "utester": "testing123"}


@app.route("/")
def show_index():
    print session
    return render_template("index.html")


@app.route("/verify", methods=["POST"])
def verify_credentials():
    username = request.form.get("username")
    password = request.form.get("password")

    print username, password

    if username in USERS and USERS[username] == password:
        return jsonify("success")

    return jsonify("failure")


@app.route("/login", methods=["POST"])
def login():
    flash("You're logged in!")
    username = request.form.get("username")
    session["username"] = username
    print session

    return redirect("/")


@app.route("/logout")
def process_logout():
    session.pop("username")
    flash("Goodbye!")
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
