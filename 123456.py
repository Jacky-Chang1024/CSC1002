# import package
import turtle

turtle.tracer(False)

# method for key call
def fxn():
    
	t.forward(40)
    # return t.pos()
    # print(t.pos())
    # turtle.pos()
    # print(x)


# set turtle screen size
sc=turtle.Screen()
sc.setup(600,300)

# motion
# turtle.forward(40)


t = turtle.Turtle()


def move():
    # global sc
    fxn1()
    print(t.pos())
    sc.update()
    sc.ontimer(move,1000)


# call method on Right key
def fxn1():
    sc.onkey(fxn,'Right')
    # print(fxn())  
    # sc.ontimer(fxn,300)

# fxn1()

move()

# to listen by the turtle
sc.listen()
sc.mainloop()