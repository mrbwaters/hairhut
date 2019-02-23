class Appointments(object):
    """This class represents all of the appointments currently scheduled.
    It stores them in a list. It sorts appointments chronologically by time
    of appointment, not by time of creation. It prints appointments.
    """


    def __init__(self):
        self.appointments = []

    def add_app(self, customer, service, day, time, time_index):
        """The add_app method takes a customer name, service, day of
        appointment, time of appointment, and time index. It appends them to
        the object's appointment list as a nested list.
        """
        self.appointments.append([customer, service, day, time, time_index])

    def print_apps(self):
        """The show_apps method uses the sort_apps method and app_to_text method
        to print all scheduled appointments in chronological order.
        """
        print("--LIST OF APPOINTMENTS--\n")
        # If no appointments scheduled, display explanation.
        if len(self.appointments) == 0:
            print("You have no appointments scheduled.")
        else:
            # Sorts appointments to chronological order before printing
            self.sort_apps()
            # For loops prints each appointment in object list.
            for i in range(len(self.appointments)):
                print(self.app_to_text(i))

    def app_to_text(self, i):
        """The app_to_text method converts takes an index i and converts the
        appointment in the object list at that index to a string in English.
        It then returns that string.
        """
        customer = self.appointments[i][0]
        service = self.appointments[i][1]
        day = self.appointments[i][2].date_text
        time = self.appointments[i][3]
        return ("%s for %s on %s at %s" %(customer, service, day, time))

    def sort_apps(self):
        """The sort_apps method sorts all scheduled appointments into
        chronological order of the appointment. It uses a series of function
        keys in sequence to accomplish this sorting.
        """
        def by_time(element):
            # The time index of the appointment.
            return element[4]
        def by_day(element):
            return element[2].day
        def by_month(element):
            return element[2].month
        def by_year(element):
            return element[2].year
        self.appointments.sort(key=by_time)
        self.appointments.sort(key=by_day)
        self.appointments.sort(key=by_month)
        self.appointments.sort(key=by_year)
