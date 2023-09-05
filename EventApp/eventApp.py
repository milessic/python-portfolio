import os
import re
import json
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
def create_event():
    clear()
    print("===Event creation,\n\t-fill each field one by one\n\t-fields with * have to be filled\n\t-fields wihout * can be left empty")
    ev_name = input("*Event Name: ")
    ev_date = input("*Event Date: ")
    ev_start_hour = input("*Event Start Hour: ")
    ev_end_hour = input("Event End Hour: ")
    ev_description = input("*Event Description: ")
    ev_ticketed = input("*Event Ticketed (True/False): ")
    if ev_ticketed.upper() == "FALSE":
        ev_ticketed = False
    if ev_ticketed:
        ev_price = input("*Event Price: ")
    else:
        ev_price = 0
    ev_lead_person = input("Lead person: ")
    new_event = {'event_id': 0, 'event_name': ev_name, 'event_date': ev_date, 'event_start_hour': ev_start_hour, 'event_end_hour': ev_end_hour, 'event_description': ev_description, 'event_ticketed': ev_ticketed, 'event_price': ev_price, 'lead_person': ev_lead_person}
    ev_id = future_events_table.insert(new_event)
    future_events_table.update(set('event_id', ev_id), Events.event_id == 0)
    input(f"Event with ID {ev_id} created")
    return ev_id

def return_event(ev_id):
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
