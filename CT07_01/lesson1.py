

#make glass box
#make paper box
#make plastic box

#repeat until 0 items
#if item is glass then
    #put in glass
#if not, check if item is plastic
    #put in plastic
#if not, put in paper


Red = int(input("How many red plates are there?")*1)
Blue = int(input("How many blue plates are there?")*2)
Green = int(input("How many green plates are there?")*3)
Ans = Red + Blue + Green
print (Ans)