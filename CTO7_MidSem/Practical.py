import random
print("Hero starts on his adventure with Health: 100")
health=100
randomhealth=random.randint(1,15)
battles=0
while health>0:
    health=health-randomhealth
    battles=battles+1
    if health<0 or health==0:
        break
    print("After fighting monsters, his Health is now: "+str(health) )
print("After fighting monsters, his Health is now:"+str(health)+". He fought "+str(battles)+", and died.")