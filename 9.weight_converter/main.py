
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = round((weight * 2.205), 3)
    unit = "Lbs."
    print(f"Your weight is: {weight} {unit}")
elif unit == "L":
    weight = round((weight / 2.205), 3)
    unit = "Kgs."
    print(f"Your weight is: {weight} {unit}")
else:
    print(f"{unit} was not valid")
