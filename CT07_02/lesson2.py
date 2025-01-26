# print("Hello from lesson 2")
# # print("Hi")
# num1 = input("Give me a number")
# print(num1)

question_answer = ["IDK","2","4"]



answr="erfghjjjjjjjjjjjjjjjjmdsssss"
attempts = 0
while True:
    while answr != question_answer[0] :
        answr = input("What is the mass of the sun?")
        attempts+=1
        if attempts>3:
            break
    print("CORRECT")
    while answr != question_answer[1] :
        answr = input("What is 1+1")
        attempts+=1
        if attempts>3:
            break
    print("CORRECT")
    while answr != question_answer[2] :
        answr = input("What is 2+2")
        attempts+=1
        if attempts>3:
            break
    print("CORRECT")
    break