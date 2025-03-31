v=['a','e','i','o','u']
w=input("enter the word where we will search the vowels: ")
found=[]
for i in w:
    if i in v:
        if i not in found:
            found.append(i)
print("found vowels: ",found)
print("unique vowels ",found,'from the gievn ')