import math
friends = 10
#friends += 1
#friends -= 1
#friends *= 3
#friends /= 2
#friends **= 2
remainder = friends % 3


print(remainder)
#print(friends)

x = 3.6
y = -4
z = 5
w = 9.9
#result = round(x)
#result = abs(y)
#exposant = pow(x,z)
#result_max = max(x, y, z)
#result_min = min(x, y, z)
#print(result_max)
#print(result_min)

#print(math.pi)
#print(math.e)
#result_carre = math.sqrt(z)
#result = math.ceil(w)
#result = math.floor(w)

#print(result)

# exercice circonferance cercle
"""

radius = float(input("Enter radius of a circle: "))
circumference = 2 * math.pi * radius

print(f"The circumference of the circle is {round(circumference,2)}")
"""
# exercice air cerce
"""
radius = float(input("Enter radius of a circle: "))
area = math.pi * pow(radius, 2)
print(f"The are of the circle is {round(area,2)} m^2")
"""

# exercice hypothenus triangle carre
base = float(input("entrer la valeur de la base du triangle carre: "))
hauteur = float(input("entrer la hauteur du triangle carre:"))
base_carre = pow(base, 2)
hauteur_carre = pow(hauteur, 2)
hypothenus = math.sqrt(base_carre + hauteur_carre)
print(f"la valeur de hypothenus est {hypothenus}")