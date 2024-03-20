import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")
car_manager = CarManager()
score = Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    # detect collision with car
    for car in car_manager.all_car:
        if car.distance(player) < 25:
            score.gameover()
            game_is_on = False
            screen.exitonclick()
    # detect successful crossing
    if player.is_at_finish_line():
        score.level_up()
        car_manager.level_up()







