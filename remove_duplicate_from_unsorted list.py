mylist=[1,2,3,2,6,9,2]
newlist=[]
for i in mylist:
    if i not in newlist:
        newlist.append(i)
    else:
        pass
print(newlist)