

def getoccurance(arr):
    result=0
    for i in range(len(arr)):
        result=result^arr[i]
    return result

arr=[1,1,1,2,2,3,3,4,4]
print(getoccurance(arr))