import calendar


class Calender(calendar.Calendar):
    def __init__(self, year, month):
        super().__init__(firstweekday=6)
        self.year = year
        self.month = month
        self.day_names = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
        self.months = (
            "January",
            "Feburary",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        )

    def get_month(self):
        return self.month[self.month - 1]

    def get_days(self):
        days = self.monthdays2calendar(self.year, self.month)
