# *args = allows you to pass multiple non-key arguments
# **kargs = allows you to pass multiple keyword-arguments
#         *unpacking operator
#         1.positional, 2.default, 3.keyword, 4.ARBITRAY

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Bro", "Code")

print()

def print_adress(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}") 

print_adress(street="123 Fate St.", city="Detroit", state="MI", zip="5432")


def shippting_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

shippting_label("Bro", "Code", "Yt", street="123 Fate St.", city="Detroit", state="MI", zip="5432")