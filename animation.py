import turtle

turtle.bgcolor("black")
screen = turtle.Screen()
screen.title('Animation Circle')

pen = turtle.Turtle()
pen.color("red")
pen.speed(0)

pen.hideturtle()

for i in range(100):
    pen.circle(i * 2)
    pen.left(5)

turtle.exitonclick()
