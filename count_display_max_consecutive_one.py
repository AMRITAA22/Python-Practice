mylist=[1,1,0,1,1,1,0,1,1,1,1]
newlist=[]
count=0
for i in mylist:
    if i==1:
        count+=1
    else:
        newlist.append(count)
        count=0
newlist.append(count)
print(newlist)