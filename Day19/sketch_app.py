from turtle import Turtle, Screen



def move_forawrd():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_right():
    tim.right(5)

def turn_left():
    tim.left(5)

def clear_drawing():
    tim.reset()

screen = Screen()
tim = Turtle()

screen.listen()
screen.onkey(move_forawrd, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear_drawing, "c")

screen.exitonclick()