
operator = input("Enter a operator (+ - * /): ")

numA = float(input("Enter number A : "))

numB = float(input("Enter number B :"))

if operator == "+":
    result = round((numA + numB), 3)
    print(f"Your result is {result}")
elif operator == "-":
    result = round((numA - numB), 3)
    print(f"Your result is {result}")
elif operator == "*":
    result = round((numA * numB), 3)
    print(f"Your result is {result}")
elif operator == "/":
    result = round((numA / numB), 3)
    print(f"Your result is {result}")
else:
    print("You give an invalid operator")
    