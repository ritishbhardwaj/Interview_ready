
def Find_Triplet(arr,target):
    new_arr=sorted(arr)
    for i in range(len(arr)):
        l=i+1
        r=len(arr)-1
        while l<r:
            sum=new_arr[i]+new_arr[l]+new_arr[r]
            if sum==target:
                print(new_arr[i],new_arr[l],new_arr[r])
                return
            elif sum< target:
                l+=1
            else:
                r-=1
    print("sorry")

arr=[8,3,0,5,7,4]
target=14
Find_Triplet(arr,target)