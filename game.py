import turtle
import random

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)

player_two = player_one.clone()
player_two.penup()
player_two.goto(-200, -100)

player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

die = [1, 2, 3, 4, 5, 6]

for i in range(20):
    if player_one.pos() >= (200, 100):
        print("Player one wins!")
        break
    elif player_two.pos() >= (200, -100):
        print("Player two wins!")
        break
    else:
        player_one_turn = input("Press enter to roll the die")
        die_outcome = random.choice(die)
        print(die_outcome)
        print("the number of steps will be")
        print(20 * die_outcome)
        player_one.forward(20 * die_outcome)

        player_two_turn = input("Press enter to roll the die")
        die_outcome = random.choice(die)
        print("the result of the dia roll is:")
        print(die_outcome)
        print("the number of steps will be")
        print(20 * die_outcome)
        player_two.forward(20 * die_outcome)
