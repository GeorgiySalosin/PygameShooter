from pygame import *
from utility import *

class SM:
    def __init__(self, dist, scale):
        self.dist = dist
        self.scale = scale

class Bush(SM):

    def __init__(self, dist, scale):
        super().__init__(dist, scale)
        self.img = image.load('Content/Map/Overcast/Vegetation_Overcast.png')
        self.dist = dist
        self.scale = scale



imageVegetation = image.load('Content/Map/Overcast/Vegetation_Overcast.png')
imageVegetation_col = image.load('Content/Map/Overcast/Vegetation_Overcast_Col.jpg')
imageBuildings = image.load('Content/Map/Overcast/Buildings_Overcast.png')
imageBuildings_col = image.load('Content/Map/Overcast/Buildings_Overcast_Col.jpg')

tree01a = get_frame(imageVegetation, 512,2,1)
tree01b = get_frame(imageVegetation, 512, 3, 1)
tree02a = get_frame(imageVegetation, 512, 6, 1)
tree02b = get_frame(imageVegetation, 512, 7, 1)
tree03a = get_frame(imageVegetation, 512, 10, 1)
tree03b = get_frame(imageVegetation, 512, 11, 1)
tree04a = get_frame(imageVegetation, 512, 12, 1)
tree04b = get_frame(imageVegetation, 512, 13, 1)
tree05a = get_frame(imageVegetation, 512, 14, 1)
tree05b = get_frame(imageVegetation, 512, 15, 1)
bush01a = get_frame(imageVegetation, 256, 0, 1)
bush01b = get_frame(imageVegetation, 256, 1, 1)
bush02a = get_frame(imageVegetation, 256, 8, 1)
bush02b = get_frame(imageVegetation, 256, 9, 1)
bush03a = get_frame(imageVegetation, 256, 16, 1)
bush03b = get_frame(imageVegetation, 256, 17, 1)
bush04a = get_frame(imageVegetation, 256, 24, 1)
bush04b = get_frame(imageVegetation, 256, 25, 1)
bush05a = get_frame(imageVegetation, 256, 34, 1)
bush05b = get_frame(imageVegetation, 256, 35, 1)
bush06a = get_frame(imageVegetation, 256, 40, 1)
bush06b = get_frame(imageVegetation, 256, 41, 1)

grass01 = get_frame(imageVegetation, 256, 2, 1)
grass02 = get_frame(imageVegetation, 256, 10, 1)
grass03 = get_frame(imageVegetation, 256, 18, 1)
grass04 = get_frame(imageVegetation, 256, 26, 1)
grass05 = get_frame(imageVegetation, 256, 27, 1)
grass06 = get_frame(imageVegetation, 256, 34, 1)
grass07 = get_frame(imageVegetation, 256, 35, 1)
grass08 = get_frame(imageVegetation, 256, 42, 1)
grass09 = get_frame(imageVegetation, 256, 43, 1)

building_destroyed01a = get_frame(imageBuildings, 512,0,1)
building_destroyed01a_col = get_frame(imageBuildings_col, 512,0)
building_destroyed01b = get_frame(imageBuildings, 512,1,1)
building_destroyed02a = get_frame(imageBuildings, 512,2,1)
building_destroyed02b = get_frame(imageBuildings, 512,3,1)
building_destroyed03a = get_frame(imageBuildings, 512,4,1)
building_destroyed03b = get_frame(imageBuildings, 512,5,1)
building_destroyed03c = get_frame(imageBuildings, 512,6,1)
building_residential01a = get_frame(imageBuildings, 512,7,1)
building_residential01b = get_frame(imageBuildings, 512,8,1)
building_residential01c = get_frame(imageBuildings, 512,9,1)
building_residential02a = get_frame(imageBuildings, 512,10,1)
building_residential02b = get_frame(imageBuildings, 512,11,1)
building_residential02c = get_frame(imageBuildings, 512,12,1)
building_residential03a = get_frame(imageBuildings, 512,13,1)
building_residential03b = get_frame(imageBuildings, 512,14,1)
building_residential03c = get_frame(imageBuildings, 512,15,1)
building_residential04a = get_frame(imageBuildings, 512,16,1)
building_residential04b = get_frame(imageBuildings, 512,17,1)
building_residential04c = get_frame(imageBuildings, 512,18,1)
building_residential05a = get_frame(imageBuildings, 512,19,1)
building_residential05b = get_frame(imageBuildings, 512,20,1)
building_residential05c = get_frame(imageBuildings, 512,21,1)
building_residential06a = get_frame(imageBuildings, 512,22,1)
building_residential06b = get_frame(imageBuildings, 512,23,1)
building_residential07a = get_frame(imageBuildings, 512,24,1)
building_residential07b = get_frame(imageBuildings, 512,25,1)
building_residential08a = get_frame(imageBuildings, 512,26,1)
building_residential08b = get_frame(imageBuildings, 512,27,1)
building_toilet_a = get_frame(imageBuildings, 512,28,1)
building_toilet_b = get_frame(imageBuildings, 512,29,1)
fence_trash_small = get_frame(imageBuildings, 512,30,1)
fence_rod = get_frame(imageBuildings, 512,31,1)
fence_concrete = get_frame(imageBuildings, 512,32,1)
fence_fabric = get_frame(imageBuildings, 512,33,1)
fence_trash_large_a = get_frame(imageBuildings, 512,34,1)
fence_trash_large_b = get_frame(imageBuildings, 512,35,1)


class SM:
    def __init__(self, texture, distance, location):
        self.set(texture, distance, location)

    def set(self, texture, distance, location):
        self.texture = texture
        self.distance = distance
        self.location = location


tree01_inst001 = SM(tree01a, 100, [200, 200])