x,y=map(int,input().split())
mylist=[]
for i in range(x):
    mylist.append([])
    for j in range(y):
        val=int(input('enter the values: '))
        mylist[i].append(val)
    print()
print(mylist)