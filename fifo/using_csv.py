# CSV is comma-separated variables
h = 'Floela, 42, admin, Python'
j = 'Jane, 32, user, SQL'
k = 'Ade, 84, guest, Java'

# work with strings of text
h_s = h.split(', ') # use the characters in quotes to split the text into a list
print(h_s)

# first write all the csv into a multi-line text file
def fileWriter(t):
    '''Validate that 't' is indeed a string of text
    If so, write it to a persistent text file'''
    if type(t)==str:
        try:
            fout = open('names.csv', 'at')
            with fout:
                fout.write(f'{t}\n') # here we choose to append a new line character
        except Exception as err:
            print(f'{err}')

# read back all the text into a list of lines

# itersate over this retrieved text to populate a list of dictionaries