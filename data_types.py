# There are many data types in Python
# Simple dtaa types include int, float, boolean, None
# collection data types include string, tuple, list
# Also dict and set
# a dictionary is a NON ORDINAL mutable collection of key:value pairs (of any data type)
d = {'name':'Ethel', 'age':42, 'status':'admin', 'auth':True}
# we may add new member to the dict
d['q_test'] = 3.8
print(d, type(d))
# we may iterate a dict
for k,v in d.items():
    print(k, v)
# there is also a 'set' data type in Python: a non ordinal collection of unique members
s = {0,4,5,5,5,5,6,4,72,'anything', False} # they will be stored as unique members
# NB False and Zero evaluate to the same thing
# Also 1 and True will evaluate to the same thing
print(s, type(s))

# the 'range' object
# instead of storing loads of values in memory using a range
n = range(0,11) # (start, stop-before)
for i in n: # iterate over the range
    print(i)

# the 'range' is a really-efficient tool for large quantities of values
# e.g. we may need a bunch of even numbers
e = range(-10, 11, 2) #(start, stop-before, step)
g =input('please enter a number: ') # input is always a string
if g.isnumeric():
    # did they enter an even number?
    if int(g) in e:
        print(f'{g} is an even number between -10 and 10')

# we ca nuse a range to create a load of calculations
# we may need some square numbers 1-10
squares = [i*i for i in range(1,11)] # remember [] will make a list
print(squares)
    