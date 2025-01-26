import time

HOWLONGUWANT = int(input("How many seconds do you want to study for?"))
Hi=HOWLONGUWANT/60
HII=HOWLONGUWANT
counter= HOWLONGUWANT
while counter != 0:
    print(counter)
    counter=counter-1
    time.sleep(1)
str(HOWLONGUWANT)
print("You studied for "+str(HOWLONGUWANT)+" seconds or "+str(Hi)+" minutes or "+ str(HII) +"hours and gained 0 brain cells.")


