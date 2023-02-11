def sol(s,k):
    l=[]
    i,j=0,0
    test=''
    for x in range(len(s)):
        for j in range(x+1,len(s)+2):
            if int(s[x:j])<=k:
                continue
                # l.append(s[x:j])
                # break
            l.append(s[x:j-1])
            break
    print(l)



s = "165462"
k = 60
sol(s,k)