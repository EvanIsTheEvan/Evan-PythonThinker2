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

import random
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

BANNANABO=t.Turtle()
BANNANABO.penup()
BANNANABO.seth(90)
BANNANABO.shape("turtle")
BANNANABO.color("#9A3836")
BANNANABO.goto(0,-250)
BANNANABO.write("BANNANABO",align="center",font=('Arial,20'))
BANNANABO.seth(random.randint(75,115))
BANNANABO.forward(random.randint(1,20))

SIGMAMAN7293=t.Turtle()
SIGMAMAN7293.penup()
SIGMAMAN7293.seth(90)
SIGMAMAN7293.shape("turtle")
SIGMAMAN7293.color("#9A3836")
SIGMAMAN7293.goto(200,-250)
SIGMAMAN7293.write("SIGMAMAN7293",align="center",font=('Arial,20'))
SIGMAMAN7293.seth(random.randint(75,115))
SIGMAMAN7293.forward(random.randint(1,20))

RIZZMAX2382=t.Turtle()
RIZZMAX2382.penup()
RIZZMAX2382.seth(90)
RIZZMAX2382.shape("turtle")
RIZZMAX2382.color("#9A3836")
RIZZMAX2382.goto(-200,-250)
RIZZMAX2382.write("RIZZMAX2382",align="center",font=('Arial,20'))
RIZZMAX2382.seth(random.randint(75,115))
RIZZMAX2382.forward(random.randint(1,20))

guess=input("WHO DO YOU TINK WILL WEEN?")


window.mainloop()
