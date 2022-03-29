import pygame
from player import *
from support import *
class Weapon(pygame.sprite.Sprite):

    def __init__(self,player,groups):
        super().__init__(groups)
        direction=player.status.split('_')[0]
        self.sprite_type='Weapon'

                    # print("####-->",direction)
                    # print("####-->",status)
        #graphics
        full_path=os.path.join(Base_Dir,'graphics\weapons',"{0}\{1}.png".format(player.weapon,direction))
        self.image=pygame.image.load(full_path).convert_alpha()


        #placement
        if direction=='right':
            self.rect=self.image.get_rect(midleft=player.rect.midright+pygame.math.Vector2(0,15))
        elif direction=='left':
            self.rect=self.image.get_rect(midright=player.rect.midleft+pygame.math.Vector2(0,15))
        elif direction=='up':
            self.rect=self.image.get_rect(midbottom=player.rect.midtop+pygame.math.Vector2(-10,0))
        elif direction=='down':
            self.rect=self.image.get_rect(midtop=player.rect.midbottom+pygame.math.Vector2(-10,0))
        else:
            self.rect=self.image.get_rect(center=player.rect.center)


class Magic(pygame.sprite.Sprite):

    def __init__(self,player,groups):
        super().__init__(groups)
        direction=player.status.split('_')[0]
        self.animations={'frames':[]}
        self.frame_idex=player.frame_idex
        self.sprite_type='Magic'
        self.animation_speed=0.15
        
        
        main_path=os.path.join(Base_Dir,'graphics/particles',f"{player.magic}")
        # print("---------",main_path)
        for animation in self.animations.keys():
            self.animations[animation]=import_folder(os.path.join(main_path,animation))


                    # print("####-->",direction)
                    # print("####-->",status)
        #graphics
        
        # full_path=os.path.join(Base_Dir,'graphics/particles',"{0}/frames/{1}.png".format(player.magic,'04'))
        
        # self.image=pygame.image.load(full_path).convert_alpha()


        #placement
        if direction=='right':
            self.animate('midleft',player.hitbox.midright+pygame.math.Vector2(0,15))
        elif direction=='left':
            self.animate('midright',player.hitbox.midleft+pygame.math.Vector2(0,15))
        elif direction=='up':
            self.animate('midbottom',player.hitbox.midtop+pygame.math.Vector2(-10,0))
        elif direction=='down':
            self.animate('midtop', player.hitbox.midbottom+pygame.math.Vector2(-10,0))
        else:
            self.animate('center', player.hitbox.center)

    def animate(self,pos,value):
        animation=self.animations['frames']
        self.frame_idex+=self.animation_speed
        if self.frame_idex>=len(animation)-1:
            self.frame_idex=0
        self.image=animation[int(self.frame_idex)]
        
        if pos=="midright":
            self.rect=self.image.get_rect(midright=value)
        elif pos=="midleft":
            self.rect=self.image.get_rect(midleft=value)
        elif pos=="midtop":
            self.rect=self.image.get_rect(midtop=value)
        elif pos=="midbottom":
            self.rect=self.image.get_rect(midbottom=value)
