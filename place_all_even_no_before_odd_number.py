N=8
mylist=[10,98,3,33,12,22,21,11]
A=[]
B=[]
for i in range(len(mylist)):
        if mylist[i]%2==0:
            A.append(mylist[i])           
        else:
            B.append(mylist[i])
print(A+B)