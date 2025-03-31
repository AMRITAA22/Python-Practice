name='aabbbbeeeeffggg'
newdict={}
for i in range(len(name)):
    key=name[i]
    count=0
    for j in range(len(name)):
        if key==name[j]:
            count+=1
    newdict[key]=count
for i,j in newdict.items():
    print(i,j,end='',sep='')