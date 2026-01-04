
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter a principle: "))
    if principle <= 0:
        print("principle cant be less or equal to zero")

while rate <= 0:
    rate = float(input("Enter a rate in percent: "))
    if rate <= 0:
        print("rate cant be less or equal to zero")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("time cant be less or equal to zero")

total = principle * (1+rate/100)**time
print(f"the total value of investment in {time} year(s) is {total:.2f}$")