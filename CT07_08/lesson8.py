# fruits=["Apple","Banana","Cherry","Durian","Elderberry","Figs"]
# index=len(fruits)//2
# left=print(fruits[:index])
# right=print(fruits[index:])


# fruits=["Apple","Banana","Cherry","Durian",]
# fruits2=["Cherry","Durian","Elderberry","Figs"]
# common=[]
# for i in fruits:
#     if i in fruits:
#         if i in fruits2:
#             common.append(i)

# print(common)


# fruits=["Apple","Banana","Cherry","Durian",]
# fruits2=["Cherry","Durian","Elderberry","Figs"]
# fruitz=fruits+fruits2
# unique=[]
# for i in fruitz:
#     if i in fruits and not i in fruits2:
#         unique.append(i)
#     if i in fruits2 and not i in fruits:
#         unique.append(i)        
# print(unique)

# num=[1,2,3,4,]
# num2=[5,6,7,8]
# numz=num+num2
# even=[]
# for i in numz:
#     if i % 2 == 0:
#         even.append(i)
# print(even)

# list1 = [3, 2, 1]
# list2 = [6, 5, 5]
# list3 = [9, 8, 7]
# list69= list1+list2+list3
# list420=[]
# for i in list69:
#     if not i in list420:
#         list420.append(i)
# list420=sorted(list420)
# list220=slice(len(list420)//2)
# list221=slice(len(list420)//2,len(list420))
# print (list420[list220])
# print (list420[list221])

# string=(input("What is your selected password?"))
# hasupper=False
# haslower=False
# hasdigit=False
# hasalnum=False
# if len(string)>7:
#     for char in string:
#         if char.isupper:
#             hasupper=True 
#         if char.islower:
#             haslower=True
#         if char.isdigit:
#             hasdigit=True
#     if string.isalnum:
#             hasalnum=True
#     if hasupper==True:
#         if haslower==True:
#             if hasdigit==True:
#                 if hasalnum==True:
#                     print("DA PASSWORD IS VALID!")
#                 else:
#                     print("INVALID!")


# text=input("Sentence:")
# alt = True
# output=""

# for i in text:
#     if alt == True:
#         output += i.upper()
#         alt=False
#     else:
#         output += i.lower()
#         alt=True

# print(output)

# string = "Computers empower our modern world with their digital brains."
# string=string.split()
# print(string)

# string = "Computers,empower,our,modern,world,with,their,digital,brains."
# string=string.split(",")
# print(string)

# list=['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']
# string= " ".join(list)
# print(string)

# list=['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']
# string= ",".join(list)
# print(string)

# string = "Hello World"

# string=string.split()
# for i in string:
#     i=i[::-1]
#     string=" ".join(i)
# print(string)

# word = "radar"
# is_pakljdsaiushdfuiabchjrbyfsedjbuh2q498ewufaIjd = word == word[::-1]
# print("Input: "+word[::1])
# print("Output: "+str(is_pakljdsaiushdfuiabchjrbyfsedjbuh2q498ewufaIjd))

# while True:
#     word = input("Gimme a word.")
#     if word == "end":
#         break
#     is_pakljdsaiushdfuiabchjrbyfsedjbuh2q498ewufaIjd = word == word[::-1]
#     print("Input: "+word[::1])
#     print("Output: "+str(is_pakljdsaiushdfuiabchjrbyfsedjbuh2q498ewufaIjd))


# poolendroms=0
# pillendrems=[]
# string = input("Gimme a sentence")
# string=string.split()
# for i in string:
#     is_pakljdsaiushdfuiabchjrbyfsedjbuh2q498ewufaIjd = i == i[::-1]
#     if is_pakljdsaiushdfuiabchjrbyfsedjbuh2q498ewufaIjd == True:
#         poolendroms=poolendroms+1
#         pillendrems.append(i)
# print(poolendroms)
# print(pillendrems)

# sales_data = [
#     ["Appel",50,1.99],
#     ["Banana",45,0.99],
#     ["Orange",30,2.49],
#     ["Grapefruit",25,3.99],
#     ["Mango",20,2.99]
# ]

# sorted_earned=[]
# earned=[]

# for fruits in sales_data:
#     fruit, sold, price = fruits
#     earned.append(sold*price)

# earned.sort()
# print(earned)




# hacking101=[
#     ["SUSSYAMONGUS3487289","5NightsAtDiddy's","Lemonsquezzer.com"],
# ]
# whatuwantbro=input("What do you want to do with the terminal? Choose Add, Search, Display or Quit.")
# while not whatuwantbro=="Quit":
#     if whatuwantbro == "Add":
#         whichpassword=input("Which website's password do you want to edit")
#         for i in hacking101:
#             User,Pass,URL=i
#             if URL == whichpassword:
#                 addpasswerd=input("What do you want to add to the password?")
#                 i.append(addpasswerd)
#     if whatuwantbro =="Search":
#         whichsearch=input("Which website's password do you want to search")
#         for i in hacking101:
#             User,Pass,URL=i
#             if URL == whichsearch:
#                 searchwut=("")
