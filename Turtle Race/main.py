from turtle import Turtle, Screen
import random
is_race = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-75, -50, -25, 0, 25, 50]
all_racers = []

screen = Screen()

screen.setup(width=500, height=400)

for t_in in range(0,6):
    turt = Turtle(shape="turtle")
    turt.color(colors[t_in])
    turt.penup()
    turt.goto(x=-240, y=y_positions[t_in])
    all_racers.append(turt)

user_bet = screen.textinput(title="Place your bet!", prompt="Which turtle will win the race? Enter its colour: ")

if user_bet:
    is_race = True

while is_race:
    for t in all_racers:
        if t.xcor() > 230:
            is_race = False
            winner = t.pencolor()
        
            if winner == user_bet.lower():
                print(f"You won! The {winner} turtle is the winner!")
            else:
                print(f"You lost.. The {winner} turtle is the winner..")
        
        rand_dist = random.randint(0, 10)
        t.forward(rand_dist)

screen.exitonclick()
