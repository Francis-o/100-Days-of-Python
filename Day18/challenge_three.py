from turtle import Turtle, Screen, colormode
import random

colormode(255)
screen = Screen()
timmy = Turtle()

#draws square up to a decogon
def draw_shape(sides):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.color(r, g, b)
    for i in range(sides):
        angle = 360/sides
        timmy.left(angle)
        timmy.forward(100)

for sides in range(3, 11):
    draw_shape(sides)


screen.exitonclick()