# import time

# HOWLONGUWANT = int(input("How many seconds do you want to study for?"))
# Hi=HOWLONGUWANT/60
# HII=HOWLONGUWANT/3600
# HIII=HOWLONGUWANT/86400
# counter= HOWLONGUWANT
# while counter != 0:
#     print(counter)
#     counter=counter-1
#     time.sleep(1)
# str(HOWLONGUWANT)
# print("You studied for "+str(HOWLONGUWANT)+" seconds or "+str(Hi)+" minutes or "+ str(HII) +"hours or "+str(HIII)+ " days and gained 0 brain cells.")


# savings=0
# while savings<100:
#     savings+=float(input("How much did you save today?"))
# print("Finally, you are $100 less poor!")

# import random

# lives=3
# num1=0
# ans=0
# Ans=1
# for i in range(1,15):
#     num1=int(random.randint(2,1043534513))
#     num2=random.randint(2,389578321657189)
#     Ans=num1*num2
#     while not ans==Ans:
#         ans=int(input("What is "+str(num1)+" x "+str(num2)+" ?"))
#         if Ans==ans:
#             print("Correct!")
#             break
#         else:
#             lives=lives-1
#             print("FAIL!!AGAIN!")
#         if lives==0:
#             print("SEE MRS TAN U! FAILURE")
# if lives>0:
#     print("FINALLY!AVERAGE BUT SLOW!")
        
# PLANTS=[
# "MERCOOREE","VENoos","EERTH","MERS","JOOPIRERTER","sETUren","uRENUS","Niptoone"
# ]
# PLANTS.insert(4,"Lalaland")
# PLANTS.append("BLUETOES")
# for i in range(len(PLANTS)):
#     print(PLANTS[i])
#     if PLANTS[i]=="EERTH":
#         print("This is my home")
#     if PLANTS[i]=="MERS":
#         print("I conquered this")
#     if PLANTS[i]=="Lalaland":
#         print("I created this")


# i=0
# COONTREES=[]
# ans=0
# while not ans == "end":
#     ans=str(input("What country do you want to visit"))
#     COONTREES.insert(i,ans)
#     i=i+1
# for a in range(len(COONTREES)-1):
#     print("I want to visit "+ COONTREES[a] +".")

i=0
MEENU=[]
ans=0
while not ans == "end":
    ans=str(input("What menu item do you want to add?"))
    MEENU.insert(i,ans)
    i=i+1
for a in range(len(MEENU)-1):
    print(MEENU[a] +" is now in the menu as the" + str(a) +"th item.")
