import turtle

s = turtle.getscreen()
s.bgcolor("#FFCE30")
s.setup(500, 500)
t = turtle.Turtle()

"""zed letter"""
# t.forward(200)
# t.left(40)

# t.right(40)
# t.forward(200)

"""equilateral triangle"""
# t.forward(100)
# t.lt(120)
# t.forward(100)
# t.lt(120)
# t.forward(100)


"""right angle triangle """
t.rt(180)
t.forward(150)
t.rt(90)
t.forward(200)
t.rt(143)
t.forward(250)

"""an acute-angled triangle"""
# t.lt(10)
# t.forward(150)
# t.lt(120)
# t.forward(100)
# t.lt(100)
# t.forward(140)


# t.forward(100)
# t.lt(150)
# t.forward(150)
# t.lt(140)
# t.forward(90)

# t.undo()
# turtle.done
turtle.exitonclick()
