# hairhut
This is a simple appointment scheduling application for a hypothetical hair salon.

Source Files
interface.py
interface.py contains the main function which creates an appointments object for the run of the program, generates available dates, and displays the initial Hair Hut menu interface. It then runs the menu_select function, also contained in interface.py, to take user input and run the appropriate method or function.
scheduler.py
scheduler.py contains the majority of functions used in scheduling. It takes user input for customer name, service (i.e., ‘Haircut only’ or ‘Shampoo & Haircut’), date, and time and adds them to the existing appointments object. scheduler.py also contains the generate_dates() function used in interface.py to create a list of available dates for scheduling.
appointments.py
appointments.py contains the Appointments class. This class represents all of the appointments currently scheduled. It stores them in a list. It sorts appointments chronologically by time of appointment, not by time of creation. It prints all appointments.
date.py
date.py contains the Date class. This class represents the dates that you can schedule appointments. It stores day, month, and year values as integers. It stores a string of the date in text according to US convention. It stores a list of available times for appointments from 9am to 5pm.

Running the Program
	To run the program, run ‘interface.py’ in the Terminal/Console/Command Prompt with Python 3. This program was written for Python version 3.7.2 and may not function correctly in earlier versions.

Design Considerations
Multiple dates - Though not expressly called for in the assignment, choosing between multiple dates seemed an essential feature. I often have to schedule my haircut appointments a day or two in advance. In future builds, the generate_dates function should be expanded to provide more dates or take user input for date creation.

Appointment sorting - Initially the list of appointments were printed in order of creation. A hairdresser would likely prefer their appointments ordered by time from soonest to most distant. The appointments method sort_apps now sorts in this manner.

Validating input - At each point of user input, the program verifies that the user has supplied valid input. For invalid input, the program explains why it is invalid and prompts the user to reenter input.

Times display - The time display initially provided a lengthy single column but was reformatted to provide three columns. The “BOOKED” signifier prevents users from double booking the same time (by selecting a booked time or selecting a time immediately before a booked time). In future builds, these unbooked but unavailable times should be flagged in the UI.

Other improvements for future builds - User should be able to go back through menus if they want to make a change. User should be able to modify or delete existing appointments. User should be able to exit the program at any point (not just the main menu). A GUI with mouse integration would likely be more user-friendly.
