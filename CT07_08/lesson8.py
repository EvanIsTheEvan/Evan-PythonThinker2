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

string=""
hasupper=False
if len(string)>7:
    for char in string:
        if char.isupper:
            hasupper=True 
        if char.islower:
            haslower=True
