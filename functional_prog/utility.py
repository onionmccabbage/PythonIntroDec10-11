# some utility functions
def findAverage(t):
    '''find the average of all the values provided in 't' (a tuple)'''
    num_values = len(t)
    total = 0
    for i in t:
        total += i
    return total/num_values

temps = range(-10, 36) # imagine a range of temperatures
# suppose acceptable temperatures are 12-28
def ok(t):
    if t>=12 and t<=35:
        return t
    

# there is a potential problem to using import
# When a module is imported, Python will assign __name__ to the name of the module
if __name__ == '__main__':
    print('Nearly lunch time')
    # only run the folowing lines if this module has been executed direclty (not via import)
    print(f'This module is called {__name__}')