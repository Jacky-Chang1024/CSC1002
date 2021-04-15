import turtle

def configure_screen():
    screen = turtle.Screen()
    # screen.screensize(250,250)
    screen.title('Snake')
    screen.reset()
    screen.setworldcoordinates(-330,-330,330,410)
    screen.setup(660,740)
    return screen
configure_screen()
turtle.home()
turtle.mainloop()