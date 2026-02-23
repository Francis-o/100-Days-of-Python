from turtle import Turtle

FONT = ('Arial', 20, 'normal')
ALIGNMENT =  "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.check_highscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.show_score()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_highscore()
        self.score = 0

    def update_score(self):
        self.score += 1

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
    
    def check_highscore(self):
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        
    def update_highscore(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))