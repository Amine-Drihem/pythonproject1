# object = a bundle of related attributes(variable) and methods
# ex phone, cup, book
# you need a class to create many object
# class = (blueprint) used to design the structure and layout of an object

from car import Car

car1 = Car("Fiat", 2024, "black", False)
car2 = Car("toyota", 2025, "red", True)
car3 = Car("charger", 2026, "yellow", True)
# si on veut acceder a l'attribut
"""
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
"""
# acceder aux methodes descriptives de car
#car1.drive()
#car2.drive()
#car3.drive()
#car1.stop()
#car2.stop()
#car3.stop()
#car1.describe()
#car2.describe()
#car3.describe()

