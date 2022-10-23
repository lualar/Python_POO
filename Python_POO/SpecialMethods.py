class TimeInterval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        ##convert to seconds
        seconds1 = self.__Convert2Seconds(self)
        seconds2 = self.__Convert2Seconds(other)
        return self.__Convert2Time(seconds1 + seconds2)

    def __sub__(self, other):
        ##convert to seconds
        seconds1 = self.__Convert2Seconds(self)
        seconds2 = self.__Convert2Seconds(other)
        return self.__Convert2Time(seconds1 - seconds2)

    def __mul__(self, value):
        #convert to seconds
        seconds1 = self.__Convert2Seconds(self)
        return self.__Convert2Time(seconds1 * value)

    def __Convert2Seconds(self, value):
        return (value.hours * 3600 + value.minutes * 60 + value.seconds)

    def __Convert2Time(self, value):
        iHours = value // 3600
        iMinutes = (value-iHours*3600)//60
        iSeconds = value - iHours*3600 - iMinutes*60
        ##print (iHours, iMinutes, iSeconds)
        return (str(iHours) + ":" + str(iMinutes) + ":" + str(iSeconds))

    def __str__(self):
        sHour = "{00}".format(self.hours)
        return (sHour + ":" + str(self.minutes) + ":" + str(self.seconds))

##Exercise 1##
timeI1 = TimeInterval(21, 58, 50)
timeI2 = TimeInterval(1, 45, 22)
##print (timeI1)
##print (timeI2)
print (timeI1 + timeI2)
print (timeI1 - timeI2)
print (timeI1 *2)

##Exercise 2##
timeI1 = TimeInterval(21, 58, 50)
timeI2 = TimeInterval(0, 0, 62)
print (timeI1 + timeI2)
print (timeI1 - timeI2)


