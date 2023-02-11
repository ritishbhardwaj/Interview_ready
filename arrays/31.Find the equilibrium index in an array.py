
def solution(arr):
    l_sum=0
    r_sum=sum(arr)
    for i in range(len(arr)):
        r_sum-=arr[i]
        if l_sum==r_sum:
            print("equilibrium index is:",i)
        l_sum+=arr[i]


# arr=[10,5,15,3,4,21,2]
# arr=[7,2,1,4,6,4,0]
# arr=[1,2,3]
arr=[2,1,-1]
solution(arr)