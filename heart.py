import turtle

turtle.bgcolor("black")
t = turtle.Turtle()

turtle.speed(-5)
t.color("white")
t.begin_fill()
t.fillcolor("red")


t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

t.write("I love you, MOM", 'false', 'center', font=('Showcard gothic', 40))
turtle.exitonclick()
