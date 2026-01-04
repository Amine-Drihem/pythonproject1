# permet de formater une valeur selon les flags dans un f string
# format specifiers = {value:flags}

price1 = 3.14159
price2 = -987.65
price3 = 12.34
# .2f pour avoir deux decimales .3f pour trois decimales et etc
# si on ecrit:10 alors le output aura 10 espaces pour ecrire
print(f"price 1 is {price1:.2f}$")
print(f"price 2 is {price2:.2f}$")
print(f"price 2 is {price3:.2f}$")

print(f"price 1 is {price1:10}$")
print(f"price 2 is {price2:10}$")
print(f"price 2 is {price3:10}$")
# justifier par la gauche < ou par la droite > qui est le default
print(f"price 1 is {price1:<10}$")
print(f"price 2 is {price2:<10}$")
print(f"price 2 is {price3:<10}$")
# center les caracteres
print(f"price 1 is {price1:^10}$")
print(f"price 2 is {price2:^10}$")
print(f"price 2 is {price3:^10}$")
# si on veut afficher des nombres en positives ou negatives auto
print(f"price 1 is {price1:+}$")
print(f"price 2 is {price2:+}$")
print(f"price 2 is {price3:+}$")
# on peut mettre deux arguments pour les flags
print(f"price 1 is {price1:+,.2f}$")
print(f"price 2 is {price2:+,.2f}$")
print(f"price 2 is {price3:+,.2f}$")