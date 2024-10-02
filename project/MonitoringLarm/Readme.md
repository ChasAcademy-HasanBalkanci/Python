1. This application monitors the system, lets users set alarms, and sends notifications via email when those alarms are triggered. It also logs all events and saves the alarms for persistence across runs. The program contains functionality for monitoring CPU, memory, and disk usage, setting alarms, logging events, and sending email notifications when alarms are triggered. The program is modular, using separate files for different functionalities. 

2. File structure for monitoring CPU, memory, and disk usage is described in the following:

3. MonitoringLarm_app/

 alarms.py        # Alarm creation and management. This file manages alarm creation, display, and removal.
 logger.py        # Logging functionality. This file handles logging of program events.
 main.py          # Main menu and program flow. This file contains the main menu and logic for handling user choices.
 menu.py          # Menu provides the main menu interface.
 monitor.py       # System monitoring. This file handles system monitoring using the psutil library.
 settings.json    # Persistent alarm settings file
 email_notifier.py# Email notifications when an alarm is triggered. This file sends email notifications using SendGrid when an alarm is triggered.
 utils.py         # Utility functions (e.g., input validation)'

4. In the app, the following libraries are used:

* psutil:

For monitoring system resources like CPU, memory, and disk usage.
Install via pip install psutil. How to install: Go to Python/Python312/Lib/: and run "pip istall psutil"

* sendgrid:

To send email notifications when alarms are triggered.
Install via pip install sendgrid. In same case you could need to install the sendgrid in your system settings:
pip install sendgrid

* json (Standard Python Library):

For saving and loading alarm configurations to/from a JSON file for persistence.

* logging (Standard Python Library):

For logging program events, including alarm configurations, monitoring actions, and errors.

* datetime (Standard Python Library):

To generate timestamps for logging events.

