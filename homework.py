from datetime import datetime


class SuperDate(datetime):

    def __init__(self, year, month, day, time):
        self.year_ = year
        self.month_ = month
        self.day_ = day
        self.time_ = time

    def get_season(self):
        winter = {12, 1, 2}
        summer = {6, 7, 8}
        autumn = {9, 10, 11}
        spring = {3, 4, 5}
        if self.month in winter:
            return 'Winter'
        elif self.month in summer:
            return 'Summer'
        elif self.month in autumn:
            return 'Autumn'
        else:
            return 'Spring'

    def get_time_of_day(self):
        if self.time_ in range(7):
            return 'Night'
        if self.time_ in range(6, 13):
            return 'Morning'
        if self.time_ in range(12, 19):
            return 'Day'
        if self.time_ in range(18, 24):
            return 'Evening'


a = SuperDate(2024, 1, 22, 22)
print(a.get_season())
print(a.get_time_of_day())
