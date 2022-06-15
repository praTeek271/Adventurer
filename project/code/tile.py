import pygame
from settings import *
import os
class Tile(pygame.sprite.Sprite):

    def __init__(self,pos,groups,sprite_type,surface=pygame.Surface((TILESIZE,TILESIZE))):
        '''
        pos=position ; 
        groups=sprite groups
        '''
        super().__init__(groups)
        
        # self.image=pygame.image.load(os.path.join(resourses_path,'rock.png')).convert_alpha()
        self.image=surface
        self.sprite_type=sprite_type
        y_offset=HITBOX_OFFSET[sprite_type]
        if sprite_type=='object':
            self.rect=self.image.get_rect(topleft=(pos[0]-3,pos[1]-(TILESIZE+2)))
        else:
            self.rect=self.image.get_rect(topleft=pos)
        self.hitbox=self.rect.inflate(0,y_offset)

