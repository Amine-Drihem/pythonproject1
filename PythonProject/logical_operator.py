# or = at least one condition must be true
# and = both conditions must be true
# not = inverts the condition ( not false, not true)




"""
temp = -5

is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("the outdoor event is canceled")
else:
    print("the outdoor event is still scheduled")
"""
temp = 20
is_sunny = False
if temp >= 28 and is_sunny:
    print("it is hot outside")
    print("it is sunny")
elif temp <= 0 and is_sunny:
    print("it is cold outside")
    print("it is sunny")
elif 28 > temp > 0 and is_sunny:
    print("it is warm outside")
    print("it is sunny")
elif temp >= 28 and not is_sunny:
    print("it is hot outside")
    print("it is cloudy")
elif temp <= 0 and not is_sunny:
    print("it is cold outside")
    print("it is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("it is warm outside")
    print("it is cloudy")