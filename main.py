
### Controller

import pygame
import levels
import renderer

### Variables

frame = 0
i_window = 0
level = 0
moves = 0

# Font is to be loaded later
game_font = None

title_screen = pygame.image.load("assets/title.png")
win_screen_bg = pygame.image.load("assets/win.png")
end_screen = pygame.image.load("assets/end.png")

### Functions

def winScreen(renderer):
    global game_font, moves
    t_moves = game_font.render(f"Moves done: {moves:03d}", False, (255,255,255))
    t_next_level = game_font.render(f"Upcoming Level : {level+1}/{len(levels.map)}", False, (255, 255, 255))
    
    t_move_rect = t_moves.get_rect()
    t_next_rect = t_next_level.get_rect()
    
    # Render the text at the center of the screen
    renderer.screen.blit(t_moves, ((renderer.d_screen_width-t_move_rect.width)/2, ((renderer.d_screen_height-t_move_rect.height)/2)-15))
    renderer.screen.blit(t_next_level, ((renderer.d_screen_width-t_next_rect.width)/2, ((renderer.d_screen_height-t_next_rect.height)/2)+15))
    
    return

def checkWin():
    global level, running, moves
    if game.b_checkWin():
        level += 1
        level %= len(levels.map)
        game.m_loadLvl(levels.map[level])
        if level != 0: 
            running = game.m_displayScreen(win_screen_bg, winScreen)
            moves = 0
        else:
            running = game.m_displayScreen(end_screen)
            if running: running = game.m_displayScreen(title_screen)
            moves = 0

### The main program

pygame.init()

game_font = pygame.font.SysFont("Helvetica", 30)

game = renderer.SokobanRenderer()
game.m_loadLvl(levels.map[level])
game.m_loadTiles("assets/")
keys = pygame.key.get_pressed()

running = True

running = game.m_displayScreen(title_screen)

while running:
    game.screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            moved = False
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                moved = game.b_move_player(-1,0)
            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not moved:
                moved = game.b_move_player(1,0)
            elif (keys[pygame.K_UP] or keys[pygame.K_w]) and not moved:
                moved = game.b_move_player(0,-1)
            elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not moved:
                moved = game.b_move_player(0,1)
            
            if keys[pygame.K_r] and not moved:
                moves = 0
                game.m_loadLvl(levels.map[level])

            # Uncomment for debug
            # if keys[pygame.K_e] and not moved:
            #     level += 1
            #    level %= len(levels.map)
            #    game.m_loadLvl(levels.map[level])
                        
            
            if moved: 
                moves += 1
                checkWin()
    
    if not running: break
    game.m_drawMap()
    pygame.display.update()

pygame.display.quit()

