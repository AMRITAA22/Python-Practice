salary=int(input("enter your salary: "))
rating=float(input("enter your rating: "))
increment=0
if salary!=0:
    if rating>=1 and rating<=3:
        increment=salary*10/100
    elif rating>=3.1 and rating<=4:
        increment=salary*30/100
    elif rating>=4.1 and rating<=5:
        increment=salary*50/100
    else:
        print("invalid salary")
else:
    print("invalid salary")
print("total incremented : ",increment)
print("total incremented salary: ",increment+salary)