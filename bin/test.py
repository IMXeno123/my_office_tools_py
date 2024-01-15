import turtle as t
s = t.Pen()
s.pencolor("green")
s.pensize(10)
j = 60
s.left(60)
for i in range(3):
    for k in range(3):
        s.forward(j)
        s.left(120)
    j += 40
s.hideturtle()
t.done()