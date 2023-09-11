""""
module for database communication
"""

import mysql.connector


def connect(user,password):
    r"""connects to the database"""
    db = mysql.connector.connect(
        host="localhost",
        user=user,
        password=password
    )
    return db


def save_event(**event):
    r"""inserts/updates event to the database"""
    pass


def delete_event(event_id):
    r"""deletes event"""


