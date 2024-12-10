# we may read back from a text file via a file access object

def readText():
    '''Retrieve any text from a specific text file
    return the entire contents of the text file'''
    fin = open('file.txt', 'rt') # 'rt' means read text
    with fin: # ...this will close the file access object when done
        retrieved = fin.read()
    return retrieved

# exercise the code
r = readText()
print(r)