# python-portfolio
This is my portfolio for python stuff, if you are interested in games/applications, please have a sit!\nDescriptions of the applications are written in the order of creation.

If you are interested in my biggest project, which is private, please ask me about jdm_console_racer!

Projects I realized:
* guess_number v1
  * simple game featuring saving highscore as txt file and showing up-to-date HUD
* event_app v1
* english_dictionary v01
* jdm_console_racer v01


## event_app v1
requirements: tinydb
program that reads and saves event data using tinydb.
* there is event search with query system
  * query works this way: field_name:searched phrase,
  * e.g.: event_name:birthday will return all events that contain "birthday" in their names
* upcomming events are listed in order from the most recent one 
* past events are listed in separate place in order from the most recent one
* event creation uses following validation:
  * event_name = not empty, 3-20 characters long
  * event_date - not empty, in format DD-MM-YYY
  * event_start_hour - not empty, in format HH:MM
  * event_end_hour - can be empty, in format HH:MM
  * event_description - not empty, 10-80 characters long
  * lead_person - can be empty, up to 20 characters
  * event_ticketed - not empty, bool
  * event_price - if event_ticketed == True, not negative 
* future events:
  * can be edited
  * can be deleted
  * comment can't be provided
* past events
  * can't be edited
  * can't be deleted
  * comment can be provided
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