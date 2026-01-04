import numpy as np

#array = np.array([1, 2.6, 3.2, 4])

#print(np.sqrt(array))
#print(np.round(array))
#print(np.floor(array))
#print(np.ceil(array))
#print(np.pi)

#exercice

#radii = np.array([1,2,3])
#print(np.pi * radii**2)

#element-wise arithmetic
#array1 = np.array([1,2,3])
#array2 = np.array([4,5,6])
#print(array1 + array2)
#print(array1 - array2)
#print(array1 * array2)
#print(array1 / array2)
#print(array1 ** array2)

#comparison operators boolean
scores = np.array([91,55,100,73,82,64])
print(scores >= 60)
print(scores < 60)
scores[scores < 60] = 0
print(scores)


