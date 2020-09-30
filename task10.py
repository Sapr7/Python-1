import turtle as t
import numpy as np
t.speed(100)
def okr():
    for i in range (360):
        t.forward(1)
        t.left(1)
for i in range (6):
    okr()
    t.left(60)