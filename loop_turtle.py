import turtle

t = turtle.Pen()
t.shape("turtle")
t.pencolor("blue")
t.speed("fast")

for x in range(5):
    t.forward(100)
    t.left(144)

turtle.done()