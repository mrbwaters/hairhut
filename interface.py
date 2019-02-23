import scheduler
import appointments
import date
import os


def main():
    """The main function creates an appointments object and populates
    available days for scheduling using generate_dates function. It then
    provides the user with a menu interface within a while loop. It
    calls the menu_select function, which returns a bool that can exit the
    while loop.
    """
    apps = appointments.Appointments()
    available_dates = scheduler.generate_dates()
    repeat = True
    # While loop repeats until menu_select returns False.
    while repeat:
        os.system('clear')
        print("Welcome to The Hair Hut scheduler!"
              "\n\nWhat would you like to do?"
              "\n1. List existing appointments"
              "\n2. Schedule a new appointment"
              "\n3. Exit scheduler")
        # Return of menu_select determines whether while loop repeats
        repeat = menu_select(available_dates, apps)


def menu_select(available_dates, apps):
    """The menu_select function takes user input for the interface menu.
    While loop repeats if a user inputs anything besides a menu integer.
    """
    while True:
        choice = input("\nType the number of your choice and press 'Enter': ")
        # If user chooses list appnts, call show_apps method and exit loop.
        if choice == '1':
            os.system('clear')
            apps.print_apps()
            input("\nPress 'Enter' to continue.")
            return True
        # If user chooses schedule, call schedule function and exit loop.
        elif choice == '2':
            os.system('clear')
            scheduler.scheduler(available_dates, apps)
            input("\nPress 'Enter' to continue.")
            return True
        # If user chooses to exit, exit loop and return False.
        elif choice == '3':
            print("\nThank you for being a proud employee of The Hair Hut!")
            return False
        # If user input is invalid, display message and repeat loop.
        else:
            print("\nInvalid input. Input must be '1', '2', or '3'.")


# Run the main function.
if __name__ == '__main__':
    main()
