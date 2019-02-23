import appointments
import date


def scheduler(available_dates, apps):
    """The scheduler function takes a list of days and an appointments object.
    It calls a series of functions to store a customer name, which service the
    customer has scheduled, the scheduled day, the scheduled time. It prints a
    confirmation of the appointment and stores it in the appointments object.
    """
    print("--SCHEDULE NEW APPOINTMENT--")
    customer_name = enter_name()
    # Stores duration of service for use in choose_time function.
    service, duration = choose_service(customer_name)
    day = choose_day(customer_name, available_dates)
    # Stores time_index to pass to apps for sorting appointments by time.
    time, time_index = choose_time(customer_name, day, duration)
    print("\n%s has an appointment for %s on %s at %s." %(customer_name,
    service, day.date_text, time))
    apps.add_app(customer_name, service, day, time, time_index)


def enter_name():
    """The enter_name function takes user input for customer name and
    verifies that the user has not left this field blank. It returns the
    valid name. Future builds may check user input against a list of existing
    user accounts.
    """
    # While loop repeats until valid customer_name is input and returned.
    while True:
        customer_name = input("\nPlease type customer name and press 'Enter': ")
        if customer_name != '':
            return customer_name
        else:
            print("Invalid input. Customer must have a name.")


def choose_service(customer_name):
    """The choose_service function displays service options and takes user
    input about which service they are scheduling. It verifies that that the
    input is either 1 or 2. It returns both the str of the service and the
    number of the choice to be used as duration.
    """
    print("\nWould %s like a haircut or shampoo and haircut?"
          "\n1. Haircut only (30 minutes)"
          "\n2. Shampoo & Haircut (60 minutes)" %(customer_name))
    # While loop repeats until valid service_choice is input and returned
    while True:
        service_choice = input("\nType the number of your choice "
                               "and press 'Enter': ")
        if service_choice == '1':
            service = "Haircut only"
            return (service, service_choice)
        if service_choice == '2':
            service = "Shampoo & Haircut"
            return (service, service_choice)
        else:
            print("Invalid input. Input must be '1' or '2'.")


def choose_day(customer_name, available_dates):
    """The choose_day function displays day options and takes user input for
    which day they are scheduling. It verifies that the input is an integer
    value within the list of available days. It returns the chosen day object.
    """
    print("\nChoose a day for %s's haircut: " %customer_name)
    j = 1
    # For loops displays each day in available_dates list
    for i in available_dates:
        print("%i. %s" %(j, i.date_text))
        j += 1
    # While loop repeats until valid day_choice is input and returned.
    while True:
        day_choice = input("\nType the number of your choice "
                           "and press 'Enter': ")
        if day_choice.isdigit():
            if int(day_choice) <= len(available_dates) and int(day_choice) > 0:
                return available_dates[int(day_choice) - 1]
            else:
                print("Invalid input. Input is outside menu scope.")
        else:
            print("Invalid input. Input must be a positive integer.")


def choose_time(customer_name, day, duration):
    """The choose_time function displays formatted time options on the chosen
    day and takes user input for which they are scheduling. It verifies that
    the input is an integer value within the list of times and not already
    booked. It modifies the input times to 'BOOKED'. It returns both the time
    of the appointment and the time_index for use in sorting appointments
    by time.
    """
    print("\nChoose a time for %s's haircut on %s:" %(customer_name,
                                                      day.date_text))
    # Creates a list of numbers and times, parses them, and prints with buffer
    # This allows for three columns of times and cleaner presentation.
    column = []
    for i in range(32):
        column.append("%i. %s" %(i + 1, day.times[i]))
    # Blank space added to improve formatting. In future builds, find more
    # efficient way to format.
    column.append(" ")
    for a, b, c in zip(column[:11], column[11:22], column[22:33]):
        print('{:<30}{:<30}{:<}'.format(a, b, c))
    # While loop repeats until user enters valid, available input
    while True:
        time_choice = input("\nType the number of your choice "
                            "and press 'Enter': ")
        if time_choice.isdigit():
            if int(time_choice) <= 32 and int(time_choice) > 0:
                time_index = int(time_choice) - 1
                time = day.times[time_index]
                # If duration is 30 minutes check two 15 minute blocks
                if duration == '1':
                    if "BOOKED" in day.times[time_index:time_index + 2]:
                        print("That time is unavailable. Select another time.")
                    else:
                        # Book two 15 minute blocks and break while loop.
                        for booked in range(time_index, time_index + 2):
                            day.times[booked] = "BOOKED"
                        break
                # If duration is 60 minutes check four 15 minute blocks
                elif duration == '2':
                    if "BOOKED" in day.times[time_index:time_index + 4]:
                        print("That time is unavailable. Select another time.")
                    else:
                        # Book four 15 minute blocks and break while loop.
                        for booked in range(time_index, time_index + 4):
                            day.times[booked] = "BOOKED"
                        break
            else:
                print("Invalid input. Input is outside menu scope.")
        else:
            print("Invalid input. Input must be a positive integer.")
    return (time, time_index)


def generate_dates():
    """The generate_dates function returns a list of day objects. In later
    builds this function may take user input to generate specific weeks or
    months.
    """
    available_dates = []
    # For loop generates days 21-25
    for i in range(21, 26):
        # All generated dates will be in January 2019
        available_dates.append(date.Date(1, i, 2019))
    return available_dates
