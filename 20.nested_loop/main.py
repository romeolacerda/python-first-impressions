
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbols = input("Enter a symbol to use")

for x in range(rows):
    for y in range(columns):
        print(symbols, end="")
    print()