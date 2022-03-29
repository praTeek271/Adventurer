# level import dictionaries 
layouts = {
			'boundary': import_csv_layout('../map/map_FloorBlocks.csv'),
			'grass': import_csv_layout('../map/map_Grass.csv'),
			'object': import_csv_layout('../map/map_Objects.csv'),
			'entities': import_csv_layout('../map/map_Entities.csv')
		}
		
graphics = {
			'grass': import_folder('../graphics/Grass'),
			'objects': import_folder('../graphics/objects')
		}

# player stats
self.stats = {'health': 100,'energy':60,'attack': 10,'magic': 4,'speed': 5}
self.max_stats = {'health': 300, 'energy': 140, 'attack': 20, 'magic' : 10, 'speed': 10}
self.upgrade_cost = {'health': 100, 'energy': 100, 'attack': 100, 'magic' : 100, 'speed': 100}

# enemy stats
self.monster_name = monster_name
monster_info = monster_data[self.monster_name]
self.health = monster_info['health']
self.exp = monster_info['exp']
self.speed = monster_info['speed']
self.attack_damage = monster_info['damage']
self.resistance = monster_info['resistance']
self.attack_radius = monster_info['attack_radius']
self.notice_radius = monster_info['notice_radius']
self.attack_type = monster_info['attack_type']

# game setup
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 60
TILESIZE = 64
HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0}

# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# weapons 
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'../graphics/weapons/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30,'graphic':'../graphics/weapons/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'../graphics/weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'../graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'../graphics/weapons/sai/full.png'}}

# magic
magic_data = {
	'flame': {'strength': 5,'cost': 20,'graphic':'../graphics/particles/flame/fire.png'},
	'heal' : {'strength': 20,'cost': 10,'graphic':'../graphics/particles/heal/heal.png'}}

# enemy
monster_data = {
	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}


# particle dictionary
self.frames = {
			# magic
			'flame': import_folder('../graphics/particles/flame/frames'),
			'aura': import_folder('../graphics/particles/aura'),
			'heal': import_folder('../graphics/particles/heal/frames'),
			
			# attacks 
			'claw': import_folder('../graphics/particles/claw'),
			'slash': import_folder('../graphics/particles/slash'),
			'sparkle': import_folder('../graphics/particles/sparkle'),
			'leaf_attack': import_folder('../graphics/particles/leaf_attack'),
			'thunder': import_folder('../graphics/particles/thunder'),

			# monster deaths
			'squid': import_folder('../graphics/particles/smoke_orange'),
			'raccoon': import_folder('../graphics/particles/raccoon'),
			'spirit': import_folder('../graphics/particles/nova'),
			'bamboo': import_folder('../graphics/particles/bamboo'),
			
			# leafs 
			'leaf': (
				import_folder('../graphics/particles/leaf1'),
				import_folder('../graphics/particles/leaf2'),
				import_folder('../graphics/particles/leaf3'),
				import_folder('../graphics/particles/leaf4'),
				import_folder('../graphics/particles/leaf5'),
				import_folder('../graphics/particles/leaf6'),
				self.reflect_images(import_folder('../graphics/particles/leaf1')),
				self.reflect_images(import_folder('../graphics/particles/leaf2')),
				self.reflect_images(import_folder('../graphics/particles/leaf3')),
				self.reflect_images(import_folder('../graphics/particles/leaf4')),
				self.reflect_images(import_folder('../graphics/particles/leaf5')),
				self.reflect_images(import_folder('../graphics/particles/leaf6'))
				)
			}