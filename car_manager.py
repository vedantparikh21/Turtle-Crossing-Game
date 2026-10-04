from turtle import Turtle
from scoreboard import Scoreboard
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3

score = Scoreboard()

class CarManager():
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.cycle = 1
        self.probability = 6
        self.generate_car()

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def reset_cars(self):
        self.cars = []
        if score.score % 6 == 0:
            self.probability -= 1

    def generate_car(self):
        if random.randint(1,self.probability) == 1: # randomness to control the speed of generation for the cars
            car = Turtle()
            car.pu()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2)
            random_y = random.randint(-270,260)
            car.goto(315,random_y)
            car.setheading(180)
            self.cars.append(car)
