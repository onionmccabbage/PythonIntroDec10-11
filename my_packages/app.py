# import the code from my other modules
from my_maths import addThem
from my_maths import subtractThem
# alternative syntax for import
import utility # import everything

# we can use the imported functions
print( addThem(3, 7) ) # 10
print( subtractThem(82, 64) ) # 18
x = 'oops'
# if we use 'import' we then do this:
print( utility.validate(x) ) # 1
print( utility.validate(42) ) # 42