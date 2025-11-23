name = "Bro"
age = 25
gpa = 5.0
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

age = float(age)
print(type(age))
print(age)

gpa = int(gpa)
print(type(gpa))
print(gpa)

age = int(age)
age = str(age)
age += "1"
print(type(age))
print(age)

name = bool(name)
print(name)

name = bool("")
print(name)