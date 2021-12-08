import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        # add to list so that we can move each car individually
        # creating on each instance doesn't move the cars, it gets confused as to which instance to confused
        # to get all the states, put them in a list and move each.
        # think in terms of this.
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # create a car and append to cars list
    def create_car(self):
        # using inheritance will cause issues so we'll use just the turtle
        # generate cars randomly
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            y_value = random.randint(-250, 250)
            x_value = 300
            new_car.penup()
            new_car.goto(x_value, y_value)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
