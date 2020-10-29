from server import dbConnector

db = dbConnector
cursor = db.cursor()


def vote_already_submitted(voterId):
    select_statement = "SELECT voterId from votes where voterId = %s;"
    data = voterId
    rows = cursor.execute(select_statement, data)
    if rows.__sizeof__() != 0:
        return "yes"
    else:
        return "no"


def check_if_lace_machine(ipAddress):
    select_statement = "SELECT ipAddress from votes WHERE ipAddress NOT IN (SELECT ipAddress FROM laceMachines) " \
                       "AND ipAddress = %s; "
    data = ipAddress
    rows = cursor.execute(select_statement, data)
    if rows.__sizeof__() != 0:
        return "no"
    else:
        return "yes"


def get_votes():
    select_statement = "SELECT choice, count(*) from votes group by choice;"
    rows = cursor.execute(select_statement)
    craigShoeCount = 0
    landShaqCount = 0
    airJordanCount = 0
    if rows is not None:
        for row in rows:
            if row[0] == "Craig Shoe":
                craigShoeCount = row[1]
            if row[0] == "Land Shaq":
                landShaqCount = row[1]
            if row[0] == "Air Jordan":
                airJordanCount = row[1]

    return craigShoeCount, landShaqCount, airJordanCount


def add_vote(voterId, ipAddress, date, choice):
    try:
        insertStatement = ("INSERT INTO votes (voterId, ipAddress, currentDate, choice)"
                           "value (%s, %s, %s, %s);")
        data = (voterId, ipAddress, date, choice)
        cursor.execute(insertStatement, data)
        db.commit()
    except dbConnector.errors.IntegrityError:
        return "integrityError"
