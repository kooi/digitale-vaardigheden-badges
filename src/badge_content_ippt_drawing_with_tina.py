import turtle
import random
tina = turtle.Turtle()
tina.shape('turtle')

#tina.begin_poly()
#for i in range(6):
#    tina.forward(100)
#    for j in range(10):
#        tina.left(6)
#        tina.forward(1)
#tina.end_poly()
#p = tina.get_poly()

for i in range(300):
    tina.forward( random.randint(0, 10) )
    tina.right( random.randint(-180, 180) )


#tina.forward(60)
#tina.left(110)
#tina.forward(65)
#tina.left(30)
#tina.forward(65)
#tina.left(230)
#
#for i in range(40):
#    tina.left(4)
#    tina.forward(1)
#tina.forward(30)



#print(p)
