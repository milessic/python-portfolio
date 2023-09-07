# python-portfolio
This is my portfolio for python stuff, if you are interested in games/applications, please have a sit!\nDescriptions of the applications are written in the order of creation.

If you are interested in my biggest project, which is private, please ask me about jdm_console_racer!

Projects I realized:
* guess_number v1
* event_app v1
* english_dictionary v01
* jdm_console_racer v01

## guess_number v1
This is my Guess The Number type of game, that features:
* uses tinydb as database
* saving highscore to file
* showing up-to-date HUD
* crate own exception and raising it to exit two layer while loop
* support of console clear for multiple systems

## event_app v1
requirements: tinydb
program that reads and saves event data using tinydb as database.
to play around, you can use create_events(n) function to generate n number of events.

* Event Search with query system
  * query works for name, id, date
* Event Monitor, where all events are displayed (from the newly created)
  * monitor shows 25 events from the list as one-liners
  * there is a paginatio in event monitor
  * events can be opened from monitor
* Event Creation
  * event have mandatory fields
* Event View:
  * event can be edited
  * event can be deleted
* events have the following structure in db:
  ```
    -event_id - int, auto-set
        -at initation is set to 0, true id is set at save
    -event_name - string
    -event_date - string
    -event_start_hour - string
    -event_end_hour - string
    -event_description - string
    -lead_person - string
    -event_ticketed - bool
    -evet_price - float
  ```

*** english_dictionary v1 ***
Calls to API and returns meaning of the word.
* saves history
* shows last 10 searched phrases that very succesfully serached
* uses Free Dictionary API
* shows word description and speech part
* handling of status codes