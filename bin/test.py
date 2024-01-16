import turtle as t
Pen1 = t.Pen()
Pen1.pencolor("red")
Pen1.pensize(3)
for i in range(3):
    for j in range(2):
        Pen1.forward(100)
        Pen1.left(90)
        Pen1.forward(200)
        Pen1.left(90)
    Pen1.left(120)
Pen1.hideturtle()
t.done()