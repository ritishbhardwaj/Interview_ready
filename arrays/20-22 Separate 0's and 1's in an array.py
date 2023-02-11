
def separation(arr):
    l=0
    r=len(arr)-1
    while l<r:

        while arr[l]==0 and l<r:
            l+=1
        while arr[r]==1 and l<r:
            r-=1
        if l<r:
            arr[l]=0
            arr[r]=1
            l+=1
            r-=1
    print(arr)

arr=[0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,1,0,1,1,0]
separation(arr)


# swap=arr[r]
# arr[r]=arr[l]
# arr[l]=swap