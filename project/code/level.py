from random import choice
from ui import UI
import pygame
import time
from debug import debug
from player import Player
from settings import *
from support import *
from tile import Tile
from weapons import Weapon,Magic
from enemy import Enemy

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# attack sprites
		self.current_attack=None
		self.current_magic=None
		self.attack_sprites=pygame.sprite.Group()
		self.attackable_sprites=pygame.sprite.Group()


		# sprite setup
		self.create_map()

		# user stats interface
		self.ui=UI()



	def create_map(self):
		layout={
			'boundary':import_csv_layout(os.path.join(Base_Dir,'map/map_FloorBlocks.csv')),
			'grass':import_csv_layout(os.path.join(Base_Dir,'map/map_Grass.csv')),
			'object':import_csv_layout(os.path.join(Base_Dir,'map/map_Objects.csv')),
			'entities':import_csv_layout(os.path.join(Base_Dir,'map/map_Entities.csv')),
		}
		graphics={
			'grass':import_folder(os.path.join(Base_Dir,'graphics/Grass')),
			'objects':import_folder(os.path.join(Base_Dir,'graphics/objects'))
		}
		# print(graphics)
		for style,layout in layout.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col !='-1':

						x = col_index * TILESIZE
						y = row_index * TILESIZE
						# For the boundary of the world
						if style=="boundary":
							Tile( (x,y), [self.obstacle_sprites], 'invisible')
						if style=="grass":	# for the grass in the area
							random_grass_img=choice(graphics['grass'])
							Tile(
								(x,y),
								[self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],
								'grass',
								random_grass_img)
						if style=="object":	# for the objects inside the game
							surf=graphics['objects'][int(col)]
							Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'objects',surf)
						if style=="entities":	# for the objects inside the game
							
							if col=='394':
								self.player = Player(
									(x,y),
									[self.visible_sprites],
									self.obstacle_sprites,
									self.create_attack,
									self.destroy_attack,
									self.create_magic,
									self.destroy_magic)
							else:
								if col=='390':monster_name='bamboo'
								elif col=='391': monster_name='spirit'
								elif col=='392': monster_name='raccoon'
								else:monster_name='squid'
								Enemy(
									monster_name,
									(x,y),
									[self.visible_sprites,self.attackable_sprites],
									self.obstacle_sprites,self.damage_player
								)
							# 	surf=graphics['objects'][int(col)]
							# Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'objects',surf)
		
		

	def create_attack(self):
		self.current_attack=Weapon(self.player, [self.visible_sprites,self.attack_sprites])

	def create_magic(self,style,strength,cost):
		# print(f"------------\n{style}")
		# print(strength)
		# print(cost)
		self.current_magic=Magic(self.player, [self.visible_sprites,self.attack_sprites])


	def destroy_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack=None

	def destroy_magic(self):
		if self.current_magic:
			self.current_magic.kill()
		self.current_magic=None
	
	def player_attack_logic(self):
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				collision_sprite=pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
				if collision_sprite:
					for target_sprite in collision_sprite:
						if target_sprite.sprite_type=='grass':
							# print("grass destroyed")
							target_sprite.kill()
						else:
							# print("enemy sprites")
							# player.health-=monster_data[self.monster_name]['damage']
							target_sprite.get_damage(self.player,attack_sprite.sprite_type)
	
	def damage_player(self,ammount,attack_type):
		if self.player.vulnerable:
			self.player.health-=ammount
			self.player.vulnerable=False
			self.player.hurt_time=pygame.time.get_ticks()
			# particles

	def player_death(self):
		if self.player.health<=0:
			self.player.kill()
			try:
				pygame.quit()
			except:
				pass
			
		

	def run(self):
		# update and draw the game
		self.player_death()
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		self.visible_sprites.enemy_update(self.player)
		self.player_attack_logic()
		# debug(self.player.status)
		self.ui.display(self.player)


class YSortCameraGroup(pygame.sprite.Group):

	def __init__(self):


		#general part
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width=self.display_surface.get_size()[0]//2
		self.half_height=self.display_surface.get_size()[1]//2
		self.offset=pygame.math.Vector2()

		# creatign the floor
		
		self.floor_surface=pygame.image.load(os.path.join(Base_Dir,'graphics/tilemap/ground.png'))
		self.floor_rect=self.floor_surface.get_rect(topleft=(0,0))
	
	def custom_draw(self,player):
		self.offset.x=player.rect.centerx-self.half_width
		self.offset.y=player.rect.centery-self.half_height
		
		#d awing the floor
		floor_offset_pos=self.floor_rect.topleft-self.offset
		self.display_surface.blit(self.floor_surface,floor_offset_pos)

		for sprite in sorted(self.sprites(), key=lambda sprite : sprite.rect.centery):
			offset_pos=sprite.rect.topleft-self.offset
			self.display_surface.blit(sprite.image,offset_pos)

	def enemy_update(self,player):
		enemy_sprites=[sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type=='enemy']
		for enemy in enemy_sprites:
			enemy.enemy_update(player)