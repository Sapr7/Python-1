import turtle as t
import numpy as np
t.speed(100)
t.left(90)
def okr1():
    for i in range (180):
        t.forward(1)
        t.left(1)
def okr2():
    for i in range (180):
        t.forward(0.25)
        t.left(1)
for i in range(5):
    okr1()
    okr2()