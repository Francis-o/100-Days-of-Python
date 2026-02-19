from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Pong")
screen.bgcolor("black")
screen.listen()

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

game_on = True
while game_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Detect when ball misses paddle
    if ball.xcor() > 380:
        scoreboard.point_left()
        ball.reset_position()

    elif ball.xcor() < -380:
        scoreboard.point_right()
        ball.reset_position()
    scoreboard.update_score()
  


screen.exitonclick()