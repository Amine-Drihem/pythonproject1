# une collection de {key:value} pairs ordonnee et changeable. pas de duplicates

capitals = {"USA": "washington DC", "India": "new delhi", "china": "beijin","canada":"ottawa"}
#print(dir(capitals))
#print(help(capitals))

#print(capitals.get("USA"))
#print(capitals.get("japan"))

#if capitals.get("India"):
#    print("that capital exists")
#else:
#    print("that capital does not exist")

#capitals.update({"germany":"berlin"})
#.update({"USA":"detroit"})
#capitals.pop("china")
#enleve le dernier item ajoutee le popitem
#capitals.popitem()
#capitals.clear()

#pour obtenir les keys mais pas les valeurs
#keys = capitals.keys()

#for key in capitals.keys():
 #   print(key)
#print(keys)

# pour obtenir just les values
#values = capitals.values()
#(values)

#for value in capitals.values():
#    print(value)

items = capitals.items()
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")
