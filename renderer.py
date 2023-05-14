### View

import pygame
import engine

class SokobanRenderer(engine.SokobanCore):

    d_screen_width = 960
    d_screen_height = 720
    b_tiles_loaded = False
    o_tile_images = [

    ]

    d_palette = [
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
        self.screen = pygame.display.set_mode((self.d_screen_width, self.d_screen_height))
        self.s_width = int(self.d_screen_width/engine.MAP_WIDTH)
        self.s_height = int(self.d_screen_height/engine.MAP_HEIGHT)

        pygame.display.set_caption("Warehouse")

    def m_displayScreen(self, img, m_render_step = None):
        # Take control of the window and display screen
        keyPressed = False
        imgrect = img.get_rect()
        while not keyPressed:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.display.quit(); return False
                elif event.type == pygame.KEYDOWN: keyPressed = True
            self.screen.blit(img, imgrect)
            if m_render_step:
                m_render_step(self)
            pygame.display.flip()
        return True

    def m_loadTiles(self, path):
        # Load tile images, if loading failed, use built-in palette for blocks
        self.b_tiles_loaded = True
        try:
            for i in range(len(self.d_palette)-1):
                self.o_tile_images.append(pygame.image.load(f"{path}/{i}.png"))
        except FileNotFoundError:
            self.b_tiles_loaded = False
            self.o_tile_images = []
            return
        # Use the player sprite as an icon if the tiles loaded successfully
        pygame.display.set_icon(self.o_tile_images[engine.PLAYER])

    def m_drawMap(self):
        rect = pygame.Rect(0,0,self.s_width, self.s_height)
        for y in range(engine.MAP_HEIGHT):
            for x in range(engine.MAP_WIDTH):
                i = self.map[self.i_getIndex(x,y)]
                rect.x = x*self.s_width
                rect.y = y*self.s_height
                if i == engine.BARRIER: continue
                if self.b_tiles_loaded:
                    self.screen.blit(self.o_tile_images[i], rect)
                else:
                    pygame.draw.rect(self.screen, self.d_palette[i], rect)
        rect.x = self.player_x * self.s_width
        rect.y = self.player_y * self.s_height
        if self.b_tiles_loaded: self.screen.blit(self.o_tile_images[engine.PLAYER], rect)
        else: pygame.draw.rect(self.screen, self.d_palette[engine.PLAYER], rect)

