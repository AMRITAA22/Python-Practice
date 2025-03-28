def highestSalary(d):
    max=0
    for i in d.values():
        if i>max:
            max=i
    return max

d={'prashant jha':200000,'ashish':25000,'sudesh':30000,'raunak':40000}

print(highestSalary(d))