## program_name current_version
### Description
App that reads and saves event data using MySQL as a database with web GUI.

* Login to the system
  * with username/login
* Multiple users
* Multiple roles
  * user
  * admin
* Homepage elements:
  * Widget that shows next 3 events 
  * Create Event Tile
  * Monitor Tile
  * Quick Search widget (by id or name)
* Event Creation:
  * events have mandatory fields
  * there's Backend validation of fields
  * after Event creation user can:
    * create new event
    * open created event
    * go back to the Home page
* Event Monitor
  * filters:
    * created by
    * created within time range
    * event date within time range
  * search:
    * by name
    * by location
  * monitor shows 50 events from the list as one-liners
    * with possibility to change number of displayed events
    * there is a pagination in event monitor for not displayed events
    * Event View can be opened from monitor
* Event View 
  * event can be edited
    * there are different validation rules here
  * files can be uploaded
    * with type and size limits
  * comments can be provided
    * timestamp, comment creator, comment text
  * events can be deleted
    * they change state and are only displayed to admin users

#### Event validation for New Events:
```
-event_name - 3 to 80 characters, mandatory
-event_date - valid date, mandatory
-event_start_hour - valid hour, mandatory
-event_end_hour - valid hour, optional
-event_description - 10 to 200 characters, mandatory
-lead_person - up to 200 characters, optional
-event_ticketed - bool, mandatory
-event_price  - float, mandatory if event_ticketed
```
#### Event validation for Edit Event:
```
-event_name - 3 to 80 characters, only editable for admin
-event_date - valid date, editable for events from yesterday to the future
-event_start_hour - valid hour, editable
-event_end_hour - valid hour, editable
-event_description - 10 to 200 characters, editable
-lead_person - up to 200 characters, editable
-event_ticketed - bool, editable
-event_price  - float, editable if event_ticketed
```

## Environment setup
* install python 3.11.x
* pip install mysql-connector-python
* create database via ``db_init.py`` script

## release notes:
#### v version
* sth