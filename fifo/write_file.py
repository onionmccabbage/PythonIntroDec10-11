# There are two easy ways to write to a text file
def printToFile():
    '''use 'print' to send text into a persistent file'''
    # we need a file access object. 'at' will append text
    fout = open('my_log.txt', 'at') # this asks the operating system to access the file system
    print('hello from Python', file=fout)

def writeToFile():
    '''more control over that gets written into a persistent text file'''

# here we exercise the code
printToFile() # this will create the file if it does not yet exist, otherwise append to it