from settings import *
from csv import reader
import pygame
def import_csv_layout(path):
    terrain_map=[]
    with open(path) as level_map:
        layout=reader(level_map,delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return(terrain_map)

def import_folder(path):
    surface_list=[]
    for _,__,img_files in os.walk(path):
        for img in img_files:
            fullpath=path+"/"+img
            image_surf=pygame.image.load(fullpath).convert_alpha()
            surface_list.append(image_surf)
            
    return(surface_list)

# print(import_folder(os.path.join(Base_Dir,'graphics/Grass')))