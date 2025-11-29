# while loop = execute some code WHILE some condition remains true

name = input("Enter your name")

while name == "":
    print("You did not enter your name: ")
    name = input("Enter your name: ")
print(f"Hello {name}")

food = input("Enter a food you would like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")

print("bye")