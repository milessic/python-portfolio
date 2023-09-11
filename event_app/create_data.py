# Miłosz Jura milessic 2023
import sys
import tinydb
from tinydb.operations import set


class WrongArgumentError(Exception):
    r"""Exception to raise in case of 1st argument not being int"""
    pass


class DataBaseNotFoundError(Exception):
    r"""Database not found, initialize it first"""
    pass

def create_events(number):
    r"""can be used to create number of events with dummy generated data"""

    # for testing
    test_event_names_1 = ['extensive', 'python', 'foo', 'john doe', 'cat', 'dog', 'parrot', 'penguin', 'porsche', 'milessic']
    test_event_names_2 = ['birthday', 'night', 'feeding', 'bar', 'picnic']
    from random import randint
    for i in range(number):
        random_name = f"{test_event_names_1[randint(0, len(test_event_names_2)-1)]} {test_event_names_2[randint(0, len(test_event_names_2)-1)]}"
        new_event = {'event_id': 0, 'event_name': f"{random_name}", 'event_date': '01-01-2023', 'event_start_hour': f'{randint(0,23)}:{randint(0,59)}',
                     'event_end_hour': f'{randint(0,23)}:{randint(0,59)}', 'event_description': 'this is test event', 'event_ticketed': True,
                     'event_price': randint(20,500), 'lead_person': 'system'}
        ev_id = events.insert(new_event)
        events.update(set('event_id', ev_id), tinydb.Query().event_id == 0)


# check for db existance
try:
    file = open("db.json", "r")
    file.close()
    db_exist = True
except FileNotFoundError:
    db_exist = False
if not db_exist:
    raise DataBaseNotFoundError("Database not initiliazed, please first use database_init.py script.")


db = tinydb.TinyDB('db.json')
events = db.table('events')


try:
    event_count = sys.argv[1]
    event_count = int(event_count)
    arg_format = True
except ValueError:
    arg_format = False
except IndexError:
    arg_format = False


if not arg_format:
    raise WrongArgumentError("Argument has to be int.")


create_events(event_count)
print(f"Created {event_count} dummy events")
