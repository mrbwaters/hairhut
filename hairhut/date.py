class Date(object):
    """This class represents the dates that you can schedule appointments.
    It stores day, month, and year values as integers. It stores a string
    of the date in text according to US convention. It stores a list of
    available times for appointments from 9am to 5pm.
    """


    def __init__(self, month, day, year):
        self.day = day
        self.month = month
        self.year = year
        self.date_text = self.make_text()
        # Available times are from 9:00am to 5:00pm in 15 minute blocks
        # Final elements are "BOOKED" to prevent scheduling a 60 minute
        # appointment after 4:00pm or 30 minute appointment after 4:30pm.
        # These "BOOKED" blocks are not visible in UI
        self.times = ["9:00am", "9:15am", "9:30am", "9:45am", "10:00am",
                      "10:15am", "10:30am", "10:45am",  "11:00am", "11:15am",
                      "11:30am", "11:45am", "12:00pm", "12:15pm", "12:30pm",
                      "12:45pm", "1:00pm", "1:15pm", "1:30pm", "1:45pm",
                      "2:00pm", "2:15pm", "2:30pm", "2:45pm", "3:00pm",
                      "3:15pm", "3:30pm", "3:45pm",  "4:00pm", "4:15pm",
                      "4:30pm", "4:45pm", "BOOKED", "BOOKED"]

    def make_text(self):
        """The make_text method converts numeric months into text and returns
        a string of the date formatted according to US convention.
        """
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November",
                  "December"]
        if self.month in range(1, 13):
            month_text = months[self.month - 1]
        else:
            month_text = "Invalid input for month"
        return "%s %s, %s" %(month_text, self.day, self.year)
