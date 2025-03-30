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
BANNANABOI3456.seth(90)
BANNANABOI3456.shape("turtle")
BANNANABOI3456.color("#9A3836")
BANNANABOI3456.goto(0,-250)
BANNANABOI3456.write(align="center",font=('Arial,20'))

SIGMAMAN7293=t.Turtle()
pen.penup()
SIGMAMAN7293.seth(90)
SIGMAMAN7293.shape("turtle")
SIGMAMAN7293.color("#9A3836")
SIGMAMAN7293.goto(200,-250)
SIGMAMAN7293.write(align="center",font=('Arial,20'))

RIZZMAX2382=t.Turtle()
pen.penup()
RIZZMAX2382.seth(90)
RIZZMAX2382.shape("turtle")
RIZZMAX2382.color("#9A3836")
RIZZMAX2382.goto(-200,-250)
RIZZMAX2382.write(align="center",font=('Arial,20'))
window.mainloop()