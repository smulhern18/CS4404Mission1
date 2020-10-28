from flask import Flask, render_template, request
import initializeDatabase
import database
import time

global app, dbConnector
app = Flask(__name__)
dbConnector = initializeDatabase.init()


def index():
    return render_template('index.html')


def submit():
    if request.method == "GET":
        return render_template('submitted.html')
    else:
        ipAddress = request.remote_addr
        todayDate = time.strftime('%Y-%m-%d %H-%M-%S')
        choice = request.form["candidates"]
        database.Database.add_vote(database.Database(), ipAddress, todayDate, choice)
        return render_template('submitted.html')


def create_app():
    app.config["DEBUG"] = True
    app.add_url_rule("/", view_func=index)
    app.add_url_rule("/submit", view_func=submit, methods=["GET", "POST"])
    db = database.Database()
    app.config["db"] = db


if __name__ == "__main__":
    create_app()
    app.run(host="localhost", port=8080, debug=True)


