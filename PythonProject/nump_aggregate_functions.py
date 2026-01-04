import numpy as np

# summarize data and typically return a single value

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

#print(np.sum(array))
#print(np.mean(array))
#print(np.std(array))
#print(np.var(array))
#print(np.min(array))
#print(np.max(array))
# si on veut la position de la valeur minimale
#(np.argmin(array))
# si on veut la position du max
#print(np.argmax(array))
# on somme les colonnes avec axis = 0
print(np.sum(array, axis=0))
# on somme les lignes avec axis = 1
print(np.sum(array, axis=1))