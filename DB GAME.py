
# simple card finding game

import turtle

## CARD
wn = turtle.Screen()
wn.title("CAVERN")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("THE CAVERN", align = "center", font=("Courier", 24, "normal"))

#moving pen down
i = 250
while pen.ycor() > 0:
    pen.sety(i)
    pen.write("THE CAVERN", align="center", font=("Courier", 24, "normal"))
    pen.penup()
    pen.hideturtle()
    pen.clear()
    pen.speed()
    pen._delay(20)
    i -= 10

## zoom screen
s = 24
while s < 72:
    pen.write("THE CAVERN", align="center", font=("Courier", s, "normal"))
    pen.penup()
    pen.hideturtle()
    pen.clear()
    pen.speed()
    pen._delay(40)
    s += 2

## final title card
pen.clear
pen.write("THE CAVERN", align="center", font=("Courier", 72, "normal"))

## slice line left

sliceline1 = turtle.Turtle()
sliceline1.pensize(3)
sliceline1.hideturtle()
sliceline1.color("yellow")
sliceline1.speed(5)
sliceline1.penup()
sliceline1.sety(0)
sliceline1.setx(0)

sliceline2 = turtle.Turtle()
sliceline2.pensize(3)
sliceline2.hideturtle()
sliceline2.color("yellow")
sliceline2.speed(5)
sliceline2.penup()
sliceline2.sety(0)
sliceline2.setx(0)

def slicelinego():
    sliceline1.pendown()
    sliceline2.pendown()
    sliceline1.showturtle()
    sliceline2.showturtle()
    sliceline1.goto(-300, 0)
    sliceline2.goto(300, 0)

slicelinego()



## Start button text
pen1 = turtle.Turtle()
pen1.hideturtle()
pen1._tracer(0)
pen1.color("white")
pen1.goto(0, -100)

## press start loop

pressed_space_once = 0

## ending all title screen

def clearscreen():
    pressed_space_once += 1

while pressed_space_once < 1:
    pen1.write("PRESS SPACE TO START", align="center", font=("Courier", 12, "normal"))
    pen1._delay(500)
    pen1.clear()
    pen1._delay(500)
    wn.listen()
    wn.onkeypress(clearscreen, "space")













# main game loop
while True:
    wn.update()

