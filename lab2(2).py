'''task1'''


import turtle as t
from random import randint
def cherepaha(i):
	for i in range(n):
		t.forward(randint(5,30))
		t.left(randint(0,360))
		t.forward(randint(10,40))
n=100
cherepaha(n)


'''task 5'''


from random import randint
import turtle


number_of_turtles = 20
steps_of_time_number = 100


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.setheading(randint(0,360))
        unit.forward(randint(-60,60))


'''task4'''
import turtle as t
x=0
y=0
Vx=5
Vy=10
ay=-0.5
dt=0.06
for i in range(10000):
	t.goto(x,y)
	x+=Vx*dt
	y+=Vy*dt+ay*dt**2/2
	Vy+=ay*dt
