from os import *
from sys import *
from collections import *
from math import *

def isValidIPv4(ipAddress):
    # Write your code here.
    l=ipAddress.split('.')
#     print(l)
    if len(l)!=4:
        return False
    if len(l)==4:
        for i in range(len(l)):
            if l[i].isnumeric():
                if int(l[i])>255 and int(l[i])<0:
                    return False
            if not l[i].isnumeric():
                return False
        return True
                
s='122.0.330.0'
print(isValidIPv4(s))