# why would we use a class?
age = 42 # we can just use numbers
username= 'student' # we may need to use strings
isAuthorised = True # handy boolean value
# we sometime gather data together in a collection
details = (37, 'Ethel', False) # related data (tuple)
n =[age, username, isAuthorised] # more related data, in a list
n[0] = 'altered' # no longer a number
# the problem is there is no mechanism to ensure the data is the type we wanted
# print(n)

# Use the built-in structures until they no longer suit your purpose
# e.g. when we must ensure data-types are exactly as planned

class User():
    '''This class will encapsulate details of a user
    Name will be a non-empty string
    Age will be a positive number (float or int)
    Authorization will be a boolean'''
    def __init__(self, n, a, auth): # the initializer is run every time we use the class
        self.name = n
        self.age = a
        self.authorization = auth
    def __str__(self):
        '''Whenever we use 'print' it will call this function'''
        return f'{self.name} age {self.age} authentication:{self.authorization}'

# NB in Python, anything with __nnn__ is a built-in feature of Python. Often called 'dunder'

# make use of the class
userA = User('Petra', 24, False) # here we create an instance of our class (calls the __init__ function)
userB = User('Zara', 67, True)
print(userA, userB)


