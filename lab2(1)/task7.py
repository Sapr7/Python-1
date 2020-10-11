import turtle as t
def Spiral():
	r=10
	t.pendown()
	for i in range(300):
		t.forward(0.03*5*(r*r+1)**0.5)
		t.left(5)
		r=r+0.03*5
	t.stamp()
	t.penup()
Spiral()