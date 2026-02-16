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


def draw_spirogram(tilt_angle):
    timmy.speed("fastest")
    angle = int(360/tilt_angle)
    for _ in range(angle):
        timmy.color(random_color())
        timmy.circle(80)
        timmy.setheading(timmy.heading() + tilt_angle)


draw_spirogram(3)
screen.exitonclick()
