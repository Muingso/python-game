import pgzrun
from random import randint 

TITLE="Shoot the Alien"
HEIGHT = 700
WIDTH = 700

Message = ""
# a varialb use to display a message on the screen
# Actor is bulit in object in pgzero
alien = Actor("alien")
def draw():
    screen.clear()
    screen.fill("brown")
    alien.draw()
    screen.draw.text(Message,center=(600,10),fontsize= 30)
# def to make the alien go random place
def place_alien():
    alien.x=randint(50,WIDTH-50)
    alien.y=randint(50,HEIGHT-50)
place_alien()











pgzrun.go()