N=int(input("enter a number: "))
mylist=[]
newlist=[]
square=0
count=0
for i in range(N):
    a=int(input())
    mylist.append(a)
for i in range(1,N+2):
    square=i*i
    if square in mylist:
        newlist.append(square)
        count+=1
print(count)
print(newlist)