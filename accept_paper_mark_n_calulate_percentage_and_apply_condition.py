p1=int(input("enter paper 1 marks: "))
p2=int(input("enter paper 1 marks: "))
p3=int(input("enter paper 1 marks: "))
p4=int(input("enter paper 1 marks: "))
p5=int(input("enter paper 1 marks: "))
total=p1+p2+p3+p4+p5
percentage=total/5

if p1>=40 and p2>=40 and p3>=40 and p4>=40 and p5>=40:
    print("pass")
else:
    print("fail")
print(total)
print(percentage)