from turtle import Screen, Turtle
import time

class Snake:
    
    def __init__(self) -> None:
        self.segment = []
        for i in range(3):
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.setx(-20*i)
            self.segment.append(new_segment)
        self.head = self.segment[0]

    def extend(self):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(self.segment[-1].position())
        self.segment.append(new_segment)
    
    def move(self) -> None:
        for i in range(len(self.segment) - 1,0,-1):
            new_x = self.segment[i-1].xcor()
            new_y = self.segment[i-1].ycor()
            self.segment[i].goto(new_x,new_y)
        self.segment[0].forward(20)

    def left(self) -> None:
        self.segment[0].setheading(180)

    def right(self) -> None:
        self.segment[0].setheading(0)

    def up(self) -> None:
        self.segment[0].setheading(90)

    def down(self) -> None:
        self.segment[0].setheading(270)