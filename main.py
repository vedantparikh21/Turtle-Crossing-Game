import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(player.move,'Up')

car = CarManager()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.generate_car()
    car.move()

    if player.ycor() > 290:
        scoreboard.clear()
        screen.update()
        scoreboard.increase_level()
        player.goto(0,-280)
        car.increase_speed()

    # check collision
    for i in car.cars:
        if player.distance(i) < 24:
            print('Game Over')
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

