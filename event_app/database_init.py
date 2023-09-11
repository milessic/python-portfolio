# Miłosz Jura milessic 2023

import tinydb
import os


class DatabaseInitError(Exception):
    pass


class DatabaseAlreadyInitialized(Exception):
    pass


def check_db_existance():
    try:
        db_file = open("db.json", "r")
        db_file.close()
        db_exist = True
    except FileNotFoundError:
        db_exist = False

    return db_exist


db_status = check_db_existance()
if db_status:
    raise DatabaseAlreadyInitialized("Database is already initialized!")
else:
    db = tinydb.TinyDB('db.json')

db_status = check_db_existance()

if not db_status:
    raise DatabaseInitError()
else:
    print(f"Database successfully initialized at {os.getcwd()} as db.json")