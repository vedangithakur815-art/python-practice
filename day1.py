# first Question
print("Hello GitHub! My first program")

# Second question
my_item = input("enter the name of the item")
quantity = int(input("enter the quantity of the item"))
price = float(input("enter the price of the item"))

subtotal = price*quantity
tax = subtotal*0.05
total = subtotal + tax 

print("subtotal",subtotal)
print("tax(5%)",tax)
print("total amount",total)
