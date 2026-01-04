
unit = input("is this temperature in celsius or fahrenheit? (C OR F): ")
temp = float(input("enter the temperature: "))

if unit == "C":
    temp = round((temp * 9) / 5 + 32)
    print(f"the temperature in fahrenheit is {temp} F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"the temperature in celsius is {temp} C")
else:
    print(f"{unit} was not valid")