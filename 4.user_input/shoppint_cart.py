item = input("What item would you like to buy: ")
price = float(input("What is it price: "))
amount = int(input("How many would you like to buy: "))

total = price * amount

print(f"You spend ${total} in {item}")