import os
import re
import tinydb
from tinydb.operations import set

# create database if not set
try:
    db = open("db.json", "r")
    db.close()

except FileNotFoundError:
    db = open("db.json", "x")
    db.close()

finally:
    db = tinydb.TinyDB('db.json')
    future_events_table = db.table('future_events')
    past_events_table = db.table('past_events')
    Events = tinydb.Query()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_event_name():
    # validation for event name, cannot be empty, has to be 3-20 characters long
    while True:
        ev_name = input("*Event Name: ")
        if len(ev_name) == 0:
            print("---!!! Criteria for EVENT NAME not met, it can't be empty!")
        elif len(ev_name) <= 3 or len(ev_name) >= 20:
            print("---!!! Criteria for EVENT NAME not met, it has to be at least 3 and up to 20 characters long")
        else:
            return ev_name


def set_event_date():
    while True:
        ev_date = input("*Event Date: ")
        if ev_date == '':
            print("---!!! Criteria not met, event date cannot be empty!")
            continue
        try:
            day_validation = 32 > int(ev_date[:2]) > 0
        except ValueError:
            day_validation = False
        try:
            month_validation = 13 > int(ev_date[3:5]) > 0
        except ValueError:
            month_validation = False

        if re.search(r"\d\d-\d\d-\d\d\d\d$", ev_date):
            format_validation = True
        else:
            print("---!!! Criteria not met for format, please enter date in format DD-MM-YYYY")
            format_validation = False

        if not day_validation:
            print("---!!! Criteria not met for DAY,   please enter date in format: DD-MM-YYYY")
        if not month_validation:
            print("---!!! Criteria not met for MONTH, please enter date in format: DD-MM-YYYY")
        if month_validation and day_validation and format_validation:
            return ev_date


def set_event_hour(mandatory):
    # mandatory - True means start hour, False means end hour
    while True:
        ev_hour = input(f"{'*' if mandatory else ''}Event {'Start' if mandatory else 'End'} Hour: ")
        if ev_hour == '':
            if mandatory:
                print("---!!! Event Start hour cannot be empty!")
                continue
            else:
                return ''
        try:
            hour_validation = 24 >= int(ev_hour[:2]) >= 0
        except ValueError:
            hour_validation = False
        try:
            minutes_validation = 60 >= int(ev_hour[3:5]) >= 0
        except ValueError:
            minutes_validation = False

        if re.search(r"\d\d:\d\d$", ev_hour):
            format_validation = True
        else:
            print("---!!! Criteria not met for format, please enter hour in format: HH:MM")
            format_validation = False

        if not hour_validation:
            print("---!!! Criteria not met for HOUR,   please enter hour in format: HH:MM")
        if not minutes_validation:
            print("---!!! Criteria not met for MINUTES,please enter hour in format: HH:MM")
        if hour_validation and minutes_validation and format_validation:
            return ev_hour


def set_event_description():
    while True:
        ev_description = input("*Event Description: ")
        if len(ev_description) < 10:
            print("---!!! Criteria not met, event description has to be at least 10 characters long.")
        elif len(ev_description) > 80:
            print("---!!! Criteria not met, event description can be max 80 characters long.")
        else:
            return ev_description


def set_event_ticketed():
    while True:
        ev_ticketed = input("*Event Ticketed (True/False): ")
        if ev_ticketed.upper() == "FALSE":
            return False
        elif ev_ticketed.upper() == "TRUE":
            return True
        else:
            print("---!!! Criteria not met, event ticketed can be \"True\" or \"False\"!")


def set_event_price(ticketed):
    if ticketed:
        while True:
            try:
                ev_price = float(input("*Event Price: "))
                if ev_price >= 0:
                    return ev_price
                else:
                    print("---!!! Criteria not met for Event price, it has to be a positive value!")
            except ValueError:
                print("---!!! Criteria not met for Event price, it has to be a number!")
    else:
        return 0


def set_event_lead_person():
    while True:
        ev_lead_person = input("Lead person: ")
        if len(ev_lead_person) >= 20:
            print("---!!! Criteria not met, lead person can be max 20 characters long!")
        else:
            return ev_lead_person


def create_event():
    # function to create an event, validations are part of this function.
    clear()
    print("===Event creation,\n\t-fill each field one by one\n\t-fields with * have to be filled\n\t-fields wihout * can be left empty")
    ev_name = set_event_name()
    ev_date = set_event_date()
    ev_start_hour = set_event_hour(True)
    ev_end_hour = set_event_hour(False)
    ev_description = set_event_description()
    ev_ticketed = set_event_ticketed()
    ev_price = set_event_price(ev_ticketed)
    ev_lead_person = set_event_lead_person()
    new_event = {'event_id': 0, 'event_name': ev_name, 'event_date': ev_date, 'event_start_hour': ev_start_hour, 'event_end_hour': ev_end_hour, 'event_description': ev_description, 'event_ticketed': ev_ticketed, 'event_price': ev_price, 'lead_person': ev_lead_person}
    ev_id = future_events_table.insert(new_event)
    future_events_table.update(set('event_id', ev_id), Events.event_id == 0)
    input(f"Event with ID {ev_id} created")
    return ev_id


def return_event(ev_id):
    # returning event with given id as dictionary
    ev_id = int(ev_id)
    try:
        found_event = future_events_table.get(doc_id=ev_id)
        if found_event:
            return found_event
        else:
            return f"No event with id {ev_id} found!"
    except:
        return f"Error: No event with id {ev_id} found!"


def search_for_event(query_criteria, query_value):
    found_events = future_events_table.search(Events[query_criteria].matches(f"[\s\S]*({query_value})[\s\S]*", flags=re.IGNORECASE))
    for event in found_events:
        print(f"Found event with id: {event['event_id']} - {event['event_name']} - {event['event_date']}, {event['event_start_hour']} - {event['event_end_hour']}")
    if not found_events:
        print(f'No event found for query: "{query_criteria}:{query_value}"')
#    print(found_events)


def print_event(ev_id):
    event = return_event(ev_id)
    t = '\n\t'
    print(f"""{event["event_name"]}\n\tdate: {event["event_date"]}\tstart: {event["event_start_hour"]}, end: {event["event_end_hour"] if event["event_end_hour"] != "" else '---'}
\tdesc: {event["event_description"][0:40]}
\t{event["event_description"][40:]}
\tprice: {'free' if event["event_ticketed"] == False else event["event_price"]}{t + 'leads: '+ event["lead_person"] if event["lead_person"] != "" else ''}""")


while True:
    clear()
    menu_choice = input("Select appropiate option:\n-CREATE new event\n-UPDATE existing event\n-SEARCH\n-VIEW FUTURE events\n-VIEW PAST events\n-EXIT\n>>> ")
    if "EXIT" in menu_choice.upper():
        break
    elif "CREATE" in menu_choice.upper():
        fresh_event = create_event()
        create_input = input("choose between:\n-VIEW created event\n-go back to MENU\n>>> ")
        if "VIEW" in create_input.upper():
            print_event(fresh_event)
            input("Press ENTER to open menu\n>>>")
        else:
            continue
    elif "UPDATE" in menu_choice.upper():
        pass
    elif "SEARCH" in menu_choice.upper():
        clear()
        event_to_show = input("=== Event Search\n!guide:\n\tto use search first type query criteria, then after colon sign type value to serch.\ne.g:\n\tid:4  or  event_name:job interview\n>>> ")
        if event_to_show[:2].lower() == "id":
            try:
                print_event(int(event_to_show[3:]))
            except:
                print(f"Didn't find event with id {event_to_show[3:]}...")
        elif event_to_show[:10].lower() == "event_name" or event_to_show[:10].lower() == "event_date":
            search_for_event(event_to_show[:10].lower(), event_to_show[11:])
        else:
            print("Only searchh by id, date or event_name are supported for now.")
        input("Press ENTER to open menu\n>>> ")
        continue
    elif "VIEW FUTURE" in menu_choice.upper():
        pass
    elif "VIEW PAST" in menu_choice.upper():
        pass
    else:
        input("Unknown command, press ENTER to continue... ")
input("press ENTER to close ")
