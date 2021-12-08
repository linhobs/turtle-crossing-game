from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color('black')
        # start at initial position
        self.init_turtle()
        # we can just put x and y values from a tuple into a fxn, the tuple will unpack itself.

    def init_turtle(self):
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.penup()
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        # I could have just used self.forward(distance)

    # def move_up(self):
    #     self.forward(MOVE_DISTANCE)
