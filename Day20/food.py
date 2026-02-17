from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        self.x_cord = random.randint(0, 270)
        self.y_cord = random.randint(0, 270)
        self.goto(self.x_cord, self.y_cord)
    
