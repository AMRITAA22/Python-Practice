A=[]
B=[]
n1=int(input("enter the size of array: "))
for i in range(n1):
    A.append(input())
n2=int(input("enter the soze of array: "))
for j in range(n2):
    B.append(input())
if len(A)==len(B):
    print("compartible")
else:
    print("not comptible")