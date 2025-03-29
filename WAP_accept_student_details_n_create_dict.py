N=int(input("enter the number of records: "))
dict={}
for i in range(N):
    roll_no=int(input("enter student roll no: "))
    full_name=input("enter student full name: ")
    dict[roll_no]=full_name
print("student roll number=",dict)

while True:
    roll_no=int(input("enter student roll no to retrive full name: "))
    name=dict.get(roll_no)
    if name:
        print("roll number",roll_no,' ','full name',name)
    else:
        print("no student name found")
    val=input("do you want to continue so enter y/n")
    if val=='No' or 'no':
        break

