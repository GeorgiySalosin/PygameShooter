from pygame import *
from utility import *
class SM_Tree(sprite.Sprite):
    def __init__(self, dist, res, frame, coords=(0,0), scale=1):
        sprite.Sprite.__init__(self)
        self.image = image.load('Content/Map/Overcast/Vegetation_Overcast.png')
        self.dist = dist
        self.scale = scale
        self.surface = get_frame(self.image, res,frame,scale)
        self.coords = coords
        self.rect = self.surface.get_rect()
        self.rect.topleft = coords
        self.collision = mask.from_surface(self.surface)
class SM_Building(sprite.Sprite):
    def __init__(self, dist, res, frame, coords=(0,0), scale=1):
        sprite.Sprite.__init__(self)
        self.image = image.load('Content/Map/Overcast/Buildings_Overcast.png')
        self.dist = dist
        self.scale = scale
        self.surface = (get_frame(self.image, res,frame,scale))
        self.surface = resize_by_distance(self.surface, dist)
        self.coords = coords
        self.rect = self.surface.get_rect()
        self.collision = mask.from_surface(self.surface)

tree01a_001 = SM_Tree(100, 512, 2, (0,0))
tree01b_001 = SM_Tree(100, 512, 3, (0,0))
tree02a_001 = SM_Tree(100, 512, 6, (0,0))
tree02b_001 = SM_Tree(100, 512, 7, (0,0))
tree03a_001 = SM_Tree(100, 512, 10, (0,0))
tree03b_001 = SM_Tree(100, 512, 11, (0,0))
tree04a_001 = SM_Tree(100, 512, 12, (0,0))
tree04b_001 = SM_Tree(100, 512, 13, (0,0))
tree05a_001 = SM_Tree(100, 512, 14, (0,0))
tree05b_001 = SM_Tree(100, 512, 15, (0,0))
bush01a_001 = SM_Tree(100, 256, 0, (0,0))
bush01b_001 = SM_Tree(100, 256, 1, (0,0))
bush02a_001 = SM_Tree(100, 256, 8, (0,0))
bush02b_001 = SM_Tree(100, 256, 9, (0,0))
bush03a_001 = SM_Tree(100, 256, 16, (0,0))
bush03b_001 = SM_Tree(100, 256, 17, (0,0))
bush04a_001 = SM_Tree(100, 256, 24, (0,0))
bush04b_001 = SM_Tree(100, 256, 25, (0,0))
bush05a_001 = SM_Tree(100, 256, 34, (0,0))
bush05b_001 = SM_Tree(100, 256, 35, (0,0))
bush06a_001 = SM_Tree(100, 256, 40, (0,0))
bush06b_001 = SM_Tree(100, 256, 41, (0,0))

grass01 = SM_Tree(100, 256, 2, (0,0))
grass02 = SM_Tree(100, 256, 10, (0,0))
grass03 = SM_Tree(100, 256, 18, (0,0))
grass04 = SM_Tree(100, 256, 26, (0,0))
grass05 = SM_Tree(100, 256, 27, (0,0))
grass06 = SM_Tree(100, 256, 34, (0,0))
grass07 = SM_Tree(100, 256, 35, (0,0))
grass08 = SM_Tree(100, 256, 42, (0,0))
grass09 = SM_Tree(100, 256, 43, (0,0))


residential01a_001 = SM_Building(10, 512,7,(0,0))
residential01b_001 = SM_Building(100, 512,8,(0,0))
residential01c_001 = SM_Building(100, 512,9,(0,0))
residential02a_001 = SM_Building(100, 512,10,(0,0))
residential02b_001 = SM_Building(100, 512,11,(0,0))
residential02c_001 = SM_Building(100, 512,12,(0,0))
residential03a_001 = SM_Building(100, 512,13,(0,0))
residential03b_001 = SM_Building(100, 512,14,(0,0))
residential03c_001 = SM_Building(100, 512,15,(0,0))
residential04a_001 = SM_Building(100, 512,16,(0,0))
residential04b_001 = SM_Building(100, 512,17,(0,0))
residential04c_001 = SM_Building(100, 512,18,(0,0))
residential05a_001 = SM_Building(100, 512,19,(0,0))
residential05b_001 = SM_Building(100, 512,20,(0,0))
residential05c_001 = SM_Building(100, 512,21,(0,0))
residential06a_001 = SM_Building(100, 512,22,(0,0))
residential06b_001 = SM_Building(100, 512,23,(0,0))
residential07a_001 = SM_Building(100, 512,24,(0,0))
residential07b_001 = SM_Building(100, 512,25,(0,0))
residential08a_001 = SM_Building(100, 512,26,(0,0))
residential08b_001 = SM_Building(100, 512,27,(0,0))
toilet_a_0011 = SM_Building(100, 512,28,(0,0))
toilet_b_001 = SM_Building(100, 512,29,(0,0))
fence_trash_small_001 = SM_Building(100, 512,30,(0,0))
fence_rod_001 = SM_Building(100, 512,31,(0,0))
fence_concrete_001 = SM_Building(100, 512,32,(0,0))
fence_fabric_001 = SM_Building(100, 512,33,(0,0))
fence_trash_large_a_001 = SM_Building(100, 512,34,(0,0))
fence_trash_large_b_001 = SM_Building(100, 512,35,(0,0))
