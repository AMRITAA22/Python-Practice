N=5
sum=0
mylist=[]
for i in range(N):
    a=int(input("enter a number: "))
    mylist.append(a)
for j in range(len(mylist)):
    if j+1 in range(len(mylist)):
        sum+=abs(mylist[j]-mylist[j+1])
print(sum)
