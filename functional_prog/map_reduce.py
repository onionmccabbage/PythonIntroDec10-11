import utility

# using 'map' 
data = [(4,5,6),(-7,-3,-99,-2),(0,0,0,0),(3246,7644,2344,7647,5673,1236,7565)]
# find the average for each tuple in the list of data
def useMap(d):
    # map will repeatedly aply a function to a data structure
    result = map(utility.findAverage, data) # pass a function into a function (higher order function)
    return result

# using 'filter' to apply a function that filters out only matching values

    
def useTempFilter():
    fine = filter(utility.ok, utility.temps)
    return fine

# exercise the code
if __name__ == '__main__':
    # When a module is run directly, Python assigns __name__ to '__main__'
    print(f'This module is called {__name__}')
    print( utility.findAverage( (1,2,3,4,5) ) ) # 3 (15/5)
    r = useMap(data)
    print( r ) # we have a 'map' object
    # we may iterate over the map objke t  to see the actual results
    for i in r:
        print(i)
    a = useTempFilter() # we now have a 'filter' object
    for i in a: # we iterate over all teh items in the filter object
        print( i ) # 12, 13,...35