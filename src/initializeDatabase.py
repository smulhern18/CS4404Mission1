import mysql.connector as mysql_connector

def init():
    db = mysql_connector.connect(
        host = "localhost",
        user = "CS4404",
        password = "ox06ox06",
        database = "CS4404"
    )

    db.cursor().execute("CREATE TABLE IF NOT EXISTS votes ( "
                            "voterId varchar(27) not null,"
                            "ipAddress varchar(16) not null,"
                            "choice varchar(128) not null,"
                        " primary key(voterId))")

    db.cursor().execute("CREATE TABLE IF NOT EXISTS laceMachines "
                        "(ipAddress varchar(16) not null, "
                        "primary key(ipAddress))")
    return db

    if __name__ == "__main__":
        init()
