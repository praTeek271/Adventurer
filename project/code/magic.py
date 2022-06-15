import pygame 
from settings import *


class MagicPlayer:

    def __init__(self,animation_player):
        self.animation_player=animation_player
        self.magic_sounds={
            'heal':pygame.mixer.Sound(os.path.join(Base_Dir,'audio/heal.wav')),
            'flame':pygame.mixer.Sound(os.path.join(Base_Dir,'audio/Fire.wav'))
        }

    def heal(self,player,strength,cost,groups):
        if player.energy>=cost:
            if player.health!=player.stats['health']:
                player.health+=strength
                
            player.energy-=cost
            self.animation_player.create_particles('aura',player.rect.center,groups)
            self.magic_sounds['heal'].play()
            self.animation_player.create_particles('heal',player.rect.center+pygame.math.Vector2(10,-60),groups)

    def flame(self,player,cost,groups):
        if player.energy>=cost:
            player.energy-=cost
            # self.magic_sounds['flame'].play()

            if player.status.split('_')[0]=='right':
                direction=pygame.math.Vector2(1,0)

            elif player.status.split('_')[0]=='left':
                direction=pygame.math.Vector2(-1,0)

            elif player.status.split('_')[0]=='up':
                direction=pygame.math.Vector2(0,-1)

            else:
                direction=pygame.math.Vector2(0,1)
        
            for i in range(1,6):
                if direction.x:
                    offset_x=(direction.x*i)*TILESIZE
                    x=player.rect.centerx+offset_x
                    y=player.rect.centery
                    self.animation_player.create_particles('flame',(x,y),groups)
                    self.magic_sounds['flame'].play()
                else:
                    offset_y=(direction.y*i)*TILESIZE
                    x=player.rect.centerx
                    y=player.rect.centery+offset_y
                    self.animation_player.create_particles('flame',(x,y),groups)
                    self.magic_sounds['flame'].play()