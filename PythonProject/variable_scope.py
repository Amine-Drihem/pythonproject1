# variable scope = une variable devient visible et accessible
# une fonction ne peut pas voir le contenu d'une autre fonction
# scope resolution = (LEGB) local -> enclosed -> global -> built-in
def func1():
    # la variable a est locale a func1

    print(x)

def func2():
    # la variable b est locale a func2

    print(x)
# ce x est global
x = 3
func1()
func2()