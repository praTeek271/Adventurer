import pygame 
from settings import *
import os
from support import import_folder
from entity import Entity

class Player(Entity):
	def __init__(self,pos,groups,obstacle_sprites,create_attack,destroy_attack,create_magic,destroy_magic):
		super().__init__(groups)
		
		self.image=pygame.image.load(os.path.join(Base_Dir,'graphics/test/player.png')).convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox=self.rect.inflate(0,-27)

		# adding graphics in the player
		self.import_player_assets()
		self.status='down'
		 
		#movement Parts
		 
		self.attacking=False
		self.attack_cooldown=400
		self.attack_time=None
		self.obstacle_sprites = obstacle_sprites
		self.create_attack=create_attack

		# weapon
		self.create_attack=create_attack
		self.destroy_attack=destroy_attack
		self.weapon_index=0
		self.weapon=list(weapon_data.keys())[self.weapon_index]

		# stats
		self.stats={
			'health':100,
			'energy':60,
			'attack':10,
			'magic':4,
			'speed':6
		}
	# ----------------------------------------made changes
		self.count_attack=0
	#
		# magic
		self.create_magic=create_magic
		self.destroy_magic=destroy_magic
		self.magic_index=0
		self.magic=list(magic_data.keys())[self.magic_index]
		self.can_switch_magic=True
		self.magic_switch_time=None
		self.switch_duration_cooldown=200
		self.health_reduction=1
		self.energy_reduction=1


		self.health=self.stats['health']*self.health_reduction
		self.energy=self.stats['energy']*self.energy_reduction
		self.exp=0
		self.speed=self.stats['speed']

		# damage timer
		self.vulnerable=True
		self.hurt_time=None
		self.invicibility_dur=500
		
	def animation(self):
		animation=self.animations[self.status]
		self.frame_idex+=self.animation_speed
		if self.frame_idex >= len(animation):
			self.frame_idex=0


			#set the image
		self.image=animation[int(self.frame_idex)]
		self.rect=self.image.get_rect(center=self.hitbox.center)

	def input(self): 
		if not self.attacking:
			keys = pygame.key.get_pressed()
		# movement input of the player
			if (keys[pygame.K_UP]or keys[pygame.K_w]):
				self.direction.y = -1
				self.status='up'
			elif (keys[pygame.K_DOWN] or keys[pygame.K_s]):
				self.direction.y = 1
				self.status='down'
			else:
				self.direction.y = 0

			if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
				self.direction.x = 1
				self.status='right'

			elif (keys[pygame.K_LEFT] or keys[pygame.K_a]):
				self.direction.x = -1
				self.status='left'
			else:
				self.direction.x = 0

		# attack input for the player
			if (keys[pygame.K_SPACE] or keys[pygame.K_f] and (self.energy!=0 or self.energy<0)):
				self.attacking=True
				self.attack_time=pygame.time.get_ticks()
				self.create_attack()
				self.count_attack+=1
				if self.count_attack in attack_cc:
					self.exp+=2
					if (self.health<=self.stats['health']):
						self.health+=2
					if (self.energy>0):
						self.energy-=0.23
					# print("Player Attacked\t---->\t---->\t---->\t---->\t---->\t---->\t---->")

		# magic input for the player
			if (keys[pygame.K_LCTRL] or keys[pygame.K_e] and (self.energy!=0 or self.energy<0)):
				self.attacking=True
				self.attack_time=pygame.time.get_ticks()
				style=list(magic_data.keys())[self.magic_index]
				strength=list(magic_data.values())[self.magic_index]['strength'] + self.stats['magic']
				cost=(list(magic_data.values()))[self.magic_index]['cost']
				self.create_magic(style,strength,cost)
		# ----------------------------------------made changes
				self.count_attack+=1
				if (style=='heal' and (self.health<=self.stats['health'])):
					self.health+=4
				if self.count_attack in attack_cc:
					self.exp+=2
					if (self.health<=self.stats['health']):
						self.health+=2
					if (self.energy>0):
						self.energy-=22

				
				# switching feature of magic
			if keys[pygame.K_q] and self.can_switch_magic:
				self.can_switch_magic=False
				self.magic_switch_time=pygame.time.get_ticks()

				if (self.magic_index< (len(list(magic_data.keys()))-1)):
					self.magic_index +=1
				else:
					self.magic_index=0
				self.magic=list(magic_data.keys())[self.magic_index]



		# change weapons
			if (keys[pygame.K_1]):
				self.weapon_index=0
				self.weapon=list(weapon_data.keys())[self.weapon_index]

			elif (keys[pygame.K_2]):
				self.weapon_index=1
				self.weapon=list(weapon_data.keys())[self.weapon_index]
			
			elif (keys[pygame.K_3]):
				self.weapon_index=2
				self.weapon=list(weapon_data.keys())[self.weapon_index]
			
			elif (keys[pygame.K_4]):
				self.weapon_index=3
				self.weapon=list(weapon_data.keys())[self.weapon_index]
			
			elif (keys[pygame.K_5]):
				self.weapon_index=4
				self.weapon=list(weapon_data.keys())[self.weapon_index]

	# player_assets
	def import_player_assets(self):
		character_path=os.path.join(Base_Dir,'graphics/player')
		self.animations={
			'up':[],
			'down':[],
			'left':[],
			'right':[],
			'right_idle':[],
			'left_idle':[],
			'up_idle':[],
			'down_idle':[],
			'right_attack':[],
			'left_attack':[],
			'up_attack':[],
			'down_attack':[]
			}

		for animation in self.animations.keys():
			fullpath=os.path.join(character_path,animation)
			self.animations[animation]=import_folder(fullpath)


	# get the position of the player in the game world
	def get_satus(self):
		if(self.direction.x==0 and self.direction.y==0):
			if not 'idle' in self.status and not 'attack' in self.status:
				if self.energy<HEALTH_BAR_WIDTH+5:
					self.energy+=5

				self.status=self.status+'_idle'
		if self.attacking:
			self.direction.x=0
			self.direction.y=0
			if not 'attack' in self.status:
				if ('idle' in self.status):
					self.status=self.status.replace('_idle', '_attack')
				else:
					self.status=self.status+'_attack'

		else:
			if ('attack' in self.status):
				self.status=self.status.replace( '_attack','_idle')

	# get weapon/magic damage 
	def get_full_weapon_damage(self):
		base_damage=self.stats['attack']
		weapon_damage=weapon_data[self.weapon]['damage']		
		return(base_damage+weapon_damage)
	def get_full_magic_damage(self):
		base_damage=self.stats['attack']
		magic_damage=magic_data[self.magic]['strength']
		return(base_damage+magic_damage)
	# weapon/magic  cooldown
	def cooldown(self):
		current_time=pygame.time.get_ticks()

		if self.attacking:
			if ((current_time-self.attack_time>=(self.attack_cooldown+(weapon_data[self.weapon]['cooldown'])))):
				self.attacking=False
				self.destroy_attack()
				self.destroy_magic()
		if not self.can_switch_magic:
			if (current_time-self.magic_switch_time) >= (self.switch_duration_cooldown):
				self.can_switch_magic=True
		if not self.vulnerable:
			if (current_time-self.hurt_time)>=self.invicibility_dur:
				self.vulnerable=True

	# sceen update
	def update(self):
		self.input()
		self.cooldown()
		self.get_satus()
		self.animation() 
		self.move(self.speed)