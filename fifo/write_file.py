# There are two easy ways to write to a text file
def printToFile():
    '''use 'print' to send text into a persistent file'''
    # we need a file access object. 'at' will append text
    # if we use 'xt' it will only print to file if it does NOT already exist
    try: # try lets us write an exception handler in case of problems
        fout = open('my_log.txt', 'at') # this asks the operating system to access the file system
        # NB print always puts a new-line character at the end
        print('hello from Python', file=fout)
        # its a good idea to close a file access object to release resources
        fout.close()
    except FileExistsError as err:
        print(f'There was a problem: {err}')

def writeToFile():
    '''more control over what gets written into a persistent text file'''
    try:
        fout = open('file.txt', 'at')
        # 'with' will close the file access object for us ( no need for fout.close() )
        with fout: # this is a tidy way to handle file access
            # .write does NOT put a new line character at the end
            fout.write('this is persisted into a text file\n') # we may choose to add a new line character
            # also \t for tab
    except Exception as err: # here we handle ANY exception
        print(f'Problem: {err}')

# here we exercise the code
printToFile() # this will create the file if it does not yet exist, otherwise append to it
writeToFile()