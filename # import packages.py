# import packages
import turtle
import random
turtle.tracer(False)

# global colors
col = ['red', 'yellow', 'green', 'blue',
	'white', 'black', 'orange', 'pink']

t = turtle.Turtle()


# method to call on timer
def fxn():
	global col
	ind = random.randint(0, 7)
	t.fd(20)

	# set background color of the
	# turtle screen randomly
	sc.bgcolor(col[ind])
	print('fxn')




# set screen
sc = turtle.Screen()
sc.setup(400, 300)

t


sc.onkey(fxn,'Up')

# loop for timer

sc.ontimer(fxn, t=400)

sc.mainloop()