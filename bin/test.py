import turtle as t
s = t.Pen()
s.pencolor("green")
s.pensize(10)
length = [60*2,100*2,140*2]
s.left(180/3)
for i in range(3):
    for j in range(3):
        s.forward(length[i])
        s.left(180-60)
s.hideturtle()
t.done()