#First import all the modules that are created in this files
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen() #Use to load the Screen! By using Screen Class in turtle module
screen.setup(width=600,height=600) #setup resolution, background color etc.
screen.bgcolor("black")
screen.title("SNAKEEEEEEEEEEEEE!!!!")
screen.tracer(0) #Manage animation speed

snake = Snake() #making a snake
food = Food() #making a food
scoreboard = ScoreBoard() #making a scoreboard

screen.listen() #use event listener to control the snake movement
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#making a while loop so the game will continue to run when game_is_on is set to True
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move() #making the snake move

    #Detect collision with food
    if snake.head.distance(food) < 8:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset()
        scoreboard.reset()

    #Detect collision with tail
    #Apply slicing so it will not loop through the [0] of the snake!
    for body in snake.snake_body[1:]:
        if snake.head.distance(body) < 7:
            snake.reset()
            scoreboard.reset()


#prevent screen automatically close whenever we run the code
screen.exitonclick()