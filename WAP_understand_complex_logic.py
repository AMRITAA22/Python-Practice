mylist=[8,6,3,4,7]
avg=0
split_add=0
for i in range(len(mylist)):
    avg=avg+mylist[i]
print(avg)
for i in range(2):
    split_add+=avg%10
    avg=avg//10
print(split_add)
