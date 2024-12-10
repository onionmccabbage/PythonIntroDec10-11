# naming things: letters, numbers, underscore
# keep asking the user to enter something until they enter a numeric value
g = '' # an empty string
while True: # True and False are 'boolean' data values
    # single equals SETS a value. Double equals CHECKS a value
    g = input('Please enter a number: ')
    # check: did they enter a number
    if g.isnumeric(): # remember every 'input' is always a string
        print(f'Thank you for entering the number {g}')
        # we may need to convert a string into a number
        n = int(g) # here we convert the string into a number
        print(f'The number {n} squared is {n*n}')
        # using comparison operators
        # is n an odd number?
        if n/2 == int(n/2): # it must be an even number
            print(f'{n} is an even number')
        elif n<10 or n>0:
            print(f'{n} is between 0 and 10')
        elif n>=10:
            print(f'{n} is greater than ten')
        break # this breaks out of the while loop

