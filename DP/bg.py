import math

def find_pairs(arr):
    bcount = arr[2] // 2
    gcount = arr[2] - bcount

    boy_comb = math.comb(arr[0], bcount)
    # print(boy_comb)
    girl_comb = math.comb(arr[1], gcount)
    permut = math.perm(arr[2] // 2)

    return boy_comb * girl_comb * permut

arr = [5,5,4]
print(find_pairs(arr))




def find_largest_submatrix_area(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_area = 0

    for i in range(rows):
        for j in range(cols):
            if i == 0 or matrix[i][j] == '0':
                dp[i][j] = int(matrix[i][j])
            else:
                dp[i][j] = dp[i - 1][j] + 1

            min_width = dp[i][j]
            for k in range(j, -1, -1):
                min_width = min(min_width, dp[i][k])
                max_area = max(max_area, min_width * (j - k + 1))

    return max_area

matrix1 = ["1011", "0011", "0111", "1111"]
matrix2 = ["101", "111", "001"]

print("Output for matrix1:", find_largest_submatrix_area(matrix1))
print("Output for matrix2:", find_largest_submatrix_area(matrix2))
