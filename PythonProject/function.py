# c'est un block de code a reutiliser
"""
def happy_birthday(name, age):
    print(f"happy birthday {name}")
    print(f"you are {age} years old")
    print("happy birthday")
    print("")

happy_birthday("bro", 20)
happy_birthday("steve", 30)
happy_birthday("joe", 40)


def display_invoice(username, amount, due_date):
    print(f"hello {username}")
    print(f"your bill of {amount:.2f} is due: {due_date}")

display_invoice("joe", 52.50, "2025")

# returen = statement used to end a function
# il renvoie un resultat

def addition(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z
print(addition(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))
"""

def creat_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first +" "+ last

full_name = creat_name("amine", "drihem")
print(full_name)

