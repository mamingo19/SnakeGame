from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-5,0),(-10,0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#snake class which has snake_body[] a list to store the body of the snake
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

#method to create a snake first of all the snake will have a length of 3
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake_body(position)

    # method to adding up snake body, this method use in whenever the snake have collision with the food it will run this method
    def add_snake_body(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.shapesize(0.5, 0.5)
        snake.goto(position)
        self.snake_body.append(snake)

# method to adding up snake body, in the tail of the snake
    def extend(self):
        self.add_snake_body(self.snake_body[-1].position())

#this is method for the snake movement
#because imagine we will have a snake that have the length of 6
#so we have a list [0,1,2,3,4,5]
#this will help the snake movement that make the [0] move to the location we want and [1] will move to [0]
#[2] will move to [1] etc! make the snake will always look like a snake! lol
    def move(self):
        for snake_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake_num - 1].xcor()
            new_y = self.snake_body[snake_num - 1].ycor()
            self.snake_body[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

#note: in this keybind method I also implement the constraint that the snake cannot move backward
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)