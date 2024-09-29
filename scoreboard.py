from turtle import Turtle

class ScoreBoard(Turtle): #by using inheritance to create a scoreboard using turtle module
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_scoreboard()

    #method to increase the scoreboard
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    #method to update the scoreboard incase in keep stacking to the others
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}" , align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    #method to show that the game is over when we lose
    # def game_over(self):
    #     self.hideturtle()
    #     self.penup()
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align="center", font=("Arial", 24, "normal") )