mylist=[2,5,1,4,7,9,5]
even=0
odd=0
for i in mylist:
    if i%2==0:
        even+=i
    else:
        odd+=i
print(even*odd)
    