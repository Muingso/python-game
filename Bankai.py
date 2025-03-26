import pgzrun

from random import randint 

from time import time

WIDTH =950
HEIGHT =950

ground=[]
cables=[]

next_P =0
nop=8

start_time =0
end_time =0
total_time =0

def create_pole():
    for i in range(0,nop):
        pole = Actor("pole")
        pole.pos=()

pgzrun.go()