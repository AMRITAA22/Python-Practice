mylist=[
    [100, 198, 333, 323],
    [122, 232, 221, 111],
    [223, 565, 245, 764]
]
newlist=[]
for i in range(len(mylist)):
    j=0
    max=mylist[i][j]
    for j in range(len(mylist)):
        c_max=mylist[i][j]
        if max>c_max:
            max=c_max
    newlist.append(max)
print(newlist)