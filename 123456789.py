import turtle
import random   

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


def move():
    global g_screen
    g_screen.ontimer(monster_move(),250)
    g_screen.ontimer(snake_move(),250)

def monster_move():
    global g_monster
    x_m, y_m, = g_monster.pos()
    x,y =  g_snake.pos() - g_monster.pos()
    Abs = max(abs(x),abs(y))
    if Abs == abs(x): 
        g_monster.setx(20 * abs(x+1) / (x+1))# 加一防止被除数为零
    else:
        g_monster.sety(20 * abs(y+1) / (y+1))
    print('monster moved')
    



    
def snake_move():
    global g_snake
    global g_screen
    s = g_snake
    angle=[0,180,90,270,0]
    g_screen.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
    g_screen.onkey(down, "Down")
    g_screen.onkey(left, "Left")
    g_screen.onkey(right, "Right")
    g_screen.onkey(pause, "space")
    print('snake moved')



    

g_snake = configure_snake()
g_monster = configure_monster()
# 
#  snake_move()
def configure_screen():
    screen = turtle.Screen()
    screen.setup(660,740)
    # screen.screensize(250,250)
    screen.title('Snake')
    screen.setworldcoordinates(-330,-330,330,410)
    return screen




g_screen = configure_screen()
g_screen.listen()
g_screen5.mainloop()