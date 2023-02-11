def sol(ind,s:str , storage:list , ds:list ,n):
    if ind>=n:
        storage.append(list(ds))
        return
    for i in range(ind,n):
        if isPalindrome(s,ind,i):
            ds.append(s[ind:i+1])
            sol(i+1,s,storage,ds,n)
            ds.pop()                       #  Previously i did --->  ds.remove(s[ind:i+1])   
                                            #  so what is wrong in it is that if i need to remove c from last but there is c fresent at 0th index then that c will get remove so wrong answer will come out

def isPalindrome(string:str, start:int , end:int ):
    while start<end:
        if string[start]!=string[end]:
            return False
        start+=1
        end-=1
    # print(b,'jj')
    return True


s = "cbbbcc"

storage=[]
ds=[]
ind=0
n=len(s)
sol(ind,s,storage,ds,n)
print(storage)

# [["c","b","b","b","c","c"],["c","b","b","b","cc"],
# ["c","b","bb","c","c"],["c","b","bb","cc"],["c","bb","b","c","c"],
# ["c","bb","b","cc"],["c","bbb","c","c"],["c","bbb","cc"],["cbbbc","c"]]