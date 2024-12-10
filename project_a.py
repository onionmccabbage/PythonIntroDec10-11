# naming things: letters, numbers, underscore
# keep asking the user to enter something until they enter a numeric value
g = '' # an empty string
while True: # True and False are 'boolean' data values
    # single equals SETS a value. Double equals CHECKS a value
    g = input('Please enter a number: ')
    # check: did they enter a number
    if g.isnumeric():
        print(f'Thank you for entering the number {g}')
        break # this breeaks out of the while loop
