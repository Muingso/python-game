from turtle import Screen
import pgzrun 
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

sky=[]
lines=[]

next_S =0 
nos=8
start_time =0
end_time =0
total_time =0

def create_staellite():
    for i in range(0,nos):
        staellite = Actor("staellite")
        staellite.pos=randint(50,WIDTH - 50),randint(50,HEIGHT - 50)
        sky.append(staellite)
    start_time=time()
def draw():
    global total_time 
    Screen.blit("background",(0,0))#BACKGROUND DRAW
    number=1
    for staellite in sky:
        screen.draw.text(str(number),(staellite.pos[0],staellite.pos[1]+20))
        staellite.draw()
        number = number + 1





pgzrun.go()