import pygame

pygame.init()

screen = pygame.display.set_mode((640,480))

pygame.display.set_caption("Hello From pygame")

rect = pygame.Rect(0,0,20,20)

running = True

while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rect.x += 1
    rect.x %= 640
    pygame.draw.rect(screen, (0,255,0), rect)
    pygame.display.update()

pygame.display.quit()
