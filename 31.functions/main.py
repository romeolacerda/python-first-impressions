
def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")    
    print(f"You are {age} years old!")
    print("Happy birthday to you!")    
    print()
    
happy_birthday("Bro", 20)
happy_birthday("Steve", 30)
 
def create_name(first, last):
    first = first.capitalize()
    last  = last.capitalize()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)