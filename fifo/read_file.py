# we may read back from a text file via a file access object

def readText():
    '''Retrieve any text from a specific text file
    return the entire contents of the text file'''
    try: # always good to use try-except when dealing with external assets
        fin = open('file.txt', 'rt') # 'rt' means read text
        with fin: # ...this will close the file access object when done
            # retrieved = fin.read() # read() will retrieve the entire file contents
            retrieved = fin.readlines() # retrieves the entire file into a LIST of single lines
        return retrieved
    except Exception as err:
        print(f'Something went wrong: {err}')

# exercise the code
r = readText()
print(r)