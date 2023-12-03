
from pygame import *

screen = display.set_mode((1920, 1080), RESIZABLE)

gx = -12288
gy = -5120
mouse.get_pos()
background = image.load(f'Content/Map/Overcast/Overcast_UltraLow.jpg')
background = transform.scale(background, [background.get_width()*0.5, background.get_height()*0.5])
event.set_grab(True)
def lock_mouse(gx, gy):
    px = 400
    py = 400
    mouse_pos = (px, py)
    rel = mouse.get_rel()
    gx += rel[0]
    gy += rel[1]
    if mouse.get_pos()[0] < mouse_pos[0] - 100 \
            or mouse.get_pos()[0] > mouse_pos[0] + 100 \
            or mouse.get_pos()[1] < mouse_pos[1] - 100 \
            or mouse.get_pos()[1] > mouse_pos[1] + 100:
        mouse.set_pos([px, py])
    return gx, gy
run = True
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
        elif e.type == MOUSEMOTION:
            gx,gy = lock_mouse(gx, gy)

    screen.blit(background, (gx,gy))
    display.flip()


