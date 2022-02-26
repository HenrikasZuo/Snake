from turtle import Turtle, distance
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7,stretch_wid= 0.7)
        self.color("goldenrod")
        self.speed(0)
        self.goto(self.generate())
        self.go_again = False
        
    def refresh(self, cor):
        """spawns food element in given position"""
        self.goto(cor)
        
    def generate(self):
        """Generates new food in bound of screen"""
        x = (random.randint(-280, 280) // 20) *  20
        y = (random.randint(-280, 280) // 20) *  20
        return (x, y)