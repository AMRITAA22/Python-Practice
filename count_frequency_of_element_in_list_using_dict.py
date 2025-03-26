mylist=[1,2,2,3,4,3,5]
mydict={}
for i in mylist:
    count=0
    key=i
    for j in mylist:
        if key==j:
            count+=1
    mydict[str(key)]=count
    count=0
print(mydict)