def fun(n):
    if n>100:
        return n-5
    
    return fun(fun(n+11))

print(fun(45))


dict={
    (1,2,4):8,
    (4,2,1):10,
    (1,2):11
}

sum=0

for k in dict:
    print(k)
    sum+=dict[k]
    # print(dict.pop)

print(len(dict)+sum)


def fun1(v):
    v+=10
    print(v)
v=12
fun1(v)
print(v)


dict1={
    "phy":94,
    "che":70,
    "bio":82,
    "eng":95
}
# [dict1.pop(k) for k,v in dict1.items() if v>90]

print(dict1)

vv=[(a,b) for a in range(3) for b in range(a)]
print(vv)



# example to demonstrate list is a mutable data type in python

# our current list
my_list = [1,2,3,4,5]

# using append operation in our list
my_list.append(3)
# printing our list after the operation
print("List after appending a value = ",my_list)

# using extend operation in our list
my_list.extend([6,11,23])
# printing our list after the operation
print("List after extending a list = ",my_list)

# after removing a value from our list
my_list.remove(3)
# printing our list after the operation
print("List after removing a value = ",my_list)



my_set = {1,2,6,5,7,11}

# adding an element in our set
my_set.add(16)
# printing our set after the operation
print("Set after adding a value : ",my_set)

# adding multiple elements in our set
# multiple elements (such as a list) can be added using update
my_set.update({9,78,100})
# printing our set after the operation
print("Set after updating some values : ",my_set)

# removing element from our set
my_set.pop()
# printing our set after the operation
print("Set after removing a value : ",my_set)