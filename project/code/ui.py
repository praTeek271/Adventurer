import pygame
from settings import *

class UI:

    def __init__(self):
        # general
        self.display_surface=pygame.display.get_surface()
        self.font=pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # bar setup
        self.health_bar_rect=pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
        self.energy_bar_rect=pygame.Rect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT)

        #convert weapon data from dictionary
        self.weapon_graphics=[pygame.image.load(weapon['graphics']).convert_alpha() for weapon in weapon_data.values()]
        self.magic_graphics=[pygame.image.load(magic['graphic']).convert_alpha() for magic in magic_data.values()]



    def show_bar(self,current,max_ammount,bg_rect,color):
        
        pygame.draw.rect(self.display_surface, UI_BG_COLOR,bg_rect,border_radius=8)
        
        # convert stats to pixel
        ratio=current/max_ammount

        current_width=bg_rect.width*ratio
        if current_width<=0:
            current_width=0
        current_rect=bg_rect.copy()
        current_rect.width=current_width

        # draw the bar
        pygame.draw.rect(self.display_surface,color,current_rect,border_radius=8)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR , current_rect,border_radius=4,width=4)

    def show_exp(self,exp):
        exp=str(exp)
        if len(exp)>3 and len(exp)<6:
            exp=int(exp)
            exp//=10**3
            text_surf=self.font.render(str(int(exp))+str('k'), False, TEXT_COLOR)
        elif len(exp)>6 and len(exp)<9:
            exp=int(exp)
            (exp)//=10**6
            text_surf=self.font.render(str(int(exp))+str('M'), False, TEXT_COLOR)
        else:
            text_surf=self.font.render(str(int(exp)), False, TEXT_COLOR)

        x=self.display_surface.get_size()[0]-20
        y=self.display_surface.get_size()[1]-20
        text_rect=text_surf.get_rect(bottomright=(x,y))

        pygame.draw.rect(self.display_surface, 'black', text_rect)
        self.display_surface.blit(text_surf,text_rect)
        pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(10,10),width=3)

    def selection_box(self,left,top):
        
        bg_rect=pygame.Rect( left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        # pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        # pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect,width=6)
        # return(bg_rect)
        #----------------------------------------------------------------
            #''' for using circles insted of rectangles '''
        pygame.draw.circle(self.display_surface, UI_BG_COLOR,(left,top),50)
        pygame.draw.circle(self.display_surface,'#aea5a4', (left,top),50,width=6)
        #-------
        
    def weapon_overlay(self,weapon_index):
        # bg_rect=self.selection_box(10, 57)
        bg_rect=self.selection_box(50, 106)

        weapon_surf=self.weapon_graphics[weapon_index]
        weapon_rect=weapon_surf.get_rect(center=(50,106))
        self.display_surface.blit(weapon_surf, weapon_rect)
        
        
    def magic_overlay(self,magic_index):
        # bg_rect=self.selection_box(10, 57)
        bg_rect=self.selection_box(109, 130)

        magic_surf=self.magic_graphics[magic_index]
        magic_rect=magic_surf.get_rect(center=(109, 130))
        self.display_surface.blit(magic_surf, magic_rect)
        
        
    def display(self,player):
        self.show_bar(player.health,player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.energy,player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)
            
        self.show_exp(player.exp)
        self.weapon_overlay(player.weapon_index)
        self.magic_overlay(player.magic_index)
        # self.selection_box(60, 76)
#---------------------------------------
        #''' for using circles insted of rectangles '''
        # self.selection_box(50, 106)
        # self.selection_box(109, 130)
#--    
  