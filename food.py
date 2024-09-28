from turtle import Turtle
import random

class Food(Turtle): #food class
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.25,0.25)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

#Method to make the food appear in a random position in the screen
    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)