# collection = single "variable" used to store multiple values
# List = [] ordered and changeble. Duplicates Ok
# Set = {} unordered and immutable, but Add/Remove Ok. No Duplicates
# Tuple = () ordered and unchangeble. Duplicates Ok. FASTER

fruits = ["apple", "orange", "banana", "coconut"]

# print(fruits[0])
print("---------- LISTS -------------")
fruits[0] = "pineapple"
fruits.append("grapes")
fruits.remove("banana")
fruits.sort()
# fruits.clear()
print(fruits.index("orange"))
print(fruits.count("orange"))
print("apple" in fruits)
for fruit in fruits:
    print(fruit)
    
    
print("---------- SETS -------------")
fruits = {"apple", "orange", "banana", "coconut"}

print(fruits)

# print(fruits[0]) # it will give an error cause sets are not subscriptable
fruits.add("grapes")
fruits.remove("banana")
fruits.clear()

print("---------- TUPLES -------------")

fruits = ("apple", "orange", "banana", "coconut")
print(fruits)
for fruit in fruits:
    print(fruit)
