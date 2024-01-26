#pygame module
import pygame
pygame.init()
#Three key elements such as window, game loop, event handler
#window
SCREEN_WIDTH = 800
SCREEN_HEIGHT =  600
#screen variables
screen = pygame.display. set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#adding player
player = pygame.Rect((300, 250, 50, 50))
#game loop
run = True
while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)
#key
key = pygame.key.get_pressed()
if key[pygame.k_a] == True:
    player.move_ip(-1, 0)
    elif key[pygame.k_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.k_w] == True:
    player.move_ip(0, -1)
    elif key[pygame.k_s] == True:
    player.move_ip(0, -1)
 #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
        pygame.display.update()
        pygame.quit()

