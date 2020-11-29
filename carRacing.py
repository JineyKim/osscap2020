import pygame
import sys
from pygame.locals import *

def turn8(matrix[], ):
    for i in range(22):
        for j in range(8,24):
            if matrix[i][j]==0:
                pygame.draw.rect(screen, BLACK, [(j-8)*20,(i+11)*20,(j-7)*20,(i+12)*20])
            elif matrix[i][j]==1:
                pygame.draw.rect(screen, WHITE, [(j-8)*20,(i+11)*20,(j-7)*20,(i+12)*20])
            elif matrix[i][j]==4:
                pygame.draw.rect(screen, RED,   [(j-8)*20,(i+11)*20,(j-7)*20,(i+12)*20])
    

matrix=[[8,8,8,8,8,8,8,8,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,1,0,4,4,4,4,4,4,4,4,4,4,4,4,0,1,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,8,8,8,8,8,8,8,8],]

circitMap=[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,6,6,6,5,5,4,3,2,1,2,3,4,5,5,6,6,6,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8]


pygame.init()

GRAY = ( 51, 51, 51)
BLACK= (  0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0, 255)
GREEN= ( 0, 255,  0)
RED  = (255,  0,  0)
 
size  = [320,640]
screen= pygame.display.set_mode(size)
  
pygame.display.set_caption("Jiney Racing 2020")
  
done= False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

            
    screen.fill(GRAY)

    for i in range(47):
        
    
    for i in range(22):
        for j in range(8,24):
            if matrix[i][j]==0:
                pygame.draw.rect(screen, BLACK, [(j-8)*20,(i+11)*20,(j-7)*20,(i+12)*20])
            elif matrix[i][j]==1:
                pygame.draw.rect(screen, WHITE, [(j-8)*20,(i+11)*20,(j-7)*20,(i+12)*20])
            elif matrix[i][j]==4:
                pygame.draw.rect(screen, RED,   [(j-8)*20,(i+11)*20,(j-7)*20,(i+12)*20])

    pygame.display.update()
    clock.tick(15)