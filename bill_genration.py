pizza=int(input("enter the number of pizza brought: "))
burger=int(input("enter the number of burger brought: "))
colddrink=int(input("enter the number of cold drink brought:"))
total_pizza_price=pizza*100
total_burger_price=burger*50
total_colddrink_price=colddrink*20

print("-----------------------")
print("total pizza amount: ", total_pizza_price)
print("burger amount: " , total_burger_price)
print("cold drink amount: ", total_colddrink_price)
print("------------------------")
print("total amount: ",total_pizza_price+total_burger_price+total_colddrink_price)
print("------------------------")
