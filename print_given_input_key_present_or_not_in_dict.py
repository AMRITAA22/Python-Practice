def highestSalary(d):
    name=input("enter a name: ")
    if name in d.keys():
        return 'yes exist'
    else:
        return 'not exist'

d={'prashant jha':200000,'ashish':25000,'sudesh':30000,'raunak':40000}
print(highestSalary(d))