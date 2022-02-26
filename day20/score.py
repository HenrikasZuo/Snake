from mimetypes import init
from select import select


from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = self.save_score()
        self.penup()
        self.pencolor("white")
        self.ht()
        self.goto(0, 250)
        self.generate_board()
    
    def generate_board(self):
        """generates and updates text element"""
        self.clear()
        self.write(f"Current score: {self.score} High score: {self.high_score}", move=False, align="center", font=("Arial", 18, "normal"))
    
    def add_score(self):
        self.score += 1
        self.generate_board()
           
    def reset(self):
        """resets everything after death"""
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score()
        self.score = 0
        self.generate_board()
        
    def save_score(self):
        with open('day20/save.txt') as data:
            return int(data.read())
    
    def write_score(self):
        with open('day20/save.txt', mode="w") as data:
            data.write(f"{self.high_score}")
