#Defining the Stack Class
class cStack:
    #Constructor
    def __init__(self, *args, **kwargs):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        #try:
            #if not self.__stack_list:
                val = self.__stack_list[-1]
                del self.__stack_list[-1]
                return val
        #except: 
        #    raise Exception("Stack contains no values!") 

#Defining a 2nd Class to handling the stack Class
class cAddingStack(cStack):
    def __init__(self):
        cStack.__init__(self)
        self.__sum = 0
        self.__count = 0

    def push(self, val):
        self.__sum += val
        self.__count += 1
        cStack.push(self, val)

    def pop(self):
        val = cStack.pop(self)
        self.__sum -= val
        self.__count -= 1
        return val

    def get_Sum(self):
        return  self.__sum
    
    def get_Counter(self):
        return  self.__count

if __name__ == "__main__":
    #Instancing the objects
    stack_object_1 = cAddingStack()
    
    for i in range(100):
        stack_object_1.push(i)
    print("Value Stack 1 after Push 1..5: ", stack_object_1.get_Sum())
    print()

    while stack_object_1.get_Counter() > 0:
        print (stack_object_1.pop())
    print("Value Stack 1 After Pop-For: ", stack_object_1.get_Sum())
    
