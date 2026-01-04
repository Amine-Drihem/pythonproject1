import time
# permet de figer le code pendant 3 secondes time.sleep()

my_time = int(input("enter the time in seconds: "))

for i in range(my_time, 0 , -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("time is up")