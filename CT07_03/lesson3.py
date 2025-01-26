import time
HOWLONGUWANT = int(input("How long do you want to study for?"))
counter= HOWLONGUWANT
while counter != 0:
    print(counter)
    counter=counter-1
    time.sleep(1)
str(HOWLONGUWANT)
print("You studied for "+str(HOWLONGUWANT)+" minutes and gained 0 brain cells.")


