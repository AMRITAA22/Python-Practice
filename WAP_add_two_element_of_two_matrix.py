x,y=map(int,input().split())
A=[]
B=[]
C=[]
for i in range(x):
    A.append([])
    for j in range(y):
        val=int(input('enter the value for A: '))
        A[i].append(val)
    print()
print(A)