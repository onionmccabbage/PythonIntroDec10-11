import random # we may inport any part of the Python standard library

# functions let us encapsulate code so we can reuse it whenever we need
# if we wish me may pass in arguments to a function (optionally include a sensible default)
def makeCubic(x=1): # we define a function in a code block
    # a good idea to check we are dealing with a number
    if(type(x)==int or type(x)==float):
        # return x*x*x # the function will stop when it runs 'return' (or if there are no more lines)
        return x**3 # ** means raise to the power of
    else:
        return f'{x} is not a number (it is a {type(x)})'
    
# maybe we need to operate air-con based on temperature
def controlAC(temperature):
    if temperature<1: # too cold - turn on the heater
        return 'Heater On'
    elif temperature > 26: # too warm - turn on AC
        return 'AC On'
    else:
        return 'comfy'

# we then use the function like this
answer = makeCubic(4.2) # the () invoke the function so it runs
print(answer)
# we can print the result of a function ccall directly
print( makeCubic(4) )
print( makeCubic(-6) )
print( makeCubic(31452) )
print( makeCubic(0) )
print( makeCubic('wibbly') ) # fails nicely
# we may call a function repeatedly using an iterator like this
for t in range(-3, 31):
    print( controlAC(t) ) # we pass each value of t in to our function

# here we use a random integer
r = random.randint(-10,30)
print( controlAC(r), r )