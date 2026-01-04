# une variable qui permet de contenir plusieurs valeurs
# on a les listes = [] ordonnee et changeable. duplicates ok
# set = {} pas ordonnee et immuable. add et remove ok pas de duplicates
# tuple = () ordonnee et inchangeable. duplicates ok plus rapide
# on utilise [] pour acceder a un element




fruits = ["apple", "banana", "cherry", "orange"]
#print(fruits)
#print(fruits[1])
#print(fruits[::2])
#print(fruits[::-1])
#print(dir(fruits))
#print(help(fruits))
#print(type(fruits))
#for x in fruits:
#on peut etirer sur une liste
#for fruit in fruits:
 #   print(fruit)
#print(len(fruits))

# on peut utilise boolean pour voir si un element est dans la liste
#print("melon" in fruits)
#changer un element par un autre
#fruits[0] = "pineapple"
#print(fruits)

# on peut ajouter un nouveau element dans la liste
#fruits.append("melon")
#fruits.remove("apple")
# insere un element dans un index donne
#fruits.insert(0,"strawberry")
# ordre alphabetiques
#fruits.sort()
#fruits.reverse()
#supprime les elements
#fruits.clear()
# donne index pour un element
#print(fruits.index("apple"))
# permet de compter combien il y a de fois un elements. duplicates ok dans list
print(fruits.count("apple"))
print(fruits)


