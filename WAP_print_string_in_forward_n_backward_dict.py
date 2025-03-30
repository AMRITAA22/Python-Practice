string=input("enter a string: ")
for i in range(len(string)):
    print("forward direction",string[i])
print("--------------------------------")
j=-1
s=len(string)
while j>=-s:
    print("backward direction: ",string[j])
    j=j-1