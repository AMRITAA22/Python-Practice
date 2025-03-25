l1=[1,2,2,1]
l2=[2,2]
newlist=[]
for i,j in zip(range(len(l1)),range(len(l2))):
    if l1[i]==l2[j]:
        if i not in newlist:
            newlist.append(l1[i])
print(newlist)

#method 2
l1=[1,2,2,1]
l2=[2,2]
newlist=[]
l1=set(l1)
l2=set(l2)
newlist=list(l1.intersection(l2))
print(newlist)