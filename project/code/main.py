import pygame, sys
from settings import *
from level import Level
from button import Button
from menu import Menu
import time

class Game:
	# BG = pygame.image.load("project/graphics/tilemap/main_menu.png")
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
		self.menu=Menu()
		self.mode=mode

		
	def get_font(size): # Returns Press-Start-2P in the desired size
		return (pygame.font.Font(UI_FONT, size))

	
	def play(self):
		mode='play'
		while True:
			pygame.display.set_caption('Play Mode')

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill(WATER_COLOR)	
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS) 
	
	def game_menu(self):
		self.mode=self.menu.main_menu()
		print(mode)

if __name__ == '__main__':
	game = Game()
	if game.mode=='menu':
		game.game_menu()
	if game.mode=='play':
		game.play()