import turtle
import random
 
 
CURSOR_SIZE = 20
PLANE_DELAY = 10 # maybe increase speed as we go.... 10
BOMB_DELAY = 50
 
def move_plane():
    new_pos = (plane.xcor(), plane.ycor())
    if new_pos[0] > width // 2:
        plane.goto(- width // 2, plane.ycor() - size)
    else:
        plane.goto(plane.xcor() + 12, plane.ycor())
    if tower_collision(plane, towers):
        plane.goto( - width // 2 , height // 2)        
    screen.update()
    turtle.ontimer(move_plane, PLANE_DELAY)
     
     
def cell_collision(tur1, tur2):
    if tur1.distance(tur2) <= size / 2:
        return True
         
def tower_collision(tur, towers):
    for tower in towers:
        for cell in tower:
            if cell_collision(tur, cell):
                return True
                 
def bomb_collision():
    # Should I use global towers or pass as argument?
    pass
  
  
def start_bomb_drop():
    global bomb_dropping
    screen.onkey(None, "space")
    bomb.goto(plane.xcor(), plane.ycor())
    bomb.showturtle()
    __continue_bomb_drop()
     
     
def __continue_bomb_drop():
    global bomb_dropping, bomb_timer_id
    try:
        pass
        # canvas.after_cancel(bomb_timer_id) # Uncomment and remove "pass" to fix bug.
    except NameError:
        pass
    bomb.goto(bomb.xcor(), bomb.ycor() - 12)
    if bomb.ycor() < - height // 2 or bomb_collision():
        stop_bomb_drop()
    bomb_timer_id  = canvas.after(BOMB_DELAY, __continue_bomb_drop)
     
def stop_bomb_drop():
    global bomb_dropping, bomb_timer_id
    bomb.hideturtle()
    screen.onkey(start_bomb_drop, "space")
    canvas.after_cancel(bomb_timer_id)
         
# Screen   
screen = turtle.Screen()
canvas = screen.getcanvas()
screen.title("Alien Bomber")
screen.setup(800, 600)
screen.bgcolor("dark blue")
screen.listen()
screen.onkey(start_bomb_drop, "space")
screen.tracer(0)
 
# MISC.
cells = 20
cell_colors = ["black", "dark green", "brown"]
width = screen.window_width() - 50
height = screen.window_height() - 50
size = width / cells
offset = (cells % 2) * size/2 + size/2  # Center even and odd cells
 
# Build towers
towers = []
for col in range(-cells // 2, cells // 2):
    tower = []
    for level in range(random.randrange(1, 11)):
        block = turtle.Turtle(shape="square")
        block.shapesize(size / CURSOR_SIZE)
        block.color(random.choice(cell_colors))
        block.penup()
        block.goto(col * size + offset, - height // 2 + level * size + offset)
        tower.append(block)
    towers.append(tower)
     
# Plane
plane = turtle.Turtle(shape="triangle", visible=False)
plane.color("yellow")
plane.shapesize(20 / CURSOR_SIZE, 40 / CURSOR_SIZE)
plane.penup()
plane.goto( - width // 2 , height // 2)
plane.showturtle()
 
# Bomb
bomb = turtle.Turtle(shape="circle")
bomb.color("red")
bomb.shapesize(0.5)
bomb.penup()
bomb.hideturtle()
bomb_dropping = False
 
# Score
score = 0
high_score = 0
pen = turtle.Turtle()
# pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))
 
# Begin
screen.update()
move_plane()
turtle.done()
