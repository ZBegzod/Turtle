import turtle

sc = turtle.Screen()

pen = turtle.Turtle()


def semi_circle(color, radius, x):
    pen.color(color)
    pen.circle(radius, -180)

    pen.penup()
    pen.setposition(x, 0)

    pen.down()
    pen.right(180)


color = [
    'violet', 'indigo', 'blue',
    'green', 'yellow', 'orange', 'red'
]

sc.setup(600, 600)
sc.bgcolor('black')

pen.right(90)
pen.width(10)

for i in range(7):
    semi_circle(color[i], 10 * (i + 8), -10 * (i + 1))

turtle.exitonclick()
