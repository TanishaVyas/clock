import pygame

# create screen
screen=pygame.display.set_mode([600,600])
pygame.display.set_caption("Clock :( ")
screen.fill((240,248,255))
pygame.display.flip()
pygame.draw.circle(screen, (0,0, 0),[300, 300], 170, 2)
pygame.draw.circle(screen, (0,0, 0),[300, 300], 175, 2)
pygame.display.update()
# to keep screen running
running=True
while running:
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:
            running = False
