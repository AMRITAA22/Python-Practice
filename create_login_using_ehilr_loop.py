username='amrita'
password='a@20005'
user=input('enter username: ')
passw=input("enter password: ")
while username!=user or password!=passw:
    user=input('enter username: ')
    passw=input("enter password: ")
else:
    print("it match")