def fib(n,dp):
    if n<=1: return n

    if dp[n]!=-1: return dp[n]

    res=fib(n-1,dp)+fib(n-2,dp)
    dp[n]=res
    return dp[n]

n=5
dp=[-1]*(n+1)
print(fib(n,dp))
# print(dp)