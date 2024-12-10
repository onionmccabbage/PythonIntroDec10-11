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

# fileWriter(h)
# fileWriter(j)
# fileWriter(k)

# read back all the text into a list of lines
def readCSV():
    '''retrieve all the contents of a CSV text file
    into a list where each member is a line'''
    try:
        fin = open('names.csv', 'rt')
        with fin:
            r = fin.readlines() # retreive a list of all the lines
        return r
    except Exception as err:
        print(err)

c = readCSV()
print(c) # expect a list of lines

# iterate over this retrieved text to populate a list of dictionaries
def makeListOfDict(l):
    '''iterate over the list, making a dict object for each user
    Append each new suer to a list'''
    users = [] # an empty list
    for i in l: # iterate of the the list 'l' 
        user = i.split(', ')
        d = {'name':user[0], 'age':user[1], 'level':user[2], 'skill':user[3]}
        users.append(d) # we have a list of dictionaries
    return users

r = makeListOfDict(c)
print(r)
