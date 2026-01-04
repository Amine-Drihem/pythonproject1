# default arguments = a default value for certain parameters.
# default is used when that argument is omitted
#permet de reduire le # de argument
# on a le positional argument vu avant, default, keyword et arbitrary

#def net_price(list_price, discount = 0, tax = 0.05):
#    return list_price * (1 - discount) * (1 + tax)
# on peut mettre discount et tax avec une valeur de defaut
# cela evite de devoir changer a chaque fois et de devoir rentrer trois arg
#print(net_price(500))
# n'utilise plus la valeur de default
#print(net_price(500,0.1))
#print(net_price(500,0.1, 0))


import time

def count(end, start = 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("done!")

count(30,15)




