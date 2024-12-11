# some utility functions
def findAverage(t):
    '''find the average of all the values provided in 't' (a tuple)'''
    num_values = len(t)
    total = 0
    for i in t:
        total += i
    return total/num_values

# using 'map' 
data = [(4,5,6),(-7,-3,-99,-2),(0,0,0,0),(3246,7644,2344,7647,5673,1236,7565)]
# find the average for each tuple in the list of data
def useMap(d):
    # map will repeatedly aply a function to a data structure
    result = map(findAverage, data) # pass a function into a function (higher order function)
    return result

# using 'filter'

# exercise the code
print( findAverage( (1,2,3,4,5) ) ) # 3 (15/5)
r = useMap(data)
print( r ) # we have a 'map' object
# we may iterate over the map objke t  to see the actual results
for i in r:
    print(i)