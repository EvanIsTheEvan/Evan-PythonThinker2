students=[]
student1=["John","67894903","Hockey"]
student2=["Tom","25348033","Badminton"]
student3=["Timothy","36728193","Soccer"]
students.append(student3)
students.append(student2)
students.append(student1)


name,phonenumber,CCA = student1
for student in students:
    print("Name:"+ str(name))
    print("Phone Number:"+ str(phonenumber))
    print("CCA:"+ str(CCA))