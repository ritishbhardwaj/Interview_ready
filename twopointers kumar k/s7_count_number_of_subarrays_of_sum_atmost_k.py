


def sol(arr:list,k):
    n=len(arr)
    i=j=0
    s=0
    ans=0
    # arr.append(k+10000)
    while j<n:
        s+=arr[j]

        if s<k:
            ans+=(j-i+1)
            j+=1
        
        else :
            while i<=j and i<n and s>=k:
                s-=arr[i]
                i+=1

            ans+=(j)-i+1
            j+=1


        # s+=arr[j]
        # while s>=k and i<=j and i<n:
        #     s-=arr[i]
        #     i+=1
        # ans+=(j-i+1)
        # j+=1
    print(ans)


queries=[
    ([2,5,6],11),
    ([1, 11, 2, 3, 15],15)
]

for arr,k in queries:
    sol(arr,k)
