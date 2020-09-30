import turtle as t
import numpy as np
t.speed(100)
t.left(90)
def okr1(a):
    for i in range (360):
        t.forward(a)
        t.left(1)
def okr2(a):
    for i in range (360):
        t.forward(a)
        t.right(1)
for i in range (10):
    okr1(i)
    okr2(i)