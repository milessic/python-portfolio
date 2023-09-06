# python-portfolio
This is my portfolio for python stuff, if you are interested in games/applications, please have a sit!\nDescriptions of the applications are written in the order of creation.

If you are interested in my biggest project, which is private, please ask me about jdm-console-racer!

## guess_number
This is my Guess The Number type of game, that features:
* uses tinydb as database
* saving highscore to file
* showing up-to-date HUD
* crate own exception and raising it to exit two layer while loop
* support of console clear for multiple systems

## event_app
requirements: tinydb
program that reads and saves event data using tinydb.
* there is event search with query system
* upcomming events are listed in order from the most recent one 
* past events are listed in separate place in order from the most recent one
* event have mandatory fields
* future events:
  * can be edited
  * can be deleted
  * comment can't be provided
* past events
  * can't be edited
  * can't be deleted
  * comment can be provided
* events have the following structure in db:

  
    -event_id - int, auto-set
        -at initation is set to 0, true id is set at save
    -event_name - string, mandatory
        -3 to 20 characters
    -event_date - string, mandatory
        -format DD-MM-YYYY
    -event_start_hour - string, mandatory
        -format HH:MM
    -event_end_hour - string
        -format HH:MM or None
    -event_description - string, mandatory
        -10 to 80 characters
    -lead_person - string, not mandatory
        -up to 20 characters
    -event_ticketed - bool, mandatory
        -True or False
    -evet_price - float, mandatory if event_ticketed == True
