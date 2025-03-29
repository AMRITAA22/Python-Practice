d={"A":1,"B":2,"C":3}
newdict={}
for i,j in zip(d.keys(),d.values()):
    newdict[j]=i
print(newdict)