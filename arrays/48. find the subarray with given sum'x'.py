from queue import Queue
from queue import  PriorityQueue as pq


'''Approach 1'''
def subarr_sum1(arr:[int],x:int) -> [int]:
    l,r=0,0
    while l<=r:
        Sum=sum(arr[l:r])
        if Sum==x:
            return arr[l:r]
        elif Sum > x:
            l+=1
        else:
            r+=1

'''Approach 2'''
def subarr_sum2(arr2,target):
    nums=arr2
    k=target
    ans = 0
    prefsum = 0
    d = {0: 1}

    for num in nums:
        prefsum = prefsum + num

        if prefsum - k in d:
            ans = ans + d[prefsum - k]

        if prefsum not in d:
            d[prefsum] = 1
        else:
            d[prefsum] = d[prefsum] + 1

    return ans

        # if Sum in hashmap:
        #     hashmap[Sum]+=1
        # else:
        #     hashmap[Sum]=1







arr1=[50,40,6,7,9,8,3,1,2]
x=21
# ans=subarr_sum1(arr1,x)
# print(ans)
print()
arr2=[1,-1,0,0]
target=0
ans=subarr_sum2(arr2,target)
print(ans)