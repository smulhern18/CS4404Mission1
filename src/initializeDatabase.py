import mysql.connector as mysql_connector
import os

def init():
    db = mysql_connector.connect(
        host = "localhost",
        user = "CS4404",
        password = "ox06ox06",
        database = "CS4404"
    )

    db.cursor().execute("CREATE TABLE IF NOT EXISTS votes ( "
                            "ipAddress varchar(16) not null,"
                            " currentDate date not null,"
                            " choice varchar(128) not null,"
                        " primary key(ipAddress, currentDate))")
    return db

    if __name__ == "__main__":
        init()
