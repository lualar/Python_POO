import abc

class ScannerDevice(abc.ABC):
    __resolution  = 0
    __Count = 0

    def __init__(self, resolution):
        self.__resolution = resolution
        self.__SN = 'Scanner' + str(resolution) + str(ScannerDevice.__Count)
        ScannerDevice.__Count += 1
    
    @abc.abstractmethod
    def scan_Document(self):
        return 'Document has been scanned!'

    @abc.abstractmethod
    def Get_ScannerStatus(self):
        return "SN: " + self.__SN + " - Resolution: " + str(self.__resolution)

class PrinterDevice(abc.ABC):
    __resolution  = 0
    __Count = 0

    def __init__(self, resolution):
        self.__resolution = resolution
        self.__SN = 'Printer' + str(resolution) + str(PrinterDevice.__Count)
        PrinterDevice.__Count += 1

    @abc.abstractmethod
    def print_Document(self):
        return 'Document has been printed!'

    @abc.abstractmethod
    def get_printerStatus(self):
        return  "SN: " + self.__SN + " - Resolution: " + str(self.__resolution)


class MFD1(ScannerDevice, PrinterDevice):
    def __init__(self, resolution):
        ScannerDevice.__init__(self, resolution)
        PrinterDevice.__init__(self, resolution)

    def Get_DeviceStatus(self):
        return self.Get_ScannerStatus() + " " + self.get_printerStatus()

    def print_Document(self):
        return PrinterDevice.print_Document(self)

    def scan_Document(self):
        return ScannerDevice.scan_Document(self)

    def get_printerStatus(self):
        return PrinterDevice.get_printerStatus(self)

    def Get_ScannerStatus(self):
        return ScannerDevice.Get_ScannerStatus(self) 

##class MFD2(ScannerDevice, PrinterDevice):

##class MFD3(ScannerDevice, PrinterDevice):

cheapDevice = MFD1(320)
print (cheapDevice.Get_DeviceStatus())
print (cheapDevice.print_Document())

                                