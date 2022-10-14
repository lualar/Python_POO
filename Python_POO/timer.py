class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        sHour = "{00}".format(self.hours)
        return (sHour + ":" + str(self.minutes) + ":" + str(self.seconds))

    def __IncHours(self):
        if (self.hours == 23):
            self.hours = 00
        else:
            self.hours +=1

    def __DecHours(self):
        if (self.hours == 00):
            self.hours = 23
        else:
            self.hours -=1


    def next_second(self):
        if (self.seconds == 59):
            if (self.minutes == 59):
                self.__IncHours()                
                self.minutes = 0
            else:
                self.minutes += 1 
            self.seconds = 0
        else:
            self.seconds +=1

    def prev_second(self):
        if (self.seconds == 00):
            if (self.minutes == 00):
                self.__DecHours()
                self.minutes = 59
            else:
                self.minutes -= 1 
            self.seconds = 59
        else:
            self.seconds -=1



timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

