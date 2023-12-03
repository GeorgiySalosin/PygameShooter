from pygame import *
def get_frame(input_image, tile_res, frame, scale=1):
     image = Surface((tile_res, tile_res), SRCALPHA)
     atlas_res = int(input_image.get_width() / tile_res)
     image.blit(input_image, (0, 0), ((tile_res * (frame % atlas_res)), (tile_res * (frame // atlas_res)), tile_res, tile_res))
     image = transform.scale(image, ((tile_res * scale), (tile_res * scale)))
     return image



def get_frame_nonsquare(input_image, tile_w, tile_h, frame, scale=1):
     image = Surface((tile_w, tile_h), SRCALPHA)
     atlas_res = input_image.get_width()/tile_w
     image.blit(input_image, (0,0), (tile_w*(frame%atlas_res), (tile_h*(frame//atlas_res)), tile_w, tile_h))
     image = transform.scale(image, ((tile_w * scale), (tile_h * scale)))
     return image