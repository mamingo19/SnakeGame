from turtle import Turtle

class ScoreBoard(Turtle): #by using inheritance to create a scoreboard using turtle module
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_scoreboard()

    #method to increase the scoreboard
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    #method to update the scoreboard incase in keep stacking to the others
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    #method to show that the game is over when we lose
    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=("Arial", 24, "normal") )