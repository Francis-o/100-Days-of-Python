from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.update_score()

    def update_score(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-100, 200)
        self.clear()
        self.write(self.left_score, move=False, align='center', font=('Arial', 70, 'normal'))
        self.goto(100, 200)
        self.write(self.right_score, move=False, align='center', font=('Arial', 70, 'normal'))
    
    def point_right(self):
        self.right_score += 1
    
    def point_left(self):
        self.left_score += 1

