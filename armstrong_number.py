num=153
result=0
for i in range(3):
    a=num%10
    result+=a*a*a
    num=num//10
print(result)