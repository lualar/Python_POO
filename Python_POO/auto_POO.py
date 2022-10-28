class AutoError(Exception):
    pass

class Automovil:
    def __init__(self, VIN):
        self.__VIN = VIN

class Vehicle(Automovil):
    def __init__(self, VIN, tires, engine):
        super().__init__(VIN)
        self.tires = tires
        self.engine = engine

class tires:
    def __init__(self, size):
        self.__size = size
        self.__Pressure = 100

    def TiresSize(self):
        print ("Tires Size are: {}".format(self.__size))

    def GetPlessure (self):
        print ("Tires pressure are: {}".format(self.__Pressure))

    def Pump(self):
        self.__Pressure = 100

class CityTires (tires):
    def __init__(self):
        super().__init__(15)

    def TiresSize(self):
        super().TiresSize()

    def GetPlessure (self):
        super().GetPlessure()

class RoadTires (tires):
    def __init__(self):
        super().__init__(18)

    def TiresSize(self):
        super().TiresSize()

    def GetPlessure (self):
        super().GetPlessure()

class engine:
    def __init__(self, type):
        self.__type = type
        self.__Status = "Stopped"

    def EngineType(self):
        print ("Engine Type is: {}".format(self.__type))

    def Start(self):
        self.__Status = "Started"

    def Stop(self):
        self.__Status = "Stopped"

    def EngineStatus(self):
        print ("Engine status: {}".format(self.__Status))

class gas(engine):
    def __init__(self):
        super().__init__("Gas")

    def EngineType(self):
        super().EngineType()

    def EngineStatus(self):
        super().EngineStatus()

    def Start(self):
        super().Start()

    def Stop(self):
        super().Stop()

class electrical(engine):
    def __init__(self):
        super().__init__("Electrical")

    def EngineType(self):
        super().EngineType()

    def EngineStatus(self):
        super().EngineStatus()

    def Start(self):
        super().Start()

    def Stop(self):
        super().Stop()


sVIN = "A1B2C3"
myCityCar = Vehicle(sVIN, CityTires(), electrical())
myCityCar.engine.Start()

sVIN = "D4E5F6"
myRoadCar = Vehicle(sVIN, RoadTires(), gas())
myRoadCar.engine.Stop()

print ("\n City Car: \n")
print (myCityCar._Automovil__VIN)
myCityCar.engine.EngineType()
myCityCar.tires.TiresSize()
myCityCar.engine.EngineStatus()

print ("\n Road Car: \n")
print (myRoadCar._Automovil__VIN)
myRoadCar.engine.EngineType()
myRoadCar.tires.GetPlessure()
myRoadCar.engine.EngineStatus()

