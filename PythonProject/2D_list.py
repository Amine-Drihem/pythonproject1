# c'est une liste qui constuite a partir de liste
"""
fruits =     ["apple", "banana", "cherry", "coconut"]
vegetables = ["celery","carrots","potatoes"]
meats =      ["chicken", "fish", " turkey"]

#groceries = [fruits, vegetables, meats]
# on peut aussi ecrire comme cela
groceries = [["apple", "banana", "cherry", "coconut"],
             ["celery","carrots","potatoes"],
             ["chicken", "fish", "turkey"]]
#print(groceries[0])
#print(groceries[1])
#print(groceries[2])
# on a besoin de deux indices pour acceder a un element pour 2D list
#print(groceries[0][0])

# si on veut etirer sur 2D list on doit utiliser nested loop pour etirer sur les elements plutot que le lignes
for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print("")
"""

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))
for row in num_pad:
    for num in row:
        print(num, end = " ")
    print("")