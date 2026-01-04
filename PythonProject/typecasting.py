# convertir une variable dans une autre forme de donnee

age = 23
gpa = 4.15
is_student = True

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(type(age))

gpa += 1
print(gpa)

name = input("Enter your name: ")
name = bool(name)
if name == False:
    name = input("Enter your name: ")
else:
    print(f"salut {name}")