import turtle
import random   

def configure_snake():
    snake = turtle.Turtle(shape='square')
    snake.color('red')
    snake.pu()
    return snake



def snake_move():
    global g_snake
    s = g_snake
    xx=[20,-20,0,0,0]
    yy=[0,0,20,-20,0]
    moveKey = ['Right','Left','Up','Down','space']
    
    for i in range(5):
        turtle.onkey( g_snake = lambda s : s.setheading(s.xcor()+xx[i],s.ycor()+yy[i]) , moveKey[i])
    turtle.onkey(move_down(),'Down')
    # g_snake =  s.onkey(move_left(),'Left')
    # g_snake =  s.onkey(move_right(),'Right')
    # g_snake =  s.onkey(move_pause(),'space')
    # g_snake = move_orientation(g_snake,i,j)

def move_down():
    g_snake.fd(23)

g_snake = configure_snake()
snake_move()
g_snake.listen()
turtle.mainloop()