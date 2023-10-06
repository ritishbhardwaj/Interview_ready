
def longest_subarray_with_atmost_sum_k(arr,k):
    l1=0

    #====== BRUTE FORCE ========
    for i in range(len(arr)):
        v=arr[i]
        for j in range(i,len(arr)):
            if i!=j:v+=arr[j]
            if v<=k:
                l1=max(l1,j-i+1)
    # print(l1)

    n=len(arr)
    i=j=s=l=0
    A=arr[:]
    neg_sum = [0] * n   # ADDED
    rs = 0
    for j in range(n-1, -1, -1):
        neg_sum[j] = rs
        rs = min(0, rs + A[j])
    # s+=arr[0]   
    while j<n:
        s+=arr[j]

        if s+neg_sum[j]<=k:
            l=max(l,abs(j-i)+1)
            j+=1
        
        elif s>k:

            while s>k and i<n and i<=j:
                s-=arr[i]
                i+=1
                        
            j+=1
            # if i>j:
            #     i=j
    
    # print(l)
    # print()
    return l1,l







arr = [1, 2, 1, 0, 1, -8, -9, 0]
k = 4
# Output is 8
# longest_subarray_with_atmost_sum_k(arr,k)

arr= [1, 2, 1, 0, 1, 1, 0]
k = 4
# output is 5
# longest_subarray_with_atmost_sum_k(arr,k)

arr=[-1, -1, 10, -1, -1]
k=6 
#output is 5
# longest_subarray_with_atmost_sum_k(arr,k)

longest_subarray_with_atmost_sum_k([1,-1],-1)


# n = int(input())
# k = int(input())
# b = [0] * (n + 1)
# i = 1
# while i <= n:
#     b[i] = int(input())
#     i += 1

# i = 1
# j = 1
# mv = 0

# gg = 0
# sum = b[1]
# while i <= n and j <= n:
#     if i == j:
#         if b[i] > k:
#             i += 1
#             j += 1
#             if i <= n:
#                 sum = b[i]
#         else:
#             kk = 1
#             mv = max(kk, mv)
#             j += 1
#             if j <= n:
#                 sum += b[j]
#     else:
#         if sum > k:
#             # [i....j] is invalid but [i......j-1] was valid
#             # so->[i+1...j-1] will also be valid hence
#             # i++ and j--
#             sum -= b[i]
#             i += 1
#             sum -= b[j]
#             j -= 1
#             if i > j:
#                 j = i
#         else:
#             kk = abs(i - j) + 1
#             j += 1
#             if j <= n:
#                 sum += b[j]
#             mv = max(kk, mv)

# print(mv)

def longest_subarray_with_at_most_k(A, k):
    n = len(A)
    res, si, sj = 0, None, None
    
    neg_sum = [0] * n   # ADDED
    rs = 0
    for j in range(n-1, -1, -1):
        neg_sum[j] = rs
        rs = min(0, rs + A[j])
    # print(neg_sum)
    ws = 0
    i = 0
    for j in range(n):
        ws += A[j]
        while i < j and ws + neg_sum[j] > k:  # CHANGED
            ws -= A[i]
            i += 1
            
        if (j - i + 1) > res:
            res = (j - i + 1)
            si, sj = i, j
    return (res, A[si:sj+1]) if res != 0 else (res, [])


for A, k in [
    ([-1,-1,10,-1,-1],6),
    ([1,1,-1],-1),
    ([9,1,2,3,4,5], 7),
    ([5, -10, 7, -20, 57], -22),
    ([-5, 8, -14, 2, 4, 12], 5),
    ([1, 2, 1, 0, 1, -8, -9, 0], 4)
]:
    print(A, k, '=>', longest_subarray_with_at_most_k(A, k))

print()
for A, k in [
    ([-1,-1,10,-1,-1],6),
    ([1,1,-1],-1),
    ([9,1,2,3,4,5], 7),
    ([5, -10, 7, -20, 57], -22),
    ([-5, 8, -14, 2, 4, 12], 5),
    ([1, 2, 1, 0, 1, -8, -9, 0], 4)
]:
    print(A, k, '=>', longest_subarray_with_atmost_sum_k(A, k))