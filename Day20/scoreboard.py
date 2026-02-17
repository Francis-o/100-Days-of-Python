from turtle import Turtle

FONT = ('Arial', 20, 'normal')
ALIGNMENT =  "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.show_score()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)