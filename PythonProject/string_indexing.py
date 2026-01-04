# [start: end : step]
credit_number = "1234-4341123-231321"

#print(credit_number[4])
#print(credit_number[0:4])
#print(credit_number[5:9])
#print(credit_number[5:])
# si on veut le dernier caractere dans un string on met -1
#print(credit_number[-1])
#print(credit_number[-2])
#print(credit_number[::3])

last_digits = credit_number[-6:]
print(f"xxxxx-xxxx-xxxx-{last_digits}")
# mettre -1 pour le step va inverser le string
credit_number = credit_number[::-1]
print(credit_number)