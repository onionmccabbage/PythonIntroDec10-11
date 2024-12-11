from functools import reduce
# NB map anmd filter are both built in to Python.
# reduce is in the Python standard library
# Reduce is used to repeatedly apply a function across a set of data
# in this case the result is a combination of ALL the results

# for example, we may need ot find the sum across a large quantity of numbers
def addThem(a, b):
    return a+b

def useReduce(values_tup):
    total = reduce( addThem, values_tup )
    return total

# exercise the code
v = tuple( [i for i in range(0,10000000)] ) # loads of numeric values
# print(v, type(v))
tot = useReduce(v)
print(f'The total is {tot}')