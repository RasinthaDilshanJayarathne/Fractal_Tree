from email import message
import turtle
import sys, time, os

message = "Hello Mother F####"

def typewritter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(0.1)
        else:
            time.sleep(1)

os.system("cls")
typewritter(message)

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")
t.shape("turtle")
t.color("white","white")
t.left(90)
t.forward(40)
t.right(90)
t.circle(40,90)
t.forward(80)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.right(180)
t.forward(80)
t.circle(20,180)
t.forward(80)
t.right(180)
t.circle(20,180)
t.forward(80)
t.right(180)
t.penup()
t.forward(40)
t.pendown()
t.circle(20,180)
t.left(50)
t.forward(50)
t.right(50)
t.circle(40,90)
t.right(90)
t.forward(40)
t.left(90)
t.forward(80)

turtle.done()