""""
age = input("enter your age: ")

if int(age) >= 100:
    print("you are too old to sign up")

elif int(age) >= 18:
    print("you are now signed up!")
elif int(age) < 0:
    print("you have not been born yet!")

#on utilise le else a la toute fin si on a autres conditions utiliser elif
else:
    print("you must be 18+ to sign up!")
"""
"""
name = input("enter your name: ")
if name == "":
    print("please enter your name")
    while name == "":
        name = input("enter your name: ")
print(f"salut {name}")
"""
for_sale = False
if for_sale:
    print("this item is for sale")
else:
    print("this item is not for sale")
