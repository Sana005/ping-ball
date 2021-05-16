from pygame import *
fon = image.load('fon.jpg')
win = display.set_mode((500,300))
win.blit(fon,(0,0))
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            exit()
    display.update()