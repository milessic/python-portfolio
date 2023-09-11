# event_app v1.2

## Environment setup
* install python 3.11.x
* install python module ``tinydb``
* initialize database just by running script ``database_init.py``
* (optional) create event data via script ``create_data.py``:
  * as an argument pass number of events, e.g. ``python create_data.py --events 100`` to create 100 events.
* application can be run via ``event_app.py`` script

### Description
program that reads and saves event data using tinydb as database.

* Event Search with query system
  * query tested for name, id, date
* Event Monitor, where all events are displayed (starting from the newly created)
  * monitor shows 25 events from the list as one-liners
  * there is a pagination in event monitor
  * events can be opened from monitor
* Event Creation
  * event have mandatory fields
  * there is value validation for each field
* Event View:
  * event can be deleted
  * event can't be edited, not implemented
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


## release notes:
#### v1.2
* removed auto-init of database
* removed function to create dummy data from ``event_app.py``
* added ``database_init.py`` and ``create_data.py`` scripts
* restored clear module back to function inside ``event_app.py``

#### v1.1
* added documentation
* small cleanup
* enhanced delete_event() output

#### v1
* introducing Event Application
 