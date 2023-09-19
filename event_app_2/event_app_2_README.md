## Helloevent v01
### Description
App that reads and saves event data using MySQL as a database with web GUI.

# TODO:
* Users groups, users see only events from associated groups
* set up roles
* unit tests

# DONE:
* Login to the system
  * with username/login
  * create account
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
    * lead person
  * pagination in Monitor
  * search:
    * by name
    * by location
  * monitor shows 50 events from the list as one-liners
    * with possibility to change number of displayed events
    * there is a pagination in event monitor for not displayed events
    * Event View can be opened from monitor
* Event View 
  * events comments
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
-event_start_date - valid date, editable for events from yesterday to the future, includes start_hour
-event_start_date - valid date, optional, cannot be in past due to event_start_date, includes end_hour
-event_description - 10 to 255 characters, editable
-lead_person - up to 255 characters, editable
-event_ticketed - bool, editable
-event_price  - int, editable if event_ticketed, in PLN
```

## Environment setup
* install python 3.11.x
* setup virtual environemnt
* install django in the virtual environment
* set up super user 
* set up database for Event model

## release notes:
#### v version
* sth