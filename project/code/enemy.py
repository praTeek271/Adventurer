import pygame

from settings import *

from entity import Entity

from support import *

class Enemy(Entity):

    def __init__(self, monster_name,pos,groups,obstacle_sprites,damage_player,trigger_def_particles):


        #general setup

        super().__init__(groups)

        self.sprite_type='enemy'


        #garphics setup

        self.import_graphics(monster_name)

        self.status='idle'

        # print("\n\n\n\n",self.animations,"\n\n\n\n")

        self.image=self.animations[self.status][self.frame_idex]

        #movement


        self.rect=self.image.get_rect(topleft=pos)

        self.hitbox=self.rect.inflate(-10,-10)

        self.obstacle_sprites=obstacle_sprites


        #stats of ememy
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


        # player_interaction

        self.can_attack=True

        self.attack_time=None

        self.attack_cooldown=400

        self.damage_player=damage_player
        self.trigger_death_particles=trigger_def_particles

		# incibility timer

        self.vulnerable=True

        self.hit_time=None

        self.invicibility_dur=400


        self.monster_DEATH_sound=pygame.mixer.Sound(os.path.join(Base_Dir,'audio/death.wav'))
        self.monster__HIT_sound=pygame.mixer.Sound(os.path.join(Base_Dir,'audio/hit.wav'))
        self.monster__HIT_sound.set_volume(0.2)
        self.monster_DEATH_sound.set_volume(0.2)
        self.attack_sound=pygame.mixer.Sound(monster_info['attack_sound'])
    def import_graphics(self,name):


        self.animations={'idle':[],'move':[],'attack':[]}

        main_path=os.path.join(Base_Dir,'graphics/monsters',f"{name}")

        # print("---------",main_path)

        for animation in self.animations.keys():

            self.animations[animation]=import_folder(os.path.join(main_path,animation))


    def get_player_distance_and_direction(self,player):

        enemy_vec=pygame.Vector2(self.rect.center)

        player_vec=pygame.math.Vector2(player.rect.center)

        distance=(player_vec-enemy_vec).magnitude()

        if distance>0:

            direction=(player_vec-enemy_vec).normalize()

        else:

            direction=pygame.math.Vector2()


        return(distance,direction)


    def get_satus(self,player):
        

        distance=self.get_player_distance_and_direction(player)[0]


        if distance<=self.attack_radius and self.can_attack:

            if self.status!='attack':

                self.frame_idex=0

            self.status='attack'

        elif distance<=self.notice_radius:

            self.status='move'

        else:

            self.status='idle'


    def actions(self,player):

        if self.status=='attack':
            self.attack_time=pygame.time.get_ticks()
            self.damage_player(self.attack_damage,self.attack_type)
            self.attack_sound.play()
        elif self.status=='move':

            self.direction=self.get_player_distance_and_direction(player)[1]

        else:

            self.direction=pygame.math.Vector2()

    def animate(self):

        animation=self.animations[self.status]

        self.frame_idex+=self.animation_speed

        if self.frame_idex>=len(animation):

            if self.status=='attack':

                self.can_attack=False

            self.frame_idex=0

        self.image=animation[int(self.frame_idex)]

        self.rect=self.image.get_rect(center=self.hitbox.center)

        if not self.vulnerable:

            # flicker

            alpha=self.wave_value()

            self.image.set_alpha(alpha)

        else:

            self.image.set_alpha(255)


    def get_damage(self,player,attack_type):

        self.direction=self.get_player_distance_and_direction(player)[1]

        if self.vulnerable: 

            if attack_type == 'Weapon':

                self.health-=player.get_full_weapon_damage()
            

            elif attack_type=='Magic':

                self.health-=player.get_full_magic_damage()

            self.hit_time=pygame.time.get_ticks()

            self.vulnerable=False
        
        

    def check_death(self):

        if self.health<=0:
            self.kill()
            self.monster_DEATH_sound.play()
            self.trigger_death_particles(self.rect.center,self.monster_name )

    def hit_reaction(self):

        if not self.vulnerable:
            self.monster__HIT_sound.play()
            self.direction*=-self.resistance

    def cooldown(self):

        current_time=pygame.time.get_ticks()

        if not self.can_attack:

            if (current_time-self.attack_time)>=self.attack_cooldown:

                self.can_attack=True

        if not self.vulnerable:

            if (current_time-self.hit_time)>=self.invicibility_dur:

                self.vulnerable=True

    def update(self):

        self.hit_reaction()

        self.move(self.speed)
        self.animate()

        self.cooldown()

        self.check_death()

    def enemy_update(self,player):

        self.get_satus(player)
        self.actions(player)