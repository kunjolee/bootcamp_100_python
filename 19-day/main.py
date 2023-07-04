# Higher order functions in python are the functions that can work with other functions inside of it

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()