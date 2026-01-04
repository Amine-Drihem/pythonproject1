#execute un block de code un nombre de fois x. on peut iterer sur un range, string, sequence.
# mettre reversed devant range pour compter depuis la fin
# range(start,end,step)
"""
for i in reversed(range(1,11,2)):
    print(i)
print("coucou")

# on peut etirer sur un string
"""
"""
credit_card  = "1234-5678-1246"
for i in credit_card:
    print(i)
"""
# utiliser continue pour skip une iteration
# si on met break on va sortir de la boucle.
"""
for i in range(1,21):
    if i == 13:
        continue
    else:
        print(i)
for i in range(1,21):
    if i == 13:
        break
    else:
        print(i)
"""
