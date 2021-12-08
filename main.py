import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_up, 'Up')
loop_run = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # put all cars in a list and move each one of them
    car_manager.create_car()
    car_manager.move_cars()
    # detect collision with cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    #     detect when player reaches the end of the road
    if player.ycor() >= 280:
        # increase score
        scoreboard.increase_level()
        player.init_turtle()
        car_manager.increase_speed()

screen.exitonclick()
#todo : allow replay again on some key press (we run out of time)