from turtle import Turtle, Screen, colormode
import random

colormode(255)

screen = Screen()
timmy = Turtle()
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_move():
    timmy.color(random_color())
    angles = [90, 180, 270, 360]
    angle = random.choice(angles)
    timmy.speed("fastest")
    timmy.pensize(10)
    timmy.forward(20)
    timmy.setheading(angle)

for _ in range(1000):
    random_move()

screen.exitonclick()