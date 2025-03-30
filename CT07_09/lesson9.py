# IDIOTRESPONSE=input("What has to be broken before you can use it?")
# isCorrect=False
# IDIOTRESPONSELOWER=IDIOTRESPONSE.lower()
# IDIOTRESPONSESPLITTED= IDIOTRESPONSELOWER.split()
# for i in IDIOTRESPONSESPLITTED:
#     if i == "egg":
#         isCorrect=True
# if isCorrect==True:
#     print("NOT BAD YOU IDIOT...")
# else:
#     print("I KNEW IT YOU FAILED!")

# print(IDIOTRESPONSE)

# import turtle as t

# window=t.Screen()
# window.setup(width=969, height=696)
# window.bgcolor("forestgreen")
# window.mainloop()

import turtle as t

window=t.Screen()
window.setup(width=696,height=696)
window.bgcolor("forestgreen")

pen=t.Turtle()
pen.penup()
pen.shape("square")
pen.sety(250)
for i in range(-696,696,25):
    pen.setx(i)
    pen.stamp()
pen.goto(-350,-250)
pen.color("yellow")
pen.pendown()
pen.seth(0)
pen.forward(696)
pen.hideturtle()

BANNANABOI3456=t.Turtle()
pen.penup()
BANNANABOI3456

window.mainloop()