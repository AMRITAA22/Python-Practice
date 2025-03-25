d1={"A": 1, "B": 2,"C": 3}
d2={"B":2,"c":4,"D":5}
for i in d1.items():
    for j in d2.items():
        if i==j:
            print(i)
        