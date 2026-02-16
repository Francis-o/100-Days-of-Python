from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()

#draw square
for i in range(4):
    timmy.forward(100)
    timmy.right(90)


screen.exitonclick()