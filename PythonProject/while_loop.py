# execute un code tant que une condition est vraie
"""
name = input("Enter your name: ")
#tant que la condition dans le while est vrai le code se repete
while name == "":
    print("vous devez entrer un nom")
    name = input("Enter your name: ")
print(f"hello {name}")
"""
"""
age = int(input("Enter your age: "))

while age < 0:
    print("age cant be negative")
    age = int(input("Enter your age: "))
print(f"you are {age} years old")
"""
"""
food = input("enter a food you like ( press q to quit): ")
while not food == "q":
    print(f"you like {food}")
    food = input("enter a food you like ( press q to quit): ")
print("bonne journee")
"""

num = int(input("Enter a number between 1 to 10: "))
while num < 1 or num > 10:
    print(f"{num} is not between 1 and 10")
    num = int(input("Enter a number between 1 to 10: "))
print(f"your number is {num}")