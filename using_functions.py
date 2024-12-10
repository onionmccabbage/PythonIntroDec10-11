# functions let us encapsulate code so we can reuse it whenever we need
# if we wish me may pass in arguments to a function (optionally include a sensible default)
def makeCubic(x=1): # we define a function in a code block
    # a good idea to check we are dealing with a number
    if(type(x)==int or type(x)==float):
        return x*x*x # the function will stop when it runs 'return' (or if there are no more lines)
    else:
        return f'{x} is not a number (it is a {type(x)})'

# we then use the function like this
answer = makeCubic(4.2) # the () invoke the function so it runs
print(answer)
# we can print the result of a function ccall directly
print( makeCubic(4) )
print( makeCubic(-6) )
print( makeCubic(31452) )
print( makeCubic(0) )
print( makeCubic('wibbly') ) # fails nicely