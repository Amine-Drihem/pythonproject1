# on peut avoir un loop dans un autre loop comme un while dans un while, etc
# on peut mettre end = quelque chose pour avoir les chiffres en ligne
# permet de executer le code trois fois donc compter 1 a 10 trois fois

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("enter a symbol to use: ")


for x in range(rows):
    for i in range(columns):
        print(symbol, end="")
    print("")
