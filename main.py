from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.update()
    snake.move()

# Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.eat()
        snake.extend()

# Detect collision with wall
    x = snake.head.xcor()
    y = snake.head.ycor()
    if x > 290 or x < -290 or y > 290 or y < -290:
        game_is_on = False
        scoreboard.over()

# Detect collision with tail
# if the head collides with any segment in the tail
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.over()


screen.exitonclick()
