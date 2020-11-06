from server import dbConnector

db = dbConnector
cursor = db.cursor(buffered=True)


def vote_already_submitted(voterId):
    select_statement = "SELECT voterId from votes where voterId = '" + str(voterId) + "';"
    cursor.execute(select_statement)
    if cursor.rowcount <= 0:
        cursor.reset()
        return "no"
    else:
        cursor.reset()
        return "yes"


def check_if_not_lace_machine(ipAddress):
    select_statement = "SELECT ipAddress FROM laceMachines WHERE( ipAddress = '" + ipAddress + "');"
    cursor.execute(select_statement)
    if cursor.rowcount > 0:
        cursor.reset()
        return "yes"
    else:
        cursor.reset()
        return "no"


def get_votes():
    select_statement = "SELECT choice, count(*) from votes group by choice;"
    cursor.execute(select_statement)
    rows = cursor.fetchall()
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
    cursor.reset()
    return craigShoeCount, landShaqCount, airJordanCount


def add_vote(voterId, ipAddress, choice):
    insertStatement = ("INSERT INTO votes (voterId, ipAddress, choice)" +
                       " values ('" + voterId + "', '" + ipAddress + "', '" + choice + "');")
    cursor.execute(insertStatement)
    db.commit()
    cursor.reset()
