from turtle import Turtle, Screen
import random

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color('red')
        self.speed('fastest')
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
    
    def move(self) -> None:
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
        # method to place food randomly on the screen
    