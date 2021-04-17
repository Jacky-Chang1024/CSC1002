import turtle
import random
import time


#目前的问题：
#初始方向问题
#manual refresh
#object移动速度
SNAKE_SPEED = 300


def configure_screen():
    screen = turtle.Screen()
    screen.setup(660,740)
    screen.title('Snake')
    # Set the origin at center of motion area
    screen.setworldcoordinates(-330,-330,330,410) 
    return screen

def configure_game_status():
    global g_status_write
    global g_motion_write
    # Use try because at first g_foodPos was not defined
    try:
        contact = 9-len(g_foodPos)
    except:
        contact = 0
    motionList = ['Right', 'Up', 'Left', 'Down']
    index = int(g_snake.heading() / 90)
    motion = motionList[index]
    if g_on == -1:
        motion = 'Pause'

    
    g_status_write.pu()
    g_status_write.ht()
    g_status_write.setpos(-210,270)
    g_status_write.clear()
    statusInfor = 'Contact: %1d    Time:%4d     Motion:' %(contact,g_t_time)
    g_status_write.write(statusInfor, align="left", font=("Arial", 16, "bold"))

    g_motion_write.pu()
    g_motion_write.ht()
    g_motion_write.setpos(130,270)
    g_motion_write.clear()
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

def configure_snake():
    snake = turtle.Turtle(shape='square')
    snake.shapesize(1,1,2)
    snake.color('red','red')
    snake.pu()
    return snake

def random_position():
    # Use this to generate random coordinates
    x = random.randrange(-240,240,20)
    y = random.randrange(-240,240,20)
    return x, y

def configure_monster():
    monster = turtle.Turtle(shape='square')
    monster.pu()
    monster.color('purple')
    # Random position with a fair distance from the snake
    while True:
        x, y = random_position()
        if abs(x) > 40 and abs(y) > 40:
            monster.setpos(x,y)
            break
    return monster

def configure_food():
    while True:
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
            food.write(cnt, align="center", font=("Arial", 10, "normal"))
            food.sety(food.ycor() + 10)
            cnt+=1
            foodPos.append((x,y))
        # Prevent overlap
        if len(set(foodPos)) == 9 and ((0,0) not in foodPos):
            return foodPos, foodList
        else:
            for food in foodList:
                food.clear()    



def update_game_status():
    global g_on
    global g_t_time
    global g_bodyFlag
    global g_finish 
    global g_status_write
    global g_motion_write
    if g_finish == False:
        g_bodyFlag = 0
        end_time = time.time()
        g_t_time = int(end_time - g_start_time) 
        # Refresh status
        # g_status_write.clear()
        # g_motion_write.clear()
        configure_game_status()

        
        if win() or lose():
            g_finish = True
            g_on = -1
            g_bodyFlag = 1 # Use this to stop body moving
            # These two stamps for enjoying sight （＾∀＾）
            g_snake.stamp()
            g_monster.stamp()
        else:
            # Refresh the screen every 0.5s
            g_screen.update()
            # g_screen.ontimer(update_game_status,500)

def win():
    # Total lenth
    if len(g_bodyInfor) == 51:
        g_snake.write('Winner!!!',align='right',font=('Arial',15,'bold'))
        return True
    else:
        return False

def lose():
    x, y = g_monster.pos() - g_snake.pos()
    # 15 is enough for this game!
    if abs(x) < 15 and abs(y) < 15:
        g_monster.write('Game Over!!!',align='right',font=('Arial',15,'bold'))
        return True
    else:
        return False




def move():
    global g_bodyInfor
    global g_body
    global g_flag

    snake_move()
    body_move()
    # monster_move()
    update_game_status()
    g_screen.ontimer(move,SNAKE_SPEED)


def monster_move():
    MONSTER_SPEED = 500 + random.randrange(-100,100)
    if g_on == 1 or g_on == 0:
        x_m, y_m, = g_monster.pos()
        x,y =  g_snake.pos() - g_monster.pos()
        Abs = max(abs(x),abs(y))
        if Abs == abs(x): 
            g_monster.setx(10 * abs(x+1) / (x+1) + x_m)  
            # Add one to prevent the dividend from being zero
        else:
            g_monster.sety(10 * abs(y+1) / (y+1) + y_m)
    update_game_status()
    g_screen.ontimer(monster_move, MONSTER_SPEED)


def body_move():
    if g_on == 1 and g_bodyFlag != 1:
        generate_bodyInfor()
        eat()
        g_body.clearstamps()
        print_body()

def eat():
    global g_lenth # Represenet the lenth of the snake
    global g_foodPos
    global g_foodPosCopy
    global SNAKE_SPEED

    

    # Get a copy at beginning
    if len(g_foodPos) == 9:
        g_foodPosCopy = g_foodPos[:]
    # Round the numbers to keep the following 'in' taking effect
    xy = tuple(map(round, g_snake.pos()))

    if xy in g_foodPos:
        g_lenth += (g_foodPosCopy.index(xy) + 1) 
        foodList[g_foodPosCopy.index(xy)].clear()
        g_foodPos.remove(xy)
        SNAKE_SPEED += g_foodPosCopy.index(xy) * 5

def print_body():
    
    for item in g_bodyInfor:
        g_body.goto(item)
        g_body.stamp()

def body_writer():
    global g_body
    g_body = turtle.Turtle(shape='square')
    g_body.shapesize(1,1,2)
    g_body.color('black','blue')
    g_body.ht()
    g_body.pu()

def generate_bodyInfor():
    global g_bodyInfor
    if g_on == 1:
        g_bodyInfor.append(tuple(map(round ,g_snake.pos())))
        if g_lenth >= len(g_bodyInfor):
            pass
        elif g_lenth < len(g_bodyInfor):
            g_bodyInfor.pop(0)


def snake_move():
    barrier()
    snake_forward()
    g_screen.onkey(up, "Up")  
    g_screen.onkey(down, "Down")
    g_screen.onkey(left, "Left")
    g_screen.onkey(right, "Right")
    g_screen.onkey(pause, "space")

def barrier():
    global g_on
    snakeCopy = g_snake.clone()
    snakeCopy.ht()
    snakeCopy.fd(20)
    x,y = tuple(map(round,snakeCopy.pos()))
    # Body as barrier
    # if (x,y) in g_bodyInfor:
    #     print(snakeCopy.pos(), g_bodyInfor)
    #     g_on = 0
    # # Just in case, don’t be very precise, 240 will do.
    # # Boundary as barrier
    if x > 240 or x < -240 or y > 240 or y < -240:
        print((x,y))
        # Snake stop, monster move
        g_on = 0

def snake_forward():
    if g_on == 1:
        g_snake.fd(20)
    
def up():
    global g_on 
    g_on = 1
    if g_snake.heading() != 90 and g_snake.heading() != 270:
        g_snake.setheading(90)
    
def down():
    global g_on 
    g_on = 1
    if g_snake.heading() != 90 and g_snake.heading() != 270:
        g_snake.setheading(270)
    
def left():
    global g_on 
    global g_flag
    g_on = 1
    if (g_snake.heading() != 0 and g_snake.heading() != 180) or g_flag == 0:
        g_flag = 1
        g_snake.setheading(180)
    
def right():
    global g_on 
    g_on = 1
    
    if g_snake.heading() != 0 and g_snake.heading() != 180:    
        g_snake.setheading(0)

def pause():
    global g_on 
    g_on = - g_on 



def start(x,y):
    global g_foodPos 
    global foodList
    global g_start_time
    g_start_time = time.time()
    g_intro.clear()
    g_foodPos, foodList = configure_food()
    body_writer()
    move()
    monster_move()
    # update_game_status()
    g_screen.onscreenclick(None)



if __name__ == '__main__':
    
    turtle.tracer(False)
    g_on = 0 
    # 1 for move, 0 for start(monster moves, snake stops), -1 for pause
    g_lenth = 6
    # Five body and one self 
    g_bodyInfor = [(0,0)]
    # Self's initital coordinate
    g_t_time = 0
    # At beginning, time = 0
    g_flag = 0
    # Use this flag to check whether it is the first move
    # So that the player can choose arbitrary direcrion at first
    # It's not very important but confused
    g_finish = False
    g_screen = configure_screen()
    g_snake = configure_snake()
    g_monster = configure_monster()
    g_intro = configure_intro()
    g_status_write = turtle.Turtle()
    g_motion_write = turtle.Turtle()

    configure_boundary()
    configure_game_status()

    g_screen.onscreenclick(start)
    turtle.update()

    g_screen.listen()
    g_screen.mainloop()    