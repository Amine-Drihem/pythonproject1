

#def add(a, b):
#    return a+b
# si on veut ajouter un troisieme arg on ne peut pas.
#print(add(1,2))

#def add(*args):
#    total = 0
#    for arg in args:
#        total += arg
#    return total

#print(add(1, 2, 3, 4))

#def display_name(*args):
#    for arg in args:
#        print(arg, end = " ")
#display_name("amine","drihem")

#def print_adress(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key}: {value}")
#print_adress(street= "123 aaa",
#             city="detroit",
#             state="michigan",
#             zip="231321")


def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end = " ")
    print("")
    for value in kwargs.values():
        print(value, end = " ")

shipping_label("mr", "amine", "drihem",
               street="123 aaa",
               apt="100",
               city="detroit",
               state="MI")
