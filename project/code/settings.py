import pygame
import os
# game setup
WIDTH    = 1280	
# HEIGTH   = 686
HEIGTH   = 656
FPS      = 60
TILESIZE = 64
Base_Dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HITBOX_OFFSET = {
	'player': -26,
	'objects': -40,
	'grass': -10,
	'invisible': 0}


attack_cc=[735, 659, 349, 243, 402, 304, 243, 9, 276, 364, 718, 188, 373, 43, 546, 711, 729, 549, 333, 168, 378, 43, 677, 738, 507, 374, 963, 64, 705, 478, 825, 609, 530, 77, 873, 281, 956, 995, 58, 200, 115, 323, 442, 148, 174, 342, 812, 560, 226, 689, 377, 98, 846, 720, 344, 994, 389, 500, 630, 590, 922, 412, 434, 726, 424, 795, 537, 891, 372, 827, 513, 946, 177, 426, 615, 878, 729, 898, 511, 139, 699, 686, 133, 768, 736, 853, 170, 575, 58, 268, 537, 143, 382, 359, 236, 246, 402, 269, 339, 307]
# GENERAL COLOR PARAMETRS
WATER_COLOR='#71ddee'
UI_BG_COLOR='#232925'
UI_BORDER_COLOR='#111111'
TEXT_COLOR='#EEEEEE'
icon_location=pygame.image.load(os.path.join(Base_Dir,'graphics/test/swordsman.png'))

HEALTH_COLOR='red'
ENERGY_COLOR='blue'
UI_BORDER_COLOR_ACTIVE='gold'
debug_bg='#6061644d'
debug_Font='#e57615'
# ui data
BAR_HEIGHT=20
HEALTH_BAR_WIDTH=240
ENERGY_BAR_WIDTH=100
ITEM_BOX_SIZE=80
UI_FONT=os.path.join(Base_Dir,'graphics/font/joystix.ttf')
UI_FONT_SIZE=18
# weapon_data
weapon_data={
    'sword':{'cooldown':100,'damage':15,'graphics':os.path.join(Base_Dir,'graphics/weapons/sword/full.png')},
    'lance':{'cooldown':400,'damage':30,'graphics':os.path.join(Base_Dir,'graphics/weapons/lance/full.png')},
    'axe':{'cooldown':300,'damage':20,'graphics':os.path.join(Base_Dir,'graphics/weapons/axe/full.png')},
    'rapier':{'cooldown':50,'damage':8,'graphics':os.path.join(Base_Dir,'graphics/weapons/rapier/full.png')},
    'sai':{'cooldown':80,'damage':10,'graphics':os.path.join(Base_Dir,'graphics/weapons/sai/full.png')}
}

# magic
magic_data={
    'flame':{'strength':20,'cost':20,'graphic':os.path.join(Base_Dir,'graphics/particles/flame/fire.png')},
    'heal':{'strength':10,'cost':10,'graphic':os.path.join(Base_Dir,'graphics/particles/heal/heal.png')},

}

# enemy
monster_data = {
	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':os.path.join(Base_Dir,'audio/attack/slash.wav'), 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':os.path.join(Base_Dir,'audio/attack/claw.wav'),'speed': 2, 'resistance': 1, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':os.path.join(Base_Dir,'audio/attack/fire-sound.mp3'), 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':os.path.join(Base_Dir,'audio/attack/slash.wav'), 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
}

# changes

mode='menu'  # default mode

MAIN_MENU=os.path.join(Base_Dir,'graphics/tilemap/menu.png')
quit_game=False

#