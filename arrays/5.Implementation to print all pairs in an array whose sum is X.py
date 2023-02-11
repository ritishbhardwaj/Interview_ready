# def print_pair(arr,size, target):
#     MAX=max(arr)
#     hashmap_positive=[0]*MAX
#     hashmap_negative=[0]*(MAX)
#     for i in range(len(arr)):
#         temp=target-arr[i]
#         if (temp>=0 and hashmap_positive[temp]==1):
#             return arr.index(temp),i
#             # print(f"pair is {temp, arr[i]}")
#         if arr[i]>=0:
#             hashmap_positive[arr[i]]=1
#         if (temp<0 and hashmap_negative[temp]==1):
#             # return arr.index(temp),arr.index(arr[i])
#             print(f"pair is {temp, arr[i]}")
#         if arr[i]<0:
#             hashmap_negative[arr[i]]=1
#
#
# arr=[50000000,3,2,4,50000000]
# target=100000000
# print(print_pair(arr,len(arr),target))


def twoSum(arr,target):
    ans=[]
    for i in range(len(arr)):
        temp=target-arr[i]
        for j in range(i+1,len(arr)):
            if arr[j]==temp:
                ans.append([i,j])
    return ans


arr= [2,7,11,15,8,1]
target=9
print(twoSum(arr,target))