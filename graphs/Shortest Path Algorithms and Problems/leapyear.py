flag=1
m=2

if m==2:
    y=2100
    if y%4==0 and (y%100!=0 or y%400==0):
        days=29
        print(days)
    else:
        days=28
        print(days)
else:
    print("yes")
