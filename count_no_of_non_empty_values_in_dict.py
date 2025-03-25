d={"A":1,"B":"", "c":3,"d":None,"E":"five"}
count=0
for i in d.values():
    if i==None or i=="":
        pass
    else:
        count+=1
print(count)