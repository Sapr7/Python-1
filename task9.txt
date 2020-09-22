import turtle as t
import numpy as np
def f_g(a,b):
    k = np.sin(np.pi/(2*a))
    k = k * 2
    k = b / k
    k = k/ 2
    t.penup()
    t.forward(k)
    t.left(90-(180/a))
    t.pendown()
    for i in range(a):
        t.left(360/a)
        t.forward(b)
    t.right(90-(180/a))
    t.penup()
    t.backward(k)
for z in range(12):
    f_g(z+3,50+ 20*z)