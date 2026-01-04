# une facon plus concise de creer des listes sur python


#doubles = []

#for x in range(1,11):
 #   doubles.append(x*2)

#print(doubles)

# doubles = [expression for value in iterable if condition]
"""
doubles = [x * 2 for x in range(1,11)]
triples = [y * 3 for y in range(1,11)]
squares = [z * z for z in range(1,11)]
print(doubles)
print(triples)
print(squares)


fruits = ["apple", "banana", "cherry"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)


fruits = ["apple", "banana", "cherry"]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)
"""

numbers = [1, -2, 3, -4, 5, -6]

positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)