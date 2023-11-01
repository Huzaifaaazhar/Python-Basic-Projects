#Program that displays current time and date in different formats.

import time #import time module
from time import gmtime,strftime

t = time.localtime()
print(time.asctime())
print(strftime("%a, %d, %b, %y, %H:%M:%S +0000", gmtime()))
print(strftime("%A", gmtime()))
print(strftime("%D", gmtime()))
print(strftime("%B", gmtime()))
print(strftime("%Y", gmtime()))

#converts second into GMT date
print(strftime("%a, %d, %b, %y, %H:%M:%S +0000", gmtime(1234567890)))
