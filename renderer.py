### View

import pygame
import engine

class SokobanRenderer(engine.SokobanCore):

    screen_width = 960
    screen_height = 720

    palette = [
        (0x1a,0x1c,0x2c), 
        (0xf4,0xf4,0xf4), 
        (0xff,0xcd,0x75), 
        (0xa7,0xf0,0x70), 
        (0xb1,0x3d,0x53), 
        (0xef,0x7d,0x57), 
        (0x1a,0x1c,0x2c)  
    ]

    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.s_width = int(self.screen_width/engine.MAP_WIDTH)
        self.s_height = int(self.screen_height/engine.MAP_HEIGHT)

        pygame.display.set_caption("Push Block")

    def displayScreen(self, img):
        # Take control of the window and display screen
        keyPressed = False
        imgrect = img.get_rect()
        while not keyPressed:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.display.quit(); return False
                elif event.type == pygame.KEYDOWN: keyPressed = True
            self.screen.blit(img, imgrect)
            pygame.display.flip()
        return True

    def drawMap(self):
        rect = pygame.Rect(0,0,self.s_width, self.s_height)
        for y in range(engine.MAP_HEIGHT):
            for x in range(engine.MAP_WIDTH):
                i = self.map[self.i_getIndex(x,y)]
                rect.x = x*self.s_width
                rect.y = y*self.s_height
                pygame.draw.rect(self.screen, self.palette[i], rect)
        rect.x = self.player_x * self.s_width
        rect.y = self.player_y * self.s_height
        pygame.draw.rect(self.screen, self.palette[1], rect)

