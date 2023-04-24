
### Controller

import pygame
import levels
import renderer

### Variables

frame = 0
i_window = 0
level = 0


### Functions

def checkWin():
    global level
    if game.b_checkWin():
        level += 1
        level %= len(levels.map)
        game.m_loadLvl(levels.map[level])


### The main program

pygame.init()

game = renderer.SokobanRenderer()
game.m_loadLvl(levels.map[level])
keys = pygame.key.get_pressed()

pygame.key.set_repeat(250, 150)

running = True

while running:
    frame += 1
    game.screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            moved = False
            if keys[pygame.K_LEFT]:
                moved = game.b_move_player(-1,0)
            elif keys[pygame.K_RIGHT] and not moved:
                moved = game.b_move_player(1,0)
        
            if keys[pygame.K_UP] and not moved:
                moved = game.b_move_player(0,-1)
            elif keys[pygame.K_DOWN] and not moved:
                moved = game.b_move_player(0,1)
            
            if keys[pygame.K_r] and not moved:
                game.m_loadLvl(levels.map[level])
            
            checkWin()
        
    game.drawMap()
    pygame.display.update()

pygame.display.quit()

