class MobilePhone():
    def __init__(self, MobileNumber):
        self.__number = MobileNumber

    def turnOn(self):
        return self.__number

    def turnOff(self):
        return (f"mobile phone {self.__number} is turned off")

    def call(self, number):
        return (f"caling {number}")

phone1 = MobilePhone(3005193192)
phone2 = MobilePhone(3043851902)

print ("mobile phone %1 is turned on", phone1.turnOn())
print ("mobile phone %1 is turned on", phone2.turnOn())
print (phone1.call(305179624))
print (phone1.turnOff())
print (phone2.turnOff())
