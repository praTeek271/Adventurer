import pygame, sys
from button import Button
from settings import *
# from pyvedplayer import Video
class Menu:
    def __init__(self,scrn='menu'):
        self.BG = pygame.image.load(MAIN_MENU)
        self.GO_BG = pygame.image.load(os.path.join(Base_Dir,'graphics/tilemap/GO_BG.png'))
        self.game_over_song=pygame.mixer.Sound(os.path.join(Base_Dir,'audio/game-over.mp3'))
        self.menu_sound=pygame.mixer.Sound(os.path.join(Base_Dir,'audio/futuristic-space-war-percussion.wav'))
        self.SCREEN = pygame.display.set_mode((1280, 720))

        if mode=='menu' or self.mode=='menu':
            self.menu_sound.play(loops=-1)
        elif mode!='menu':
            self.menu_sound.stop()
        
        if scrn=='gameOver':
            self.game_over_song.play(loops=-1)
            scrn='menu'
            self.game_over_menu()


    def get_font(self,size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font(UI_FONT, size)
#
    # def play():
    #     while True:
    #         PLAY_MOUSE_POS = pygame.mouse.get_pos()

    #         SCREEN.fill("black")

    #         PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
    #         PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
    #         SCREEN.blit(PLAY_TEXT, PLAY_RECT)

    #         PLAY_BACK = Button(image=None, pos=(640, 460), 
    #                             text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

    #         PLAY_BACK.changeColor(PLAY_MOUSE_POS)
    #         PLAY_BACK.update(SCREEN)

    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 sys.exit()
    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #                 if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
    #                     main_menu()

    #         pygame.display.update()
#
    def options(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill("white")

            OPTIONS_TEXT = self.get_font(45).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            self.SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        mode='menu'
                        self.main_menu()

            pygame.display.update()

    def game_over_menu(self):
        while True:
            self.SCREEN.blit(self.GO_BG, (0, 0))
            MOUSE_POS = pygame.mouse.get_pos()
        # buttons on the game over screen
            RE_PLAY_BUTTON = Button(image=None, pos=(950, 360),text_input="PLAY AGAIN", font=self.get_font(50), base_color="white", hovering_color="Green")
            QUIT = Button(image=None, pos=(950, 460), text_input="QUIT", font=self.get_font(50), base_color="white", hovering_color="Green")
           
        #    update with hover
            for button in [RE_PLAY_BUTTON,QUIT]:
                button.changeColor(MOUSE_POS)
                button.update(self.SCREEN)
            
        # for the events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RE_PLAY_BUTTON.checkForInput(MOUSE_POS):
                        self.game_over_song.stop()
                        mode='menu'
                        self.main_menu()
                    if QUIT.checkForInput(MOUSE_POS):
                        pygame.quit()
                        sys.exit()


            pygame.display.update()

    def main_menu(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            # MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
            # MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=None, pos=(390,430), 
                                text_input="PLAY", font=self.get_font(40), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=None, pos=(965, 430), 
                                text_input="OPTIONS", font=self.get_font(34), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=None, pos=(673, 640), 
                                text_input="QUIT", font=self.get_font(40), base_color="#d7fcd4", hovering_color="White")

            # SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.menu_sound.stop()
                        return('play')
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        mode='option'
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

