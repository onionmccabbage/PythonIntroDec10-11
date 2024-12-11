from threading import Thread # we need ther 'Thread' class
import time
import random

def someFunction(n):
    '''This is a normal function - we will call it in threads'''
    for i in range(1,11): # ten items
        print(f'{n} is sleeping')
        time.sleep( random.random()*0.1 ) # emulate a long running bit of code

if __name__ == '__main__':
    t1 = Thread(target=someFunction, args=('A',)) # this is a one-member tuple
    t1.start()