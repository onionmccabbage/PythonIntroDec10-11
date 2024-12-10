# this is a comment - a place to explain whats going on
# All computer languages use variables - names for data
a = 3   # integer
b = 7.5 # floating point
s = "welcome to Python" # string data-type (single or double quotes)

# at any time we may ask Python to print stuff
print(a, b)
print(s)
# Python has several 'collections' for data. String, Tuple and List
# a tuple is an immutable ordinal collection of any data type
t = (4,5,6,7,8,3,9,2) # a tuple of numbers (or any other data type)
# a list is a mutalbe ordinal collection of any data type
l = [3,9,44,-2,0,3,13523] # a list of numbers (or any other data type)
l.append('extra') # the list is mutalbe - we can alter it
l.remove(3) # removes only the FIRST occurence of the item
print(l)

# Python code structore: code blocks
# we may need to iterate (loop) over the members of a collection (string, tuple, list)
for i in l: # the colon : indicates the begining of a code block
    print(i) # this line is indented to indicate to belongs to the current code block

# when the code is no longer indented, that indicates the end of the code block
for i in t:
    print(i)
    print(type(i)) # we can find what type of data it is

# we may ask for user input (always a string)
n = input('Please enter a value ') # pause until there is some input
print(n, type(n)) # input is ALWAYS a string of data
# we may carry out conditional logic
if n.isnumeric(): # checks that ONLY digits exist in the value (no . no , just digits)
    # we may choose to format a string
    print(f'The number {n} was entered') # we may inject values into a string
else:
    print(f'{n} is not a number')