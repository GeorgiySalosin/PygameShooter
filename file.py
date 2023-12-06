
from pygame import *


screen = display.set_mode((800, 400), RESIZABLE)
gx = 0
gy = 0
bg = image.load(f'bg.png')
aspect = screen.get_width()/bg.get_width()
bg = transform.scale(bg, [bg.get_width()* aspect, bg.get_height()*aspect])
clock = time.Clock()
FPS = 60
def bg_scroll(bg, gx, gy):
    inst01 = bg
    inst02 = bg
    inst03 = bg

run = True
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
    clock.tick(FPS)
    screen.blit(bg, (gx,gy))
    display.flip()

