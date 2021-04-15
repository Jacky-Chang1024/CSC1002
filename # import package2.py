# import package
import turtle

# methods with different work
# at different keys
def fxn():
	turtle.forward(20)
	
def fxn1():
	turtle.right(90)

def fxn2():
	turtle.left(90)
	
# set screen size
sc=turtle.Screen()
sc.setup(500,300)

# call methods
turtle.onkey(fxn,'space')
turtle.onkey(fxn1,'Right')
turtle.onkey(fxn2,'Left')

# to listen by the turtle
sc.listen()
turtle.mainloop()