from ast import Break
from turtle import Screen
from food import Food
from snake import Snake
from score import Score
import time
import random

screen = Screen()
screen.setup(width= 600, height = 600)
screen.bgcolor("Black")
screen.bgpic("day20/sqe.png")
screen.title("My snake Game")
screen.tracer(0)
screen.colormode(255)
positionX=0

game_is_on = True
pressed = False
snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down , "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

# Checks for collision in each segment

def check_for_collision(cor):
    for segment in snake.segments:
        if round(segment.distance(cor), 2) <= 20:        
            segment.color("gray")
            return True   
    return False

# if any of segmens hit snake part restart loop from scratch with new coordinates

def collision_check_loop():
    """return save coordinates to spawn in"""
    hit = True
    cordinates = food.generate()
    while hit:
        hit = check_for_collision(cordinates)
        if hit == False:
            break
        cordinates = food.generate()
    return cordinates

while game_is_on:
 
    screen.update()
    time.sleep(0.1)

    snake.move_snake()
    snake.is_pressed = False
    
    # Detect collision with food and extend snake
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh(collision_check_loop())
        score.add_score()
        
    #Checks if head hit the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
        
    # detects if snake hits it's self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
    
screen.exitonclick()