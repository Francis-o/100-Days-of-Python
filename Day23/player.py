from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.update_player()
        
    def update_player(self):
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("black")
        self.goto(STARTING_POSITION)
    
    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
