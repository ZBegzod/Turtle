import time
import turtle
import random

delay = 0.1
score = 0
high_score = 0

screen = turtle.Screen()
screen.title('Snake game')
screen.bgcolor("blue")

screen.setup(width=600, height=600)
screen.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.d = "Stop"

# food in the game
food = turtle.Turtle()
random_color = random.choice(["red", "green", "black"])
random_shape = random.choice(["square", "triangle", "circle"])
food.speed(0)
food.shape(random_shape)
food.color(random_color)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
# pen.shape()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)

pen.write(
    "Score: 0 High Score 0", align="center",
    font=("candra", 24, "bold")
)


# assign ds
def go_up():
    if head.d != "down":
        head.d = "up"


def go_down():
    if head.d != "up":
        head.d = "down"


def go_left():
    if head.d != "right":
        head.d = "left"


def go_right():
    if head.d != "left":
        head.d = "right"


def move():
    if head.d == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.d == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.d == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.d == "right":
        x = head.xcor()
        head.setx(x + 20)


screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

segments = []

while True:
    screen.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < - 290:
        time.sleep(1)
        head.goto(0, 0)
        head.d = "Stop"
        random_color = random.choice(['red', 'blue', 'green'])
        random_shape = random.choice(['square', 'circle'])

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0
        delay = 0.1

        pen.clear()
        pen.write("Score : {} High Score : {}".format(
            score, high_score), align="center", font=("candra", 24, "bold"))

    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # adding new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {} High Score : {}".format(
            score, high_score), align="center", font=("candra", 24, "bold")
        )

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.d = "Stop"
            random_color = random.choice(['red', 'blue', 'green'])
            random_shape = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))

    time.sleep(delay)

screen.mainloop()
