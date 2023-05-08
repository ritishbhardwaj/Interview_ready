from sys import *
def kadane(arr):
    summ=0
    maxi=-maxsize

    for i in range(len(arr)):
        summ+=arr[i]

        if summ>maxi:
            maxi=summ
        
        if summ<0:
            summ=0

    return maxi