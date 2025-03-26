value='aaabbbccc'
newvalue=''
for i in range(len(value)):
    count=0
    key=value[i]
    for j in value:
        if key==j:
            count+=1
    if key not in newvalue:
        newvalue+=key+str(count)
print(newvalue)