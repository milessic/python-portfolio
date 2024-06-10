# Miłosz Jura milessic 2023
import os
import re
import tinydb
import readline
from python_sryton import PythonSryton
from tinydb.operations import set

# to play with the program, you can use "create_events(n)" function, where n is number of generated events.
# or you just can create them one by one :)

current_version = "v1.3"
"""Change log
----1.3:
- added Edit Event possibility
- added possiblity to open Event from Monitor using one command
- added history support
- added PythonSryton
"""

muszelka = PythonSryton()

class DatabseNotFoundError(Exception):
    r"""exception to raise in case db.json not found"""
    pass

# check for db existance
try:
    db = open("db.json", "r")
    db.close()
    db_exist = True
except FileNotFoundError:
    db_exist = False

if not db_exist:
    raise DatabseNotFoundError("Database not found, have you initialized it? To initialize it use database_init.py script")

db = tinydb.TinyDB('db.json')
events = db.table('events')
Events = tinydb.Query()


def clear():
    r"""clears console based on user OS"""
    os.system('cls' if os.name == 'nt' else 'clear')
    

def set_event_name():
    r"""validation function for event_name, returns validaated event_name"""
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
    r"""validation function for event_date, returns validated event_date"""
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
    r"""validation function for event_start_hour and event_end_hour,
    if mandatory == True: event_start_hour
    if mandatory == False: event_end_hour
    returns validated event_hour"""
    # mandatory - True means start hour, False means end hour
    print(mandatory)
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
    r"""validation function for event_description, returns validated event_description"""
    while True:
        ev_description = input("*Event Description: ")
        if len(ev_description) < 10:
            print("---!!! Criteria not met, event description has to be at least 10 characters long.")
        elif len(ev_description) > 80:
            print("---!!! Criteria not met, event description can be max 80 characters long.")
        else:
            return ev_description


def set_event_ticketed():
    r"""validation function for event_ticketed, returns validated event_ticketed"""
    while True:
        ev_ticketed = input("*Event Ticketed (True/False): ")
        if ev_ticketed.upper() == "FALSE":
            return False
        elif ev_ticketed.upper() == "TRUE":
            return True
        else:
            print("---!!! Criteria not met, event ticketed can be \"True\" or \"False\"!")


def set_event_price(ticketed):
    r"""validation function for event_price, returns validated event_price"""
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


def set_lead_person():
    r"""validation function for event_lead_person, returns validated event_lead_person"""
    while True:
        ev_lead_person = input("Lead person: ")
        if len(ev_lead_person) >= 20:
            print("---!!! Criteria not met, lead person can be max 20 characters long!")
        else:
            return ev_lead_person


def create_event():
    r"""Opens Event creation window and goes through event creation funnel field by field,
        using validation functions.

        After each field is properly filled, creates new record in database
        returns created event id
        """
    # function to create an event, validations are part of this function.
    clear()
    print("===Event creation,\n---fill each field one by one\n---fields with * have to be filled\n---fields wihout * can be left empty")
    ev_name = set_event_name()
    ev_date = set_event_date()
    ev_start_hour = set_event_hour(True)
    ev_end_hour = set_event_hour(False)
    ev_description = set_event_description()
    ev_ticketed = set_event_ticketed()
    ev_price = set_event_price(ev_ticketed)
    ev_lead_person = set_lead_person()
    new_event = {'event_id': 0, 'event_name': ev_name, 'event_date': ev_date, 'event_start_hour': ev_start_hour, 'event_end_hour': ev_end_hour, 'event_description': ev_description, 'event_ticketed': ev_ticketed, 'event_price': ev_price, 'lead_person': ev_lead_person}
    ev_id = events.insert(new_event)
    events.update(set('event_id', ev_id), Events.event_id == 0)
    print(f"Event with ID {ev_id} created")
    return ev_id


def edit_event(ev_id:int):
    ev_id = int(ev_id)
    found_event = return_event(ev_id)
    new_event = found_event
    inp = ""
    all_fields = "\t - " + "\n\t - ".join([f.replace('_', ' ') for f in found_event.keys() if f != 'event_id'])
    all_fields.replace("lead person", "event lead person")
    print(f"What field do you want to edit?\n{all_fields}\nType new value and press enter\ntype FIELD NAME, SAVE or CANCEL to exit")
    first_iteration = True
    while True:
        if inp.upper() == "DONE":
            break
        inp = input(f"{'------------\nEDIT, SAVE or CANCEL\n' if not first_iteration else ''}>>> ")
        first_iteration = False
        if "SAVE" in inp.upper():
            save = True
            break
        if "CANCEL" in inp.upper():
            save = False
            break
        try:
            print(f"Field '{inp.lower()} is: \'{found_event[inp.replace(' ', '_')]}\'")
            new_value = print(f"ENTERING NEW {inp}")
        except KeyError:
            print(f"There is no field '{inp}'!")
            continue
        # new_event[inp.replace(' ', '_')] = new_value
        try:
            new_event[inp.replace(' ', '_')] = globals().get(f'set_{inp.replace(" ", "_")}')() if 'hour' not in inp.lower() else set_event_hour(True if 'start' in inp else False) 
            input(f"EDITED FIELD {inp}, press ENTER")
        except Exception as e:
            print(f"COULD NOT SET FIELD '{inp}' due to {e}!")
    if save:
        update = events.update(new_event, Events.event_id == ev_id)
    input(f"{'Event ID:' + str(ev_id) + ' saved' if save else 'Cancelling operation...'}\n>>> PRESS ENTER ")
    
def delete_event(ev_id):
    r"""deletes event from database, returns info that if event was deleted"""
    try:
        events.remove(doc_ids=[int(ev_id)])
    except:
        return f"\n---event id:{ev_id} COULD NOT be deleted..."


def return_event(ev_id):
    r"""returns event dictionary due to provided event id"""
    # returning event with given id as dictionary
    ev_id = int(ev_id)
    try:
        found_event = events.get(doc_id=ev_id)
        if found_event:
            return found_event
        else:
            return f"No event with id {ev_id} found!"
    except:
        return f"Error: No event with id {ev_id} found!"


def search_for_event(query_criteria, query_value):
    r"""return search results for event due to provided query, search is insensitive"""

    found_events = events.search(Events[query_criteria].matches(f"[\s\S]*({query_value})[\s\S]*", flags=re.IGNORECASE))
    if not found_events:
        print(f'No event found for query: "{query_criteria}:{query_value}"')
        return
    print(f"Found {len(found_events)} events:")
    for event in found_events:
        print(return_event_line(event["event_id"]))
#    print(found_events)


def return_event_line(ev_id):
    r"""returns event as one line with following information:
            - event_name
            - event_date
            - event_start_hour
            - event_end_hour
    """

    event = return_event(ev_id)
    t_zeros = '0'*(3-len(str(ev_id)))
    return f"id:{t_zeros}{ev_id} - {event['event_name']} - {event['event_date']}, {event['event_start_hour']}{' - '+event['event_end_hour'] if event['event_end_hour']!= '' else ''}"


def print_event_card(ev_id):
    r"""prints pretty event_card with all event information."""

    event = return_event(ev_id)
    t = '\n\t'
    print(f"""{event["event_name"]}\n\tdate: {event["event_date"]}\tstart: {event["event_start_hour"]}, end: {event["event_end_hour"] if event["event_end_hour"] != "" else '---'}
\tdesc: {event["event_description"][0:40]}
\t{event["event_description"][40:]}
\tprice: {'free' if event["event_ticketed"] == False else event["event_price"]}{t + 'leads: '+ event["lead_person"] if event["lead_person"] != "" else ''}""")


def open_event(ev_id):
    r"""opens event card with options to delete, (in future) edit or exit"""
    while True:
        clear()
        print(f"===EVENT ID {ev_id}")
        print_event_card(ev_id)
        input_event = input("===options:\n\t-EDIT\n\t-DELETE\n\t-go BACK to monitor\n>>> ")

        if "BACK" in input_event.upper():
            return
        elif "EDIT" in input_event.upper():
            edit_event(ev_id)
        elif "DELETE" in input_event.upper():
            confirm = input("Are you sure? YES/NO\n>>> ")
            if "NO" in confirm.upper():
                continue
            elif "YES" in confirm.upper():
                input(f"{delete_event(ev_id)}\npress ENTER to continue\n>>>")
                return


def show_event_monitor():
    r"""shows event monitor with last created 25 events,
        user can navigate through event pages,
        open events or exit.
    """

    nl = "\n"
    event_list_num = 25
    page = 0
    while True:
        clear()
        total_events_in_db = len(events)
        max_pages = total_events_in_db//event_list_num+1
        first_monitor_event = total_events_in_db-(event_list_num*page)
        print(f"===Reported Events:\n---page {page+1} of {max_pages}\n---found {total_events_in_db} events\n---displaying {event_list_num} events")
        event_max = 0
        if total_events_in_db == 0:
            print("\n<<no event created...>>\n")
        for event in range(first_monitor_event,0,-1):
            while True:
                try:
                    print(return_event_line(event))
                    event_max += 1
                    break
                except TypeError:
                    event += 1
                    continue
            if event_max == event_list_num:
                break
        if event_max < event_list_num:
            there_are_next = False
        else:
            there_are_next = True
        user_input = input(f"===options:{f'{nl}-- view NEXT 50' if there_are_next else '' }{f'{nl}-- view PREVIOUS 50' if page != 0 else ''}\n-- OPEN event\n-- EXIT to main menu\n>>> ")
        if "EXIT" in user_input.upper():
            return
        elif "NEXT" in user_input.upper() and there_are_next:
            page += 1
        elif "PREVIOUS" in user_input.upper() and page != 0:
            page -= 1
        elif "OPEN" in user_input.upper():
            input_as_list = user_input.split(sep=" ")
            if len(input_as_list) == 2:
                try:
                    input_ev_id = int(input_as_list[1])
                except (ValueError, IndexError):
                    try:
                        input_ev_id = input("type event id to open:\n>>> ")
                    except TypeError:
                        input("invalid id typed, press ENTER to continue...")
                        continue
            open_event(input_ev_id)
            pass


while True:
    clear()
    menu_choice = input("===event_app v1 Miłosz Jura milessic 2023\nSelect appropiate option:\n-CREATE new event\n-SEARCH\n-open MONITOR\n-EXIT\n>>> ")
    if "EXIT" in menu_choice.upper():
        break
    elif "CREATE" in menu_choice.upper():
        fresh_event = create_event()
        create_input = input("===choose between:\n-VIEW created event\n-go back to MENU\n>>> ")
        if "VIEW" in create_input.upper():
            open_event(fresh_event)
            input("Press ENTER to open menu\n>>>")
        else:
            continue
    elif "SEARCH" in menu_choice.upper():
        clear()
        event_to_show = input("=== Event Search\n!guide:\n\tto use search first type query criteria, then after colon sign type value to serch.\ne.g:\n\tid:4  or  event_name:job interview\n>>> ")
        if event_to_show[:2].lower() == "id":
            try:
                print_event_card(int(event_to_show[3:]))
            except:
                print(f"Didn't find event with id {event_to_show[3:]}...")
        elif event_to_show[:10].lower() == "event_name" or event_to_show[:10].lower() == "event_date":
            search_for_event(event_to_show[:10].lower(), event_to_show[11:])
        else:
            print("Only searchh by id, date or event_name are supported for now.")
        input("Press ENTER to open menu\n>>> ")
        continue
    elif "MONITOR" in menu_choice.upper():
        show_event_monitor()
    elif "PYTHONSRYTON" in menu_choice.upper():
        muszelka.run(locals())
    else:
        input("Unknown command, press ENTER to continue... ")
input("press ENTER to close ")
