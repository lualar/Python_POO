class WeekDayError(Exception):
    pass

class Weeker:
    #
    # Write code here.
    # Mon Tue Wed Thu Fri Sat Sun
    # 0..6
    
    __WeekSet={'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun'}
    __dayOfTheWeek = 0
    __d={1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat', 7: 'Sun'}


    def __init__(self, day):
        if (day in self.__WeekSet):
            iIndex = list(self.__d.values()).index(day)
            self.__dayOfTheWeek = iIndex 
        else:
            raise WeekDayError()

    def __str__(self):
        return (list(self.__d.values())[self.__dayOfTheWeek])

    def add_days(self, n):
        self.__dayOfTheWeek += (n % 7)
        if (self.__dayOfTheWeek > 7):
            self.__dayOfTheWeek = 0 + self.__dayOfTheWeek


    def subtract_days(self, n):
        self.__dayOfTheWeek -= (n % 7)
        if (self.__dayOfTheWeek < 1):
            self.__dayOfTheWeek = 7 + self.__dayOfTheWeek

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
