import sys

#Defining the ExceptionError for Queue Class
class cQueueError(IndexError):
    def __init__(self):
        self.message = "No more items to get from Queue!\n"

#Defining the Queue Class
class cQueue:
    #Constructor
    def __init__(self):
        self.__queue_list = []
        self.__count = 0

    def put(self, val):
        self.__queue_list.append(val)
        self.__count += 1

    def get(self):
        try:
            if (self.__count == 0):
                raise cQueueError()
            else:
                val = self.__queue_list[0]
                del self.__queue_list[0]
                self.__count -= 1
                return val
        except Exception as e: 
            print (e.message)

    def get_Counter(self):
        return  self.__count

class SuperQueue(cQueue):
    def __init__(self):
        cQueue.__init__(self)
        self.__count = 0

    def put(self, val):
        cQueue.put(self, val)
        self.__count += 1

    def get(self):
        val = cQueue.get(self)
        self.__count -= 1
        return val
    
    def get_Counter(self):
        return  self.__count

    def isempty(self):
        if (self.__count == 0):
            return True
        else:
            return False

if __name__ == "__main__":
    #Instancing the objects
    print ("Python Queue Management Using POO/Classes")
    que = SuperQueue()
    que.put(1)
    que.put("dog")
    que.put(False)
    print(que.get_Counter())
    for i in range(4):
        if not que.isempty():
            print(que.get())
        else:
            print("Queue empty")
    
