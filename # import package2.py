# import package
import turtle

# methods with different work
# at different keys
def fxn():
	tim.forward(20)
	
def fxn1():
	tim.right(90)

def fxn2():
	tim.left(90)



tim = turtle.Turtle()

# set screen size
sc=turtle.Screen()
sc.setup(500,300)


turtle.mainloop()
# call methods
turtle.onkey(fxn,'space')
turtle.onkey(fxn1,'Right')
turtle.onkey(fxn2,'Left')

# to listen by the tim
turtle.listen()
# tim.mainloop()