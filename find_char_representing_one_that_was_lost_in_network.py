name='abcdfjgerj abcdfijger'
def stringvarifye(name):
    for i in range(len(name)):
        if name[i] == ' ':
            return name[i-1]
name=input(' ')
result=stringvarifye(name)
if result:
    print(result)
else:
    print('NA')