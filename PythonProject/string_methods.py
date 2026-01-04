
#name = input("Enter your full name: ")
#phone_number = input("Enter your phone number: ")

#result = len(name)
#result = name.find(" ")
# trouve le premier occurence
#result = name.find("e")
# trouve le premier occurence a partir de la fin
#result = name.rfind("")
#met en majuscule la premiere lette
#result = name.capitalize()
#met tout en majuscule
#result = name.upper()
# met tout en minuscule
#result = name.lower()
# envoie true seulement si name contient que des chiffres
#result = name.isdigit()
# envoie true seulement si name contient que des lettres et pas de espace
#result = name.isalpha()
#permet de denomber un caractere
#result = phone_number.count("-")
#result = name.count("e")
# remplacer un caractere par un autre
#result = name.replace( "e", "z")
#print(result)

#exercice
user_name = input("Enter a username: ")

if len(user_name) > 12:
    print("username is too long")
elif not user_name.find(" ") == -1:
    print("your username cant contain spaces")
elif not user_name.isalpha():
    print("your username cant contain numbers")
else:
    print(f"welcome {user_name}")