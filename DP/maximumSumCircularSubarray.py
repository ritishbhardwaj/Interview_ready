def sol(arr):
    #case 1 of all negative vals
    flag_all_neg=True
    for i in range(len(arr)):
        if arr[i]!=(0-abs(arr[i])):
            flag_all_neg=False
            break
    if flag_all_neg== True:
        print(max(arr))
        return max(arr)
    for i in range(len(arr)):
        if arr[i]==0-abs(arr[i]):
            subarr=arr[i-1:-1]+arr[len(arr)-1:i:-1]
            print(subarr)
            main_one(subarr)
    
def main_one(sarr):pas   # sarr is passed subarray

arr=[1,6,-4,-5,-1,2,3,7,-1,-2]
# arr=[-1,-2,-3,-4,-5,-6]
sol(arr=arr)


