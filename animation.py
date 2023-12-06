from utility import *
from pygame import *





i_test = image.load(r"test/order_test.png")
a_test = anim_list_nonsquare(i_test, 1920, 1080, 144)   #order and switch debug

i_idle_m24 = image.load(r"Content/Character/Weapon/M24/Idle.png")
a_idle_m24 = anim_list_nonsquare(i_idle_m24, 1920, 1080, 144)

i_zooming_m24 = image.load(r"Content/Character/Weapon/M24/Zooming.png")
a_zooming_m24 = anim_list_nonsquare(i_zooming_m24, 1920, 1080, 22)

i_scope_idle_m24 = image.load(r"Content/Character/Weapon/M24/Scope_Idle.png")
a_scope_idle_m24 = [i_scope_idle_m24]

i_scope_shot_m24 = image.load(r"Content/Character/Weapon/M24/Scope_shot.png")
a_scope_shot_m24 = anim_list_nonsquare(i_scope_shot_m24, 1920, 1080, 16)

i_noscope_shot_m24 = image.load(r"Content/Character/Weapon/M24/Noscope_shot.png")
a_noscope_shot_m24 = anim_list_nonsquare(i_noscope_shot_m24, 1920, 1080, 18)

i_reloading_bullet_m24 = image.load(r"Content/Character/Weapon/M24/Reloading_bullet.png")
a_reloading_bullet_m24 = anim_list_nonsquare(i_reloading_bullet_m24, 1920, 1080, 59)

i_reloading_mag_m24 = image.load(r"Content/Character/Weapon/M24/Reloading_mag.png")
a_reloading_mag_m24 = anim_list_nonsquare(i_reloading_mag_m24, 1920, 1080, 250)

i_blend_exposure_m24 = image.load(r"Content/Character/Weapon/M24/Blend_exposure.png")
a_blend_exposure_m24 = anim_list_nonsquare(i_blend_exposure_m24, 1920, 1080, 16)
