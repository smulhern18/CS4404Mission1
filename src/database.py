from server import dbConnector

global db, cursor
db = dbConnector
cursor = db.cursor()


class Database:

    def add_vote(self, ipAddress, date, choice):
        try:
            insertStatement = ( "INSERT INTO votes (ipAddress, currentDate, choice)"
                "value (%s, %s, %s)" )
            data = (ipAddress, date, choice)
            cursor.execute(insertStatement, data)
            db.commit()
        except dbConnector.errors.IntegrityError:
            pass

    def get_votes(self, movie_key):
        selectStatement = "SELECT * from votes"
        cursor.execute(selectStatement)