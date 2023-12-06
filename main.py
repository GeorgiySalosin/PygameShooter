from pygame import *
from utility import *
from animation import *
from static_object import *

init()
# DISPLAY SETTINGS
info = display.Info()
FULLSCREEN_SIZE = (info.current_w, info.current_h)
is_fullscreen = False

# SCREEN DATA
WIDTH = 1920
HEIGHT = int(WIDTH * 9 / 16)
screen = display.set_mode((WIDTH, HEIGHT), RESIZABLE)
current_size = screen.get_size()
last_size = current_size  # screen size before going fullscreen
virtual_surface = Surface((WIDTH, HEIGHT))  # this surface represents a display. can be scaled to blit onto it

background = image.load(f'Content/Map/Overcast/Overcast_HQ.jpg')
background = transform.scale(background,[background.get_width()//4, background.get_height()//4])

dx = -(background.get_width()//2) + virtual_surface.get_width()//2
dy = -(background.get_height()//2) + virtual_surface.get_height()//2
pos = [0, 0]

# USER DATA
clock = time.Clock()
FPS = 60
font = font.Font('Content/HUD/Fonts/Bernhard.otf', 40)
camNoScopeSensibility = 1.5
BULLETS = 5
automatic_zoom = True

states = ('Idle', 'Zooming', 'Scope_idle', 'Scope_shot', 'Noscope_shot', 'Reloading_bullet', 'Reloading_mag', 'Blend_exposure')
states_duration = (2400, 350, 0, 250, 300, 970, 4166, 250)
current_frame = 0
current_state = states[0]
previous_time = time.get_ticks()
previous_state = current_state

bullets = BULLETS
is_mouse_locked = True
mouse.set_visible(False)
event.set_grab(True)

# STATIC OBJECTS
#solid = resize_by_distance(tree01a, 100)
#solid2 = resize_by_distance(tree01a, 10)

def play_m24_anim(current_state, current_frame):    # defines which animation should be played based on current state

    if current_state == states[0]:
        current_frame = play_cycled(a_idle_m24, current_frame, virtual_surface)
    elif current_state == states[1]:
        current_frame = play_cycled(a_zooming_m24, current_frame, virtual_surface)
    elif current_state == states[2]:
        current_frame = play_cycled(a_scope_idle_m24, current_frame, virtual_surface)
    elif current_state == states[3]:
        current_frame = play_cycled(a_scope_shot_m24, current_frame, virtual_surface)
    elif current_state == states[4]:
        current_frame = play_cycled(a_noscope_shot_m24, current_frame, virtual_surface)
    elif current_state == states[5]:
        current_frame = play_cycled(a_reloading_bullet_m24, current_frame, virtual_surface)
    elif current_state == states[6]:
        current_frame = play_cycled(a_reloading_mag_m24, current_frame, virtual_surface)
    elif current_state == states[7]:
        current_frame = play_cycled(a_blend_exposure_m24, current_frame, virtual_surface)
    return current_state, current_frame

run = True
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == VIDEORESIZE:
            current_size = e.size
        # KEYDOWN
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
            elif e.key == K_F1:
                is_mouse_locked = not is_mouse_locked
                mouse.set_visible(not mouse.get_visible())
                if is_mouse_locked:
                    dx, dy = lock_mouse(dx, dy, virtual_surface, camNoScopeSensibility, True)
            elif e.key == K_F11:  # to go fullscreen or back
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    last_size = current_size
                    current_size = FULLSCREEN_SIZE
                    display.set_mode(current_size, FULLSCREEN)
                else:
                    current_size = last_size
                    display.set_mode(current_size, RESIZABLE)
            elif e.key == K_r:  # to reload a mag
                if bullets < BULLETS:
                    if current_state == states[0] or current_state == states[1] or current_state == states[2]:
                        previous_state = current_state
                        previous_time = time.get_ticks()
                        current_state = states[6]
                        current_frame = 0
        # MOUSE BUTTON CLICK
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 3:   #to scope-in/out
                if current_state == states[0]:
                    previous_state = current_state
                    previous_time = time.get_ticks()
                    current_state = states[1]
                    current_frame = 0

                elif current_state == states[1]:
                    previous_state = current_state
                    current_state = states[0]
                    current_frame = 0

                elif current_state == states[2]:
                    previous_state = current_state
                    current_state = states[0]
                    current_frame = 0

                elif current_state == states[3]:
                    previous_state = current_state
                    current_state = states[0]
                    current_frame = 0
                elif current_state == states[5] or current_state == states[6]:
                    automatic_zoom = not automatic_zoom
            if e.button == 1:   # to shoot
                if current_state == states[2]:
                    previous_state = current_state
                    previous_time = time.get_ticks()
                    current_state = states[3]
                    current_frame = 0
                    bullets -= 1

                if current_state == states[0]:
                    previous_state = current_state
                    previous_time = time.get_ticks()
                    current_state = states[4]
                    current_frame = 0
                    bullets -= 1

        elif e.type == MOUSEMOTION:
            if is_mouse_locked:
                dx, dy = lock_mouse(dx, dy, virtual_surface, camNoScopeSensibility)
            else:
                event.set_grab(False)

    if current_state == states[1]:
        automatic_zoom = True
        if (time.get_ticks() - previous_time) > states_duration[1]:
            previous_state = current_state
            current_state = states[2]
            current_frame = 0

    elif current_state == states[2]:
        if previous_state == states[7]:
            if not mouse.get_pressed()[0]:
                    previous_state = current_state
                    previous_time = time.get_ticks()
                    current_frame = 0
                    if bullets <= 0:
                        current_state = states[6]
                    else:
                        current_state = states[5]

    elif current_state == states[3]:
        if mouse.get_pressed()[0]:
            if (time.get_ticks() - previous_time) > states_duration[3]:
                previous_state = current_state
                previous_time = time.get_ticks()
                current_state = states[7]
                current_frame = 0
        else:
            if (time.get_ticks() - previous_time) > states_duration[3]:
                if bullets<=0:
                    previous_state = current_state
                    current_state = states[6]
                else:
                    previous_state = current_state
                    previous_time = time.get_ticks()
                    current_state = states[5]

    elif current_state == states[4]:
        if (time.get_ticks() - previous_time) > states_duration[4]:
            previous_state = current_state
            current_frame = 0
            if bullets<=0:
                current_state = states[6]
            else:
                current_state = states[5]

    elif current_state == states[5]:
        if (time.get_ticks() - previous_time) > states_duration[5]:
            previous_state = current_state
            previous_time = time.get_ticks()
            current_frame = 0
            if automatic_zoom:
                current_state = states[1]
            else:
                current_state = states[0]

    elif current_state == states[6]:
        if (time.get_ticks() - previous_time) > states_duration[6]:
            previous_state = current_state
            previous_time = time.get_ticks()
            current_frame = 0
            if automatic_zoom:
                current_state = states[1]
            else:
                current_state = states[0]
            bullets = BULLETS

    elif current_state == states[7]:
        if mouse.get_pressed()[0]:
            if (time.get_ticks() - previous_time) > states_duration[7]:
                previous_state = current_state
                current_state = states[2]
                current_frame = 0
        else:
            previous_state = current_state
            current_frame = 0
            if bullets <= 0:
                current_state = states[6]
            else:
                current_state = states[5]

    dx, dy = bg_check_bounds(dx, dy, background, virtual_surface)

    virtual_surface.blit(background, [dx, dy])
    current_state, current_frame = play_m24_anim(current_state, current_frame)


    scaled_surface = transform.scale(virtual_surface, current_size)
    screen.blit(scaled_surface, (0, 0))
    display.flip()
    clock.tick(FPS)
quit()
