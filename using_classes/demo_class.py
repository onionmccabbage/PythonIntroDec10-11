# a class may as simple as this
class Useless:
    pass

# all classes inherit from 'object'
class MyObj():
    '''this is an object'''

class OtherObj(object):
    '''we may inherit from any other class'''

class MyList(list):
    '''we now have a list class'''

class MyException(Exception):
    '''we can make our own Exception classes'''