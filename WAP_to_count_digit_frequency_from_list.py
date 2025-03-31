l=[1,2,3,3,4,1,4,5,1,2]
count=0
newdict={}
for i in range(len(l)):
    key=l[i]
    j=i+1
    for j in range(len(l)):
        if key==l[j]:
            count+=1
    newdict[key]=count
for i,j in newdict.items():
    print(i,'occur',j,'times')