from flask import Flask, render_template, request
import initializeDatabase
import database

global app, dbConnector
app = Flask(__name__)
dbConnector = initializeDatabase.init()


def index():
    return render_template('index.html')


def submit():
    if request.method == "GET":
        return render_template('submitted.html')
    else:
        if request.form["voterIdBox"] == "":
            return render_template('missingInfo.html')
        if request.form["candidates"] is None:
            return render_template('missingInfo.html')
        if database.vote_already_submitted(request.form['voterIdBox']) == "yes":
            return render_template('alreadyVoted.html')
        print("please use another device next")
        if database.check_if_not_lace_machine(request.environ['REMOTE_ADDR']) == "no":
            return render_template('useAnotherDevice.html')
        voterId = request.form["voterIdBox"]
        print("validating voterId next")
        if validateVoterId(voterId) == "invalid":
            return render_template('missingInfo.html')
        ipAddress = request.environ['REMOTE_ADDR']
        choice = request.form["candidates"]
        database.add_vote(voterId, ipAddress, choice)
        return render_template('submitted.html')


def results():
    craigVotes, shaqVotes, jordanVotes = database.get_votes()
    return '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Indescision 2020 ' \
           'Results</title></head><body><ul><li>Craig Shue: ' + str(craigVotes) + '</li><li>Land Shaq: ' + str(shaqVotes) + '</li><li>Air Jordan: ' \
           + str(jordanVotes) + '</li></ul></body></html>'


def create_app():
    app.config["DEBUG"] = True
    app.add_url_rule("/", view_func=index)
    app.add_url_rule("/submit", view_func=submit, methods=["POST"])
    app.add_url_rule("/results", view_func=results, methods=["GET"])

def validateVoterId(voterId):
    if len(voterId) != 27:
        return "invalid"
    if voterId.isnumeric():
        return "valid"


if __name__ == "__main__":
    create_app()
    app.run(host="localhost", port=8080, debug=True)


