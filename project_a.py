# naming things: letters, numbers, underscore
# keep asking the user to enter something until they enter a numeric value
g = '' # an empty string
while True: # True and False are 'boolean' data values
    # single equals SETS a value. Double equals CHECKS a value
    g = input('Please enter a number: ')
    # check: did they enter a number
    if g.isnumeric(): # remembre every 'input' is always a string
        print(f'Thank you for entering the number {g}')
        # we may need to convert a string into a number
        n = int(g) # here we convert the string into a number
        print(f'The number {n} squared is {n*n}')
        break # this breaks out of the while loop
