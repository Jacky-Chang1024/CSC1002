import turtle
turtle.tracer(False)
def f():
    global t
    t = turtle.Turtle(shape='square')
    t.fd(21)
    t.stamp()
    # t.clearstamps()

def f1():
    t.clearstamps()
    
def F():
    f()
    # f1()
    print('good')
    print(t.pos())
    turtle.ontimer(F,500)
    turtle.update()


F()
turtle.mainloop()