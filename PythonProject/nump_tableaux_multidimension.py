import numpy as np
# zero dimensional array
#array = np.array("A")
#print(array.ndim)

# 1 dimensional array or single row
#array = np.array(["A","B","C","D"])
#print(array.ndim)

# 2 dimensionaal array
# on peut la voir en matrice avec des lignes et des colonnes
#array = np.array([["a", "b", "c"],
  #                ["d", "e", "f"],
 #                 ["g", "h", "i"]])
#print(array.ndim)

array = np.array([[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
                  [["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r"]],
                  [["s", "t", "u"], ["v", "w", "x"], ["y", "z", " "]]])
#print(array.ndim)
#shape qui montre la profondeur, le nombre de ligne et de colonne
#print(array.shape)

#pour acceder a un element on utilise le chain indexing
#print(array[0][0][0])

# on peut utiliser le multi dimensional indexing qui est plus rapide
#print(array[1,1,1])

word = array[0,0,0] + array[1,1,0] + array[0,2,2] + array[1,1,1] + array[0,1,1]
print(word)


