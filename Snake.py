import turtle
import random
import time
    
def configure_screen():
    screen = turtle.Screen()
    screen.setup(660,740)
    # screen.screensize(250,250)
    screen.title('Snake')
    screen.setworldcoordinates(-330,-330,330,410)
    return screen

def configure_game_status():
    global g_status_write
    global g_motion_write
    global g_t_time
    global g_start_time
    
    try:
        contact = 9-len(foodPos)
        
    except:
        contact = 0
    # print(contact)
    motionList = ['Right', 'Up', 'Left', 'Down']
    index = int(g_snake.heading() / 90)
    motion = motionList[index]
    if on == -1:
        motion = 'Pause'

    
    # status.clear()
    # print('cleared')
    # print(motion)
    # print(g_t_time)

    
    g_status_write = turtle.Turtle()
    g_status_write.pu()
    g_status_write.ht()
    g_status_write.setpos(-210,270)
   
    statusInfor = 'Contact: %1d    Time:%4d     Motion:' %(contact,g_t_time)
    g_status_write.write(statusInfor, align="left", font=("Arial", 16, "bold"))

    g_motion_write = turtle.Turtle()
    g_motion_write.pu()
    g_motion_write.ht()
    g_motion_write.setpos(130,270)
    g_motion_write.write(motion, align='left', font=('Arial', 16, 'bold'))


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
    foodPos = []
    for food in foodList:
        x, y = random_position()
        food.ht()
        food.pu()
        food.setpos(x,y)
        food.sety(food.ycor() - 10)
        # print(cnt,x,y)
        food.write(cnt, align="center", font=("Arial", 10, "normal"))
        food.sety(food.ycor() + 10)
        cnt+=1
        foodPos.append((x,y))
    return foodPos, foodList


def update_game_status():
    global g_t_time

    end_time = time.time()
    g_t_time = int(end_time - g_start_time) 
    g_status_write.clear()
    g_motion_write.clear()
    configure_game_status()

    g_screen.update()
    g_screen.ontimer(update_game_status,500)


def eat():
    global g_lenth
    global foodPos
    global foodPosCopy
    
    if len(foodPos) == 9:
        foodPosCopy = foodPos[:]
    
    xy = g_snake.pos()

    if xy in foodPos:
        g_lenth += (foodPosCopy.index(xy) + 1) 
        foodList[foodPosCopy.index(xy)].clear()
        foodPos.remove(xy)


def print_body():
    
    # body.clearstamps()
    for item in g_bodyInfor:
        body.goto(item)
        body.stamp()
    # print('body printed')

def body_writer():
    global body
    body = turtle.Turtle(shape='square')
    body.color('blue')
    body.ht()
    body.pu()

def generate_bodyInfor():


    global g_bodyInfor

        # g_bodyInfor = []
    
    if on == 1:
        g_bodyInfor.append(g_snake.pos())
        if g_lenth >= len(g_bodyInfor):
            pass
        elif g_lenth < len(g_bodyInfor):
        # g_bodyInfor.append(g_snake.pos())
            g_bodyInfor.pop(0)
    # print(g_bodyInfor)

    # for i in range(number):
    #     bodyInfor.append(bodyInfor[-1])

def body_move():
    generate_bodyInfor()
    eat()
    body.clearstamps()
    # print('body cleared')
    print_body()


def move():
    global g_bodyInfor
    global body

    
    snake_move()
    monster_move()
    body_move()

    g_screen.update()
    g_screen.ontimer(move,500)

def monster_move():
    # global g_monster 
    if on == 1 or on == 0:
        x_m, y_m, = g_monster.pos()
        x,y =  g_snake.pos() - g_monster.pos()
        Abs = max(abs(x),abs(y))
        if Abs == abs(x): 
            g_monster.setx(10 * abs(x+1) / (x+1) + x_m)  # 加一防止被除数为零
        else:
            g_monster.sety(10 * abs(y+1) / (y+1) + y_m)
        # print('monster moved')
        # print(g_monster.pos())
  
def snake_move():
    # global g_snake
    # global g_screen
    # s = g_snake
    # angle=[0,180,90,270,0]
    snake_forward()
    g_screen.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
    g_screen.onkey(down, "Down")
    g_screen.onkey(left, "Left")
    g_screen.onkey(right, "Right")
    g_screen.onkey(pause, "space")
    # print('snake moved')
    # print(g_snake.pos())

def snake_forward():
    if on == 1:
        g_snake.fd(20)
    
def up():
    global on 
    on = 1
    if g_snake.heading() != 90 and g_snake.heading() != 270:
        g_snake.setheading(90)
    
def down():
    global on 
    on = 1
    if g_snake.heading() != 90 and g_snake.heading() != 270:
        g_snake.setheading(270)
    
def left():
    global on 
    on = 1
    if g_snake.heading() != 0 and g_snake.heading() != 180:
        g_snake.setheading(180)
    
def right():
    global on 
    on = 1
    
    if g_snake.heading() != 0 and g_snake.heading() != 180:    
        g_snake.setheading(0)

def pause():
    global on 
    on = - on 


def start(x,y):
    global foodPos 
    global foodList
    global g_start_time
    g_start_time = time.time()
    g_intro.clear()
    foodPos, foodList = configure_food()
    # generate_body(5)
    body_writer()
    move()
    update_game_status()
    g_screen.onscreenclick(None)



if __name__ == '__main__':
    
    turtle.tracer(False)
    # turtle.ontimer()
    # turtle.pu()
    # turtle.shape('square')
    on = 0

    g_lenth = 5

    g_bodyInfor = []



    
    g_screen = configure_screen()
    g_snake = configure_snake()
    # g_bodyInfor = [(0,0)] 
    g_monster = configure_monster()
    configure_boundary()
    g_intro = configure_intro()
    g_t_time = 0
    configure_game_status()
    g_screen.onscreenclick(start)
    turtle.update()
    # g_foodList = configure_food()
    # turtle.update()





    g_screen.listen()
    g_screen.mainloop()    
    



