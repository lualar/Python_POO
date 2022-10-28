from datetime import datetime
import time

def simple_decorator(own_function):
    def internal_wrapper(*args, **kwargs):
        print('\n"{}" was called: '.format(own_function.__name__))
        # get current time using now() method
        timestamp = datetime.now()
        # convert timestamp to human-readable string, following passed pattern:
        string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        print(string_timestamp)
        own_function(*args, **kwargs)
        timestamp = datetime.now()
        # convert timestamp to human-readable string, following passed pattern:
        string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        print(string_timestamp)
                        
    return internal_wrapper

@simple_decorator
def Suma(*args, **kwargs):
    time.sleep(2)
    print (sum(args))

@simple_decorator
def Multiplicacion(*args, **kwargs):
    time.sleep(4)
    iTotal = 1
    for i in args:
        iTotal *= i
    print (iTotal)

Suma(1,2,3,4,5)
Multiplicacion(1,2,3,4,5)