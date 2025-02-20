from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
game_is_on = True

snake = Snake()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()