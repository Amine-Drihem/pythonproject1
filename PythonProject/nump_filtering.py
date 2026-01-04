import numpy as np
# refers to the process of selecting elements from an array that match a condition

ages = np.array([[21,17,19,20,30,18,65],
                 [39,22,15,99,18,20,21]])
#teenagers = ages[ages < 18]
#print(teenagers)
#adults = ages[(ages >= 18) & (ages < 65)]
# | la barre represente le ou
#seniors = ages[ages >= 65]
#evens = ages[ages % 2 == 0]
#odds = ages[ages % 2 != 0]

#print(adults)
#print(seniors)
#print(evens)
#print(odds)
# permet de preserver le shape initial
adults = np.where(ages >= 18, ages, 0 )
print(adults)