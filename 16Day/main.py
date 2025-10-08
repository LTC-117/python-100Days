from turtle import Turtle, Screen
import turtle

turtle.bgcolor('black')

timmy = Turtle()
timmy.shape("turtle")
timmy.color("white")

for x in range (90):
    timmy.forward(4)
    timmy.left(4)

for x in range (90):
    timmy.forward(4)
    timmy.right(4)

my_screen = Screen()
my_screen.exitonclick()
