
operator = input("enter an operator (+ - * /): ")
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

if operator == "+":
    print(round(num1 + num2, 3))
elif operator == "-":
    print(round(num1 - num2, 3))
elif operator == "*":
    print(round(num1 * num2, 3))
elif operator == "/":
    print(round(num1 / num2, 3))
else:
    print(f"your {operator} is not a valid operator")

