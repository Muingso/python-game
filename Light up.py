import pgzrun 
from random import randint 

TITLE = "Light up"

HEIGHT = 800
WIDTH = 1500

message=""

alien=Actor("alien")
message=""

def draw():
    screen.clear()
    screen.fill("blue")
    alien.draw()
    screen.draw.text(message,center=(800,25),fontsize= 70)

def place_alien():
    alien.x= randint(50, WIDTH-50)
    alien.y= randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message= "Good Shot"
        place_alien()
    else:
        message= "You missed"
place_alien()
pgzrun.go()
