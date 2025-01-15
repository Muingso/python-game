import pgzrun
HEIGHT =800
WIDTH =700

def draw():
    rect = Rect((0,0),(64,64))
    rect.center = 180,180
    screen.draw.filled_rect(rect,("white"))
pgzrun.go()  