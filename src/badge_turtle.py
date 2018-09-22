import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.begin_poly()
for i in range(6):
    tina.forward(100)
    for j in range(10):
        tina.left(6)
        tina.forward(1)
tina.end_poly()

p = tina.get_poly()

print(p)

