import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
car_manager.spawn_cars()

#player movement
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.random_spawn()
    car_manager.move_cars()

    #Reset player if y cord greater than 300
    if player.ycor() > 300:
        player.update_player()
        scoreboard.next_level()
        car_manager.new_level()

    # check for collision
    for car in car_manager.cars:
        if player.distance(car) <= 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()