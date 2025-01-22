import pgzrun 
HEIGHT = 700
WIDTH = 700

def draw():
    
    rect = Rect ((0,0),(256,128))
    rect.center = 350,250
    screen.draw.filled_rect(rect,("white"))

    screen.draw.filled_circle((350,256),25,"red")
     

pgzrun.go()
