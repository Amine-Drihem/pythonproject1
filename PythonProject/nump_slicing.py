import numpy as np
# 2 dimensional array une matrice
array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])
# on parle ici de row selection dans la matrice
# array[start:end:step]

#print(array[1])
#print(array[2])
#print(array[3])
#print(array[-1])
#print(array[0: 3])
#print(array[1:4])
#print(array[1:])

#print(array[0:4:2])
# ou on met comme cela
#print(array[::2])
# on peut mettre le step negative pour commencer par la fin
#print(array[::-1])

# maintenant on passe a column selection
# premiere colonne = index 0, deuxieme = index 1 et etc
# on utilise des vigules pour separer ligne et colonne
#print(array[:,0])
#print(array[:,1])
#print(array[:,2])
#print(array[:,3])
#print(array[:,-1])
#print(array[:, :3])
#print(array[:, 1:4])
#print(array[:,::2])
#print(array[:,1::2])
#print(array[:,::-2])

# on veut seulement certaines lignes colonnes
print(array[0:2,0:2])
print(array[0:2,2:4])
print(array[2:,0:2])