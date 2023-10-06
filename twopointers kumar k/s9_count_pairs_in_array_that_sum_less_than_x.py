

def sol(arr:list,k:int):
    
    #Brute Force
    cnt=0
    for i in range(len(arr)):

        for j in range(i+1,len(arr)):
            s= arr[i]+arr[j]
            if arr[i]+arr[j]<k:
                cnt+=1
            else:
                break
    print(cnt)


    n=len(arr)
    cnt=0
    i=0
    j=n-1
    
    while i<j:
        s=arr[i]+arr[j]
        if arr[i]+arr[j]>=k:
            j-=1

        else:
            cnt+=(j-i)
            i+=1
    
    print(cnt)




queries=[
    ([1, 3, 7, 8, 10, 11],10),
    ([1, 2, 3, 4, 5, 6, 7, 8],7),
]

for arr , x in queries:
    sol(arr,x)