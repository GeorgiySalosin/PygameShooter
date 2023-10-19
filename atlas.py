import pygame

class Atlas():
   def __init__(self, input_image):
     self.atlas = input_image

   def get_frame(self, tile_res, frame, scale):
     frame -= 1
     image = pygame.Surface((tile_res, tile_res), pygame.SRCALPHA)
     atlas_res = int(self.atlas.get_width() / tile_res)
     image.blit(self.atlas, (0, 0),
                ((tile_res * (frame % atlas_res)), (tile_res * (frame // atlas_res)), tile_res, tile_res))
     image = pygame.transform.scale(image, ((tile_res * scale), (tile_res * scale)))
     return image


img_vegetation = pygame.image.load(f'Content/Map/Vegetation/Vegetation_2048_256-512.png')
vegetation = Atlas(img_vegetation)

tree01_1 = vegetation.get_frame(512,3,1)
tree01_2 = vegetation.get_frame(512,4,1)
tree02_1 = vegetation.get_frame(512,7,1)
tree02_2 = vegetation.get_frame(512,8,1)
tree03_1 = vegetation.get_frame(512,11,1)
tree03_2 = vegetation.get_frame(512,12,1)
tree04_1 = vegetation.get_frame(512,13,1)
tree04_2 = vegetation.get_frame(512,14,1)
tree05_1 = vegetation.get_frame(512,15,1)
tree05_2 = vegetation.get_frame(512,16,1)

bush01_1 = vegetation.get_frame(256,1,1)
bush01_2 = vegetation.get_frame(256,2,1)
bush02_1 = vegetation.get_frame(256,9,1)
bush02_2 = vegetation.get_frame(256,10,1)
bush03_1 = vegetation.get_frame(256,17,1)
bush03_2 = vegetation.get_frame(256,18,1)
bush04_1 = vegetation.get_frame(256,25,1)
bush04_2 = vegetation.get_frame(256,26,1)
bush05_1 = vegetation.get_frame(256,33,1)
bush05_2 = vegetation.get_frame(256,34,1)
bush06_1 = vegetation.get_frame(256,41,1)
bush06_2 = vegetation.get_frame(256,42,1)

grass01 = vegetation.get_frame(256,3,1)
grass02 = vegetation.get_frame(256,11,1)
grass03 = vegetation.get_frame(256,19,1)
grass04 = vegetation.get_frame(256,27,1)
grass05 = vegetation.get_frame(256,28,1)
grass06 = vegetation.get_frame(256,35,1)
grass07 = vegetation.get_frame(256,36,1)
grass08 = vegetation.get_frame(256,43,1)
grass09 = vegetation.get_frame(256,44,1)




