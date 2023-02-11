'''problem statement: Implementation of maximum difference bw two elements in an array such that larger element has higher index than smaller element'''


'''here we'll use the concept of maximum subarray'''

'''(Approach 1)'''

# def max_diff_sum(arr):
#     diff_arr=[]
#     for i in range(len(arr)-1):
#         diff_arr.append(arr[i+1]-arr[i])
#     current=diff_arr[0]
#     for i in range(1,len(diff_arr)):
#         if diff_arr[i-1]>0:
#             diff_arr[i]+=diff_arr[i-1]
#         current=max(current,diff_arr[i])
#
#     return current
#
# arr=[3,1,4,7,5,100,10]
# print(max_diff_sum(arr))


'''(Approach 2)'''

def max_diff_sum(arr):
    min_element_so_far=arr[0]
    max_diff_so_far=-1
    # curr_diff=arr[1]-arr[0]
    a=len(arr)

    for i in range(1,len(arr)):
        if ((arr[i] - min_element_so_far) > max_diff_so_far) and  (arr[i] - min_element_so_far)>0:
            max_diff_so_far = arr[i] - min_element_so_far
        if arr[i]<min_element_so_far:
            min_element_so_far=arr[i]

        # else:
        #     curr_diff=arr[i]-min_element_so_far
        #     if arr[i]-min_element_so_far>max_diff_so_far:
        #         max_diff_so_far=arr[i]-min_element_so_far
    print(max_diff_so_far)


arr=[999,997,980,976,948,940,938,928,924,917,907,907,881,878,864,862,859,857,848,840,824,824,824,805,802,798,788,777,775,766,755,748,735,732,727,705,700,697,693,679,676,644,634,624,599,596,588,583,562,558,553,539,537,536,509,491,485,483,454,449,438,425,403,368,345,327,287,285,270,263,255,248,235,234,224,221,201,189,187,183,179,168,155,153,150,144,107,102,102,87,80,57,55,49,48,45,26,26,23,15]
max_diff_sum(arr)

# from collections import deque as dq
#
# s='YazaAaay'
# ss=[]
# verify=[]
# flag=0
# for i in range(len(s)):
#     ss.append(s[i])
#     if len(ss)>1:
#         if (ss[i-1]).lower()!=(ss[i]).lower() :
#             ss[i-1]=''
#         else:
#             verify.append(''.join(ss))
# # return verify[0]
# print(verify)
#
# import PIL















