"""Script to initialize database"""
import mysql.connector
import getpass
import src.db_con as db_con


class DataBaseNotFound (Exception):
    pass


while True:

    usr = input("user: ")
    pss = getpass.getpass("pass: ")

    try:
        db = db_con.connect(usr,pss)
        break
    except mysql.connector.errors.ProgrammingError:
        print("Invalid user/password, please try again....")


my_cursor = db.cursor(buffered=True)

my_cursor.execute("CREATE DATABASE eventsdb10")


my_cursor.execute("SHOW DATABASES")
# TODO create a check for database creation
if not my_cursor:
    my_cursor.close()
    db.close()
    raise DataBaseNotFound("Database not found!")

my_cursor.close()
db.close()
print("database created.")