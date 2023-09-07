# event_app v1.1
``requires: tinydb``
### Description
program that reads and saves event data using tinydb as database.
to play around, you can use ``create_events(n)`` function to generate ``n`` number of events.

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
#### v1.1
* added documentation
* small cleanup
* enhanced delete_event() output

#### v1
* introducing Event Application
 