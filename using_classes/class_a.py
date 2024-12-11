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
    __slots__ = ['__name', '__age', '__authorization'] # restrict to only these properties
    def __init__(self, n, a, auth): # the initializer is run every time we use the class
        self.name = n # call the 'name' setter function
        self.age = a
        self.authorization = auth
    # In order to validate properties, we write proerty methods like this:
    @property # this is called a 'decorator'
    def name(self): # 'getter' method
        return self.__name
    @name.setter
    def name(self, new_name): # 'setter' method
        '''validate the incoming value is a non-empty string'''
        if type(new_name)==str and len(new_name)>0:
            self.__name = new_name
        else:
            raise TypeError('Name must be a non-empty string')
    @property
    def age(self):
        # this is called 'name mangling'. It makes it very hard ot directly acess the property
        return self.__age 
    @age.setter
    def age(self, new_age):
        '''validate the incoming age is a positive number'''
        if type(new_age) in (int, float) and new_age>=0:
            self.__age = new_age
        else:
            raise TypeError('Age must be a positive number')
    # Write getter and setter methods for the 'authorization' (must be a boolean)
    @property
    def authorization(self):
        return self.__authorization
    @authorization.setter
    def authorization(self, new_auth):
        if type(new_auth)==bool:
            self.__authorization = new_auth
        else:
            raise TypeError('Authorization must be True or False')
    def __str__(self):
        '''Whenever we use 'print' it will call this function'''
        return f'{self.name} age {self.age} authentication:{self.authorization}'


# NB in Python, anything with __nnn__ is a built-in feature of Python. Often called 'dunder'

# make use of the class
userA = User('Petra', 24, False) # here we create an instance of our class (calls the __init__ function)
userB = User('Zara', 67, True)
# userC = User('Orla', 4, None) # problem - name must be a string, age must be positive, auth must be boolean
print(userA, userB)


