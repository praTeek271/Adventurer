import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self) : 
		  
		# general setu p
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('..ADVENTURER..')
		pygame_icon = icon_location
		pygame.display.set_icon(pygame_icon)
		self.clock = pygame.time.Clock()
		self.main_sound=pygame.mixer.Sound(os.path.join(Base_Dir,'audio/main.ogg'))
		self.main_sound.play(loops=-1)
		self.level=Level()
 		
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill(WATER_COLOR)	
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS) 

if __name__ == '__main__':
	game = Game()
	game.run() 