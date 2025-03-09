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
print("He fought "+str(battles-1)+" battles, and died.")

# food=[]
# foodrequest=0
# num=0
# while not foodrequest=="end":
#     foodrequest=input("What would you like to order?")
#     if foodrequest=="end":
#         break
#     food.append(foodrequest)
# print("You have ordered the following:")
# for i in food:
#     num=num+1
#     print(str(num)+". "+i)