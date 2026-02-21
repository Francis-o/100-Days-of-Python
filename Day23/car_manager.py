from turtle import Turtle,  colormode
import random

colormode(255)
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.spawn_cars()
        self.speed_incre = -5
    
    def create_car(self, x_cord,  y_cord):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        r = random.randint(0, 250)
        g = random.randint(0, 250)
        b = random.randint(0, 250)
        new_car.color(r, g, b)
        new_car.goto(x_cord, y_cord)
        self.cars.append(new_car)
    
    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() + self.speed_incre, car.ycor())

    def spawn_cars(self):
        for _ in range(10):
            x_cord = random.randint(150, 1000)
            y_cord = random.randint(-250, 250)
            self.create_car(x_cord, y_cord)

    def random_spawn(self):
        num = random.randint(1, 4)
        if num == 2:
            x_cord = random.randint(300, 600)
            y_cord = random.randint(-250, 250)
            self.create_car(x_cord, y_cord)
    
    def new_level(self):
        self.spawn_cars()
        self.speed_incre -= 5