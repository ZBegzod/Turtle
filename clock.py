import time
import turtle
import datetime as dt

t1 = turtle.Turtle()

t2 = turtle.Turtle()

screen = turtle.Screen()

screen.bgcolor("green")

t1.pensize(3)
t1.color('black')

t1.penup()
t1.goto(-20, 0)
t1.pendown()

for i in range(2):
    t1.forward(200)
    t1.left(90)
    t1.forward(70)
    t1.left(90)

t1.hideturtle()

second = dt.datetime.now().second
minute = dt.datetime.now().minute
hour = dt.datetime.now().hour

t2.hideturtle()
while True:
    t2.clear()

    t2.write(
        str(hour).zfill(2) + ":" +
        str(minute).zfill(2) + ":" +
        str(second).zfill(2),
        font=("Arial Narrow", 35, "bold")
    )

    time.sleep(1)
    second += 1

    if second == 60:
        second = 0
        minute += 1

    if minute == 60:
        minute = 0
        hour += 1

    if hour == 24:
        hour = 1

turtle.exitonclick()
