# from turtle import *
import turtle
import random
    

def configure_screen():
    screen = turtle.Screen()
    screen.setup(660,740)
    # screen.screensize(250,250)
    screen.title('Snake')
    screen.setworldcoordinates(-330,-330,330,410)
    return screen

def configure_game_status(p_contact, p_time, p_motion):
    # global g_screen
    turtle.pu()
    turtle.ht()
    turtle.setpos(0,270)
    status = 'Contact: %d  Time: %d  Motion: %s' %(p_contact,p_time,p_motion)
    turtle.write(status, align="center", font=("Arial", 16, "bold"))

def configure_intro():
    intro = turtle.Turtle()
    intro.ht()
    intro.pu()
    intro.setpos(-230,120)
    welcome = '''
    Welcome to Snake!
    You are going to use the 4 arrow keys to move the snake 
    around the screen, trying to consume all the food items
    before the monster catchers you

    Click anywhere on the screen to start the game.
    '''
    intro.write(welcome, align = 'left',font=("Arial", 10, "normal"))
    return intro

def configure_boundary():
    boundary = turtle.Turtle()
    boundary.pu()
    boundary.ht()
    boundary.speed(0)
    boundary.setpos(-250,330)
    boundary.pensize(2)
    boundary.pd()
    boundary.fd(500)
    boundary.rt(90)
    boundary.fd(580)
    boundary.rt(90)
    boundary.fd(500)
    boundary.rt(90)
    boundary.fd(580)
    boundary.bk(80)
    boundary.rt(90)
    boundary.fd(2)
    boundary.pensize(5)
    boundary.fd(495)
    # return boundary

def configure_snake():
    snake = turtle.Turtle(shape='square')
    snake.color('red')
    snake.pu()
    return snake

def random_position():
    x = random.randrange(-240,240,20)
    y = random.randrange(-240,240,20)
    return x, y

def configure_monster():
    monster = turtle.Turtle(shape='square')
    monster.pu()
    monster.color('purple')
    while True:
        x, y = random_position()
        if abs(x) > 40 and abs(y) > 40:
            monster.setpos(x,y)
            break
    print(monster.pos())
    return monster

def configure_food():
    foodList=[]
    for i in range(9):
        foodList.append(turtle.Turtle())
    cnt = 1
    for food in foodList:
        x, y = random_position()
        food.ht()
        food.pu()
        food.setpos(x,y)
        print(cnt,x,y)
        food.write(cnt, align="center", font=("Arial", 10, "normal"))
        cnt+=1
    # return foodList


def move():
    turtle.ontimer(monster_move(),250)
    turtle.ontimer(snake_move(),250)

# def monster_move():
#     global g_monster
#     x_m, y_m, = g_monster.pos()
#     x,y =  g_snake.pos() - g_monster.pos()
#     Abs = max(abs(x),abs(y))
#     if Abs == abs(x): 
        


    
def snake_move():
    global g_snake
    global g_screen
    s = g_snake
    angle=[0,180,90,270,0]
    
    moveKey = ['Right','Left','Up','Down','space']
    for i in range(5):
        g_snake =  g_screen.onkey(lambda : s.setpos(s.xcor()+xx[i],s.ycor()+yy[i]) ,moveKey[i])
    # g_snake =  s.onkey(move_down(),'Down')
    # g_snake =  s.onkey(move_left(),'Left')
    # g_snake =  s.onkey(move_right(),'Right')
    # g_snake =  s.onkey(move_pause(),'space')
    # g_snake = move_orientation(g_snake,i,j)
    

#注意转向的使用，上面的基本错了


    


# def move_orientation(p_object,i,j):
#     xx=[20,-20,0,0]
#     yy=[0,0,20,-20]
#     p_object.setpos(p_object.xcor()+xx[i], p_object.ycor()+yy[j] )
#     return p_object


def start(x,y):
    g_intro.clear()
    configure_food()



if __name__ == '__main__':

    turtle.tracer(False)
    # turtle.ontimer()
    # turtle.pu()
    # turtle.shape('square')
    
    g_screen = configure_screen()
    g_snake = configure_snake()
    g_monster = configure_monster()
    configure_game_status(12,12,'asd')
    configure_boundary()
    g_intro = configure_intro()
    g_screen.onscreenclick(start)
    turtle.update()
    # g_foodList = configure_food()
    turtle.update()

    # monster_move()
    # snake_move()

    g_screen.listen()
    g_screen.mainloop()    
    



