class Date:
    def __init__(self, day = 0, month = 0, year = 0):
        self.day = day
        self.month = month
        self.year = year
    
    @classmethod
    def date_str(cls, string):
        day, month, year = map(int, string.split("-"))
        date1 = cls(day, month, year)
        return date1
    
    @staticmethod
    def date_meta(string):
        day, month, year = map(int, string.split("-"))
        return day <= 31 and month <= 12 and year <= 2023
    
date2 = Date.date_str("23-7-2000")
is_date = Date.date_meta("12-11-1990")

print(date2.__dict__)
print(is_date)