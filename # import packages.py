# import packages
import turtle
import random
turtle.tracer(False)

# global colors
col = ['red', 'yellow', 'green', 'blue',
	'white', 'black', 'orange', 'pink']

# method to call on timer
def fxn():
	global col
	ind = random.randint(0, 7)

	# set background color of the
	# turtle screen randomly
	sc.bgcolor(col[ind])


# set screen
sc = turtle.Screen()
sc.setup(400, 300)

# loop for timer
for i in range(10):
	turtle.ontimer(fxn, t=400*(i+1))

turtle.mainloop()