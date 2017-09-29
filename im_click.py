import pygame
import sys
img_path = sys.argv[1]
pygame.init()
screen = pygame.display.set_mode([640,480]) ##size of window
your_image = pygame.image.load(img_path)## image must be in the same folder, else path must be specified
# your_image = pygame.transform.scale(your_image, (640, 480))
while 1:
    screen.blit(your_image,[0,0]) ##pos of your image on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print '%d\t%d' % (pos[0], pos[1])

    pygame.display.flip()
