from pygame import *
from configparser import ConfigParser

def cfg_load():
    config_path = 'config.ini'
    config = ConfigParser()

    try:
        with open(config_path) as f:
            config.read_file(f)
    except FileNotFoundError:
        config['SETTINGS'] = {
            "screen_width": str(display.Info().current_w),
            "screen_height": str(display.Info().current_h),
            "bullets": '5',
            "camNoScopeSensibility": '2'
        }
        with open(config_path, 'w') as f:
            config.write(f)
    return config
config = cfg_load()


# ATLASSING
def get_frame(input_image, tile_res, frame, scale=1):
    image = Surface((tile_res, tile_res), SRCALPHA)
    atlas_res = int(input_image.get_width() / tile_res)
    image.blit(input_image, (0, 0),
               ((tile_res * (frame % atlas_res)), (tile_res * (frame // atlas_res)), tile_res, tile_res))
    image = transform.scale(image, (round(int(config['SETTINGS']['screen_width']) * scale), round(int(config['SETTINGS']['screen_height']) * scale)))
    return image
def get_frame_nonsquare(input_image, tile_w, tile_h, frame, scale=1):
    image = Surface((tile_w, tile_h), SRCALPHA)
    atlas_res = input_image.get_width() / tile_w
    image.blit(input_image, (0, 0), (tile_w * (frame % atlas_res), (tile_h * (frame // atlas_res)), tile_w, tile_h))
    image = transform.scale(image, (round(int(config['SETTINGS']['screen_width']) * scale), round(int(config['SETTINGS']['screen_height']) * scale)))
    return image



# ANIMATION
def anim_list(image, tile_res, length, scale=1):
    myList = []
    for i in range(0, length):
        myList.append(get_frame(image, tile_res, i, scale))
    return myList
def anim_list_reverse(image, tile_res, length, scale=1):
    myList = []
    for i in range(0, length):
        myList.append(get_frame_nonsquare(image, tile_res, length-i, scale))
    return myList

def anim_list_nonsquare(image, tile_w, tile_h, length, scale=1):
    myList = []
    for i in range(0, length):
        myList.append(get_frame_nonsquare(image, tile_w, tile_h, i, scale))
    return myList
def anim_list_nonsquare_reverse(image, tile_w, tile_h, length, scale=1):
    myList = []
    for i in range(0, length):
        myList.append(get_frame_nonsquare(image, tile_w, tile_h, length-i, scale))
    return myList

def play_cycled(anim_list, current_frame, virtual_surface, coords = (0, 0)):  #utility function for playing animation by switching frames in an animation list
    virtual_surface.blit(anim_list[current_frame], (coords[0], coords[1]))
    current_frame += 1
    if current_frame >= len(anim_list):
        current_frame = 0
    return current_frame


# SPAWNING SM
def foggize(surface, fog_amount):
    fog = (59, 69, 86)
    _,_,w,h = surface.get_rect()
    img_color = [(1 - fog_amount) * 255] * 3
    fog = [x * fog_amount for x in fog]
    new_surface = Surface((w,h), SRCALPHA, 32)
    new_surface.blit(surface, surface.get_rect())
    new_surface.fill(img_color, surface.get_rect(), special_flags=BLEND_MULT)
    new_surface.fill(fog, surface.get_rect(), special_flags=BLEND_RGB_ADD)
    return new_surface
def resize_by_distance(surface, range):
    width, height = surface.get_size()
    surface = transform.scale(surface, (int(width*10/range), int(height*10/range)))
    fog_amount = int(range/100)
    surface = foggize(surface, fog_amount)
    return surface


# FUNCTIONAL



def bg_check_bounds(dx, dy, background, virtual_surface):    # Prevent scrolling out of background bounds
    if dx > 0:
        dx = 0
    elif dx < -(background.get_width()-virtual_surface.get_width()):
        dx = -(background.get_width()-virtual_surface.get_width())
    if dy > 0:
        dy = 0
    elif dy < -(background.get_height()-virtual_surface.get_height()):
        dy = -(background.get_height()-virtual_surface.get_height())
    return dx, dy


def lock_mouse(gx, gy, virtual_surface, camNoScopeSensibility, check_pos_offset = False):   #enables limitless move with mouse
    px = virtual_surface.get_width()//2
    py = virtual_surface.get_height()//2
    mouse_pos = (px, py)
    rel = mouse.get_rel()
    gx += rel[0]*camNoScopeSensibility
    gy += rel[1]*camNoScopeSensibility
    if mouse.get_pos()[0] < mouse_pos[0] - 100 \
            or mouse.get_pos()[0] > mouse_pos[0] + 100 \
            or mouse.get_pos()[1] < mouse_pos[1] - 100 \
            or mouse.get_pos()[1] > mouse_pos[1] + 100:     # if set mouse pos to 0 every frame then mouse move will be flicky, that's why magic numbers are used
        mouse.set_pos([px, py])
        if check_pos_offset:    #if snapping to locked mouse mode (F1 pressed) then we have to compensate mouse position offset
            gx -= rel[0]
            gy -= rel[1]
    return gx, gy


def bullet(virtual_surface, tracer_anim, is_tracer_start):
    tracer_frame = 0
    while tracer_frame < 255:
        tracer_frame = play_cycled(tracer_anim, tracer_frame, virtual_surface,
                                   [(virtual_surface.get_width() -
                                     tracer_anim[0].get_width()) // 2, (
                                            virtual_surface.get_height() - tracer_anim[
                                        0].get_height()) // 2])


def zoom(bg, dx, dy):
    bg = transform.scale(bg, [bg.get_width()*4, bg.get_height()* 4])
    dx *=4
    dy*=4
    return bg, dx, dy


def unzoom(bg, dx, dy):
    bg = transform.scale(bg, [bg.get_width() // 4, bg.get_height() // 4])
    dx //= 4
    dy //= 4
    return bg, dx, dy