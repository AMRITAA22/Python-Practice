mylist=[5,3,9,2,8]
max=min=mylist[0]
for i in range(len(mylist)):
    if max<mylist[i]:
        max=mylist[i]
    if min>mylist[i]:
        min=mylist[i]
print(max)
print(min)

