import time
HOWLONGUWANT = int(input("How long do you want to study for?"))
counter= HOWLONGUWANT
while counter != 0:
    print(counter)
    counter=counter-1
    time.sleep(1)
print("You studied for"+counter+"minutes")


