from utility import *
from pygame import *

 # order and switch debug
test = (image.load(r"test/order_test.png"), 1920, 1080, 144, 0.9)


a_idle_m24 = anim_list_nonsquare(image.load(r"Content/Character/Weapon/M24/Idle.png"), 1920, 1080, 144, 0.9)
a_zooming_m24 = anim_list_nonsquare(image.load(r"Content/Character/Weapon/M24/Zooming.png"), 1920, 1080, 22, 0.9)
a_scope_idle_m24 = anim_list_nonsquare(image.load(r"Content/Character/Weapon/M24/Scope_Idle.png"), 1920, 1080, 1, 0.9)
a_scope_shot_m24 = anim_list_nonsquare(image.load(r"Content/Character/Weapon/M24/Scope_shot.png"), 1920, 1080, 16, 0.9)
a_noscope_shot_m24 = anim_list_nonsquare(image.load(r"Content/Character/Weapon/M24/Noscope_shot.png"), 1920, 1080, 18, 0.9)
a_reloading_bullet_m24 = anim_list_nonsquare(image.load(r"Content/Character/Weapon/M24/Reloading_bullet.png"), 1920, 1080, 59, 0.9)
a_reloading_mag_m24 = anim_list_nonsquare(image.load(r"Content/Character/Weapon/M24/Reloading_mag.png"), 1920, 1080, 250, 0.9)
a_blend_exposure_m24 = anim_list_nonsquare(image.load(r"Content/Character/Weapon/M24/Blend_exposure.png"), 1920, 1080, 16, 0.9)

a_scope_shot_recoil_m24 = [[0, -10], [1, -34], [3, -65], [5, -96], [7, -120], [9, -130], [12, -129], [15, -127],
                           [18, -124], [21, -120], [23, -114], [25, -108], [27, -101], [29, -94], [30, -87], [30, -79],
                           [30, -71], [29, -63], [28, -56], [27, -49], [26, -42], [24, -36], [22, -26], [21, -23],
                           [20, -21], [20, -20]]

i_fx_tracer_base = image.load(r'Content/FX/Tracer_Base_256x16.png')
a_fx_tracer_base = anim_list(i_fx_tracer_base, 256, 256, 0.9)