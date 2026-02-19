from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.create_paddle(x_cord, y_cord)

    def create_paddle(self, x_cord, y_cord):
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x_cord, y_cord)
    
    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)