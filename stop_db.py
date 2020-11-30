# Pseudo Code to stop DB and get the backup

def stop_database():
    #run("systemctl stop postgresql.service")
    pass


def start_database():
    #run("systemctl start postgresql.service")
    pass


class DBHandler:
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()


def db_backup():
    #run("pg_dump database")
    pass


def main():
    with DBHandler():
        db_backup()