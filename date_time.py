import time
import datetime

if __name__ == '__main__': # only run the following code if its is the main module (not if its imported)
    t = time.time()
    # we now have the time as a number representing the seconds since 1 Jan 1970
    print( f'the numeric time is {t:0.2f}' ) # format a float to 2 dp
    # datetime is much more friendly tool for dates and times
    ds = datetime.datetime.now()
    print(ds)
    pretty_date = ds.strftime('%d/%m/%Y %H:%M:%S')
    print(pretty_date)