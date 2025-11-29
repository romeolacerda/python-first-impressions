height = int(input("Enter your piramid height: "))

for i in range(1, height + 1):
    spaces = " " * (height - i)
    blocks = "#" * (2 * i - 1)
    print(f"{spaces}{blocks}")