from matrix import *
import pygame
import sys
import LED_display as LMD
import threading
import time

#r36 r32 r26 r21 r15 r8 r3

WINDOWWIDTH = 480
WINBOWHEIGHT = 800
screen = pygame.display.set_mode((500, 500))
done = False
title = "RRacing game"
pygame.display.set_caption(title) #게임 이름

clock = pygame.time.Clock()

def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

def drive(handle):
    print(handle)
    if handle==13:
        ta=0
        tb=0
        tc=0
        td=6
        te=7
        tf=7
        tg=8
        th=8
        ti=8
        tj=8
        tk=8
    elif handle==12:
        ta=0
        tb=0
        tc=5
        td=6
        te=7
        tf=7
        tg=8
        th=8
        ti=8
        tj=8
        tk=8
    elif handle==11:
        ta=5
        tb=6
        tc=7
        td=7
        te=8
        tf=8
        tg=8
        th=8
        ti=8
        tj=8
        tk=8
    elif handle==10:
        ta=6
        tb=6
        tc=7
        td=7
        te=8
        tf=8
        tg=8
        th=8
        ti=8
        tj=8
        tk=8
    elif handle==9:
        ta=7
        tb=7
        tc=8
        td=8
        te=8
        tf=8
        tg=8
        th=8
        ti=8
        tj=8
        tk=8
    elif handle==8:
        ta=8
        tb=8
        tc=8
        td=8
        te=8
        tf=8
        tg=8
        th=8
        ti=8
        tj=8
        tk=8
    elif handle==7:
        ta=9
        tb=8
        tc=8
        td=8
        te=8
        tf=8
        tg=8
        th=8
        ti=8
        tj=8
        tk=8
    elif handle==6:
        ta=9
        tb=9
        tc=9
        td=9
        te=8
        tf=8
        tg=8
        th=8
        ti=8
        tj=8
        tk=8
    elif handle==5:
        ta=10
        tb=9
        tc=9
        td=9
        te=8
        tf=8
        tg=8
        th=8
        ti=8
        tj=8
        tk=8
    elif handle==4:
        ta=10
        tb=10
        tc=9
        td=9
        te=8
        tf=8
        tg=8
        th=8
        ti=8
        tj=8
        tk=8
    elif handle==3:
        ta=11
        tb=10
        tc=9
        td=9
        te=8
        tf=8
        tg=8
        th=8
        ti=8
        tj=8
        tk=8
    elif handle==2:
        ta=16
        tb=13
        tc=10
        td=10
        te=9
        tf=9
        tg=8
        th=8
        ti=8
        tj=8
        tk=8
    elif handle==1:
        ta=16
        tb=16
        tc=11
        td=10
        te=9
        tf=9
        tg=8
        th=8
        ti=8
        tj=8
        tk=8
    elif handle==0:
        ta=16
        tb=16
        tc=16
        td=10
        te=9
        tf=9
        tg=8
        th=8
        ti=8
        tj=8
        tk=8
    
    
    for j in range(8,24):
####        if matrix[0][j+ta-8]==0:
####            pygame.draw.circle(screen,BLACK,[(j-8)*20+10,210],10)
####        elif matrix[0][j+ta-8]==1:
####            pygame.draw.circle(screen,RED  ,[(j-8)*20+10,210],10)
####        elif matrix[0][j+ta-8]==2:
####            pygame.draw.circle(screen,GREEN,[(j-8)*20+10,210],10)
####        elif matrix[0][j+ta-8]==3:
####            pygame.draw.circle(screen,YELLO,[(j-8)*20+10,210],10)
####        elif matrix[0][j+ta-8]==4:
####            pygame.draw.circle(screen,BLUE ,[(j-8)*20+10,210],10)
####        elif matrix[0][j+ta-8]==5:
####            pygame.draw.circle(screen,PINK ,[(j-8)*20+10,210],10)
####        elif matrix[0][j+ta-8]==6:
####            pygame.draw.circle(screen,CYAN ,[(j-8)*20+10,210],10)
####        elif matrix[0][j+ta-8]==7:
####            pygame.draw.circle(screen,WHITE,[(j-8)*20+10,210],10)
        LMD.set_pixel(0,j, matrix[0][j+ta-8])
##
    for j in range(8,24):
####        if matrix[1][j+tb-8]==0:
####            pygame.draw.circle(screen,BLACK,[(j-8)*20+10,230],10)
####        elif matrix[1][j+tb-8]==1:
####            pygame.draw.circle(screen,RED  ,[(j-8)*20+10,230],10)
####        elif matrix[1][j+tb-8]==2:
####            pygame.draw.circle(screen,GREEN,[(j-8)*20+10,230],10)
####        elif matrix[1][j+tb-8]==3:
####            pygame.draw.circle(screen,YELLO,[(j-8)*20+10,230],10)
####        elif matrix[1][j+tb-8]==4:
####            pygame.draw.circle(screen,BLUE ,[(j-8)*20+10,230],10)
####        elif matrix[1][j+tb-8]==5:
####            pygame.draw.circle(screen,PINK ,[(j-8)*20+10,230],10)
####        elif matrix[1][j+tb-8]==6:
####            pygame.draw.circle(screen,CYAN ,[(j-8)*20+10,230],10)
####        elif matrix[1][j+tb-8]==7:
####            pygame.draw.circle(screen,WHITE,[(j-8)*20+10,230],10)
        LMD.set_pixel(1,j, matrix[1][j+tb-8])
##
    for j in range(8,24):
####        if matrix[2][j+tc-8]==0:
####            pygame.draw.circle(screen,BLACK,[(j-8)*20+10,250],10)
####        elif matrix[2][j+tc-8]==1:
####            pygame.draw.circle(screen,RED  ,[(j-8)*20+10,250],10)
####        elif matrix[2][j+tc-8]==2:
####            pygame.draw.circle(screen,GREEN,[(j-8)*20+10,250],10)
####        elif matrix[2][j+tc-8]==3:
####            pygame.draw.circle(screen,YELLO,[(j-8)*20+10,250],10)
####        elif matrix[2][j+tc-8]==4:
####            pygame.draw.circle(screen,BLUE ,[(j-8)*20+10,250],10)
####        elif matrix[2][j+tc-8]==5:
####            pygame.draw.circle(screen,PINK ,[(j-8)*20+10,250],10)
####        elif matrix[2][j+tc-8]==6:
####            pygame.draw.circle(screen,CYAN ,[(j-8)*20+10,250],10)
####        elif matrix[2][j+tc-8]==7:
####            pygame.draw.circle(screen,WHITE,[(j-8)*20+10,250],10)
        LMD.set_pixel(2,j, matrix[2][j+tc-8])
##
    for j in range(8,24):
####        if matrix[3][j+td-8]==0:
####            pygame.draw.circle(screen,BLACK,[(j-8)*20+10,270],10)
####        elif matrix[3][j+td-8]==1:
####            pygame.draw.circle(screen,RED  ,[(j-8)*20+10,270],10)
####        elif matrix[3][j+td-8]==2:
####            pygame.draw.circle(screen,GREEN,[(j-8)*20+10,270],10)
####        elif matrix[3][j+td-8]==3:
####            pygame.draw.circle(screen,YELLO,[(j-8)*20+10,270],10)
####        elif matrix[3][j+td-8]==4:
####            pygame.draw.circle(screen,BLUE ,[(j-8)*20+10,270],10)
####        elif matrix[3][j+td-8]==5:
####            pygame.draw.circle(screen,PINK ,[(j-8)*20+10,270],10)
####        elif matrix[3][j+td-8]==6:
####            pygame.draw.circle(screen,CYAN ,[(j-8)*20+10,270],10)
####        elif matrix[3][j+td-8]==7:
####            pygame.draw.circle(screen,WHITE,[(j-8)*20+10,270],10)
        LMD.set_pixel(3,j, matrix[3][j+td-8])
##
    for j in range(8,24):
####        if matrix[4][j+te-8]==0:
####            pygame.draw.circle(screen,BLACK,[(j-8)*20+10,290],10)
####        elif matrix[4][j+te-8]==1:
####            pygame.draw.circle(screen,RED  ,[(j-8)*20+10,290],10)
####        elif matrix[4][j+te-8]==2:
####            pygame.draw.circle(screen,GREEN,[(j-8)*20+10,290],10)
####        elif matrix[4][j+te-8]==3:
####            pygame.draw.circle(screen,YELLO,[(j-8)*20+10,290],10)
####        elif matrix[4][j+te-8]==4:
####            pygame.draw.circle(screen,BLUE ,[(j-8)*20+10,290],10)
####        elif matrix[4][j+te-8]==5:
####            pygame.draw.circle(screen,PINK ,[(j-8)*20+10,290],10)
####        elif matrix[4][j+te-8]==6:
####            pygame.draw.circle(screen,CYAN ,[(j-8)*20+10,290],10)
####        elif matrix[4][j+te-8]==7:
####            pygame.draw.circle(screen,WHITE,[(j-8)*20+10,290],10)
        LMD.set_pixel(4,j, matrix[4][j+te-8])
##
    for j in range(8,24):
####        if matrix[5][j+tf-8]==0:
####            pygame.draw.circle(screen,BLACK,[(j-8)*20+10,310],10)
####        elif matrix[5][j+tf-8]==1:
####            pygame.draw.circle(screen,RED  ,[(j-8)*20+10,310],10)
####        elif matrix[5][j+tf-8]==2:
####            pygame.draw.circle(screen,GREEN,[(j-8)*20+10,310],10)
####        elif matrix[5][j+tf-8]==3:
####            pygame.draw.circle(screen,YELLO,[(j-8)*20+10,310],10)
####        elif matrix[5][j+tf-8]==4:
####            pygame.draw.circle(screen,BLUE ,[(j-8)*20+10,310],10)
####        elif matrix[5][j+tf-8]==5:
####            pygame.draw.circle(screen,PINK ,[(j-8)*20+10,310],10)
####        elif matrix[5][j+tf-8]==6:
####            pygame.draw.circle(screen,CYAN ,[(j-8)*20+10,310],10)
####        elif matrix[5][j+tf-8]==7:
####            pygame.draw.circle(screen,WHITE,[(j-8)*20+10,310],10)
        LMD.set_pixel(5,j, matrix[5][j+tf-8])
##
    for j in range(8,24):
####        if matrix[6][j+tg-8]==0:
####            pygame.draw.circle(screen,BLACK,[(j-8)*20+10,330],10)
####        elif matrix[6][j+tg-8]==1:
####            pygame.draw.circle(screen,RED  ,[(j-8)*20+10,330],10)
####        elif matrix[6][j+tg-8]==2:
####            pygame.draw.circle(screen,GREEN,[(j-8)*20+10,330],10)
####        elif matrix[6][j+tg-8]==3:
####            pygame.draw.circle(screen,YELLO,[(j-8)*20+10,330],10)
####        elif matrix[6][j+tg-8]==4:
####            pygame.draw.circle(screen,BLUE ,[(j-8)*20+10,330],10)
####        elif matrix[6][j+tg-8]==5:
####            pygame.draw.circle(screen,PINK ,[(j-8)*20+10,330],10)
####        elif matrix[6][j+tg-8]==6:
####            pygame.draw.circle(screen,CYAN ,[(j-8)*20+10,330],10)
####        elif matrix[6][j+tg-8]==7:
####            pygame.draw.circle(screen,WHITE,[(j-8)*20+10,330],10)
        LMD.set_pixel(6,j, matrix[6][j+tg-8])
##            
    for j in range(8,24):
####        if matrix[7][j+th-8]==0:
####            pygame.draw.circle(screen,BLACK,[(j-8)*20+10,350],10)
####        elif matrix[7][j+th-8]==1:
####            pygame.draw.circle(screen,RED  ,[(j-8)*20+10,350],10)
####        elif matrix[7][j+th-8]==2:
####            pygame.draw.circle(screen,GREEN,[(j-8)*20+10,350],10)
####        elif matrix[7][j+th-8]==3:
####            pygame.draw.circle(screen,YELLO,[(j-8)*20+10,350],10)
####        elif matrix[7][j+th-8]==4:
####            pygame.draw.circle(screen,BLUE ,[(j-8)*20+10,350],10)
####        elif matrix[7][j+th-8]==5:
####            pygame.draw.circle(screen,PINK ,[(j-8)*20+10,350],10)
####        elif matrix[7][j+th-8]==6:
####            pygame.draw.circle(screen,CYAN ,[(j-8)*20+10,350],10)
####        elif matrix[7][j+th-8]==7:
####            pygame.draw.circle(screen,WHITE,[(j-8)*20+10,350],10)
        LMD.set_pixel(7,j, matrix[7][j+th-8])
##
    for j in range(8,24):
####        if matrix[8][j+ti-8]==0:
####            pygame.draw.circle(screen,BLACK,[(j-8)*20+10,370],10)
####        elif matrix[8][j+ti-8]==1:
####            pygame.draw.circle(screen,RED  ,[(j-8)*20+10,370],10)
####        elif matrix[8][j+ti-8]==2:
####            pygame.draw.circle(screen,GREEN,[(j-8)*20+10,370],10)
####        elif matrix[8][j+ti-8]==3:
####            pygame.draw.circle(screen,YELLO,[(j-8)*20+10,370],10)
####        elif matrix[8][j+ti-8]==4:
####            pygame.draw.circle(screen,BLUE ,[(j-8)*20+10,370],10)
####        elif matrix[8][j+ti-8]==5:
####            pygame.draw.circle(screen,PINK ,[(j-8)*20+10,370],10)
####        elif matrix[8][j+ti-8]==6:
####            pygame.draw.circle(screen,CYAN ,[(j-8)*20+10,370],10)
####        elif matrix[8][j+ti-8]==7:
####            pygame.draw.circle(screen,WHITE,[(j-8)*20+10,370],10)
        LMD.set_pixel(8,j, matrix[8][j+ti-8])
##
    for j in range(8,24):
####        if matrix[9][j+tj-8]==0:
####            pygame.draw.circle(screen,BLACK,[(j-8)*20+10,390],10)
####        elif matrix[9][j+tj-8]==1:
####            pygame.draw.circle(screen,RED  ,[(j-8)*20+10,390],10)
####        elif matrix[9][j+tj-8]==2:
####            pygame.draw.circle(screen,GREEN,[(j-8)*20+10,390],10)
####        elif matrix[9][j+tj-8]==3:
####            pygame.draw.circle(screen,YELLO,[(j-8)*20+10,390],10)
####        elif matrix[9][j+tj-8]==4:
####            pygame.draw.circle(screen,BLUE ,[(j-8)*20+10,390],10)
####        elif matrix[9][j+tj-8]==5:
####            pygame.draw.circle(screen,PINK ,[(j-8)*20+10,390],10)
####        elif matrix[9][j+tj-8]==6:
####            pygame.draw.circle(screen,CYAN ,[(j-8)*20+10,390],10)
####        elif matrix[9][j+tj-8]==7:
####            pygame.draw.circle(screen,WHITE,[(j-8)*20+10,390],10)
        LMD.set_pixel(9,j, matrix[9][j+tj-8])
##            
    for j in range(8,24):
####        if matrix[11][j+tk-8]==0:
####            pygame.draw.circle(screen,BLACK,[(j-8)*20+10,410],10)
####        elif matrix[11][j+tk-8]==1:
####            pygame.draw.circle(screen,RED  ,[(j-8)*20+10,410],10)
####        elif matrix[11][j+tk-8]==2:
####            pygame.draw.circle(screen,GREEN,[(j-8)*20+10,410],10)
####        elif matrix[11][j+tk-8]==3:
####            pygame.draw.circle(screen,YELLO,[(j-8)*20+10,410],10)
####        elif matrix[11][j+tk-8]==4:
####            pygame.draw.circle(screen,BLUE ,[(j-8)*20+10,410],10)
####        elif matrix[11][j+tk-8]==5:
####            pygame.draw.circle(screen,PINK ,[(j-8)*20+10,410],10)
####        elif matrix[11][j+tk-8]==6:
####            pygame.draw.circle(screen,CYAN ,[(j-8)*20+10,410],10)
####        elif matrix[11][j+tk-8]==7:
####            pygame.draw.circle(screen,WHITE,[(j-8)*20+10,410],10)
        LMD.set_pixel(10,j, matrix[10][j+tk-8])
##        
    for i in range(11,22):
        for j in range(8,24):
####            if matrix[i][j]==0:
####                pygame.draw.circle(screen,BLACK,[(j-8)*20+10,(i+11)*20-10],10)
####            elif matrix[i][j]==1:
####                pygame.draw.circle(screen,RED  ,[(j-8)*20+10,(i+11)*20-10],10)
####            elif matrix[i][j]==2:
####                pygame.draw.circle(screen,GREEN,[(j-8)*20+10,(i+11)*20-10],10)
####            elif matrix[i][j]==3:
####                pygame.draw.circle(screen,YELLO,[(j-8)*20+10,(i+11)*20-10],10)
####            elif matrix[i][j]==4:
####                pygame.draw.circle(screen,BLUE ,[(j-8)*20+10,(i+11)*20-10],10)
####            elif matrix[i][j]==5:
####                pygame.draw.circle(screen,PINK ,[(j-8)*20+10,(i+11)*20-10],10)
####            elif matrix[i][j]==6:
####                pygame.draw.circle(screen,CYAN ,[(j-8)*20+10,(i+11)*20-10],10)
####            elif matrix[i][j]==7:
####                pygame.draw.circle(screen,WHITE,[(j-8)*20+10,(i+11)*20-10],10)
            LMD.set_pixel(i,j, matrix[i][j])


matrix=[[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2],
        [4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2],
        [4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2],
        [4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2],
        [4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2],
        [4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2],
        [4,4,4,4,4,4,4,4,4,0,3,3,3,3,3,3,3,3,3,3,3,3,0,2,2,2,2,2,2,2,2,2],
        [8,8,8,8,8,8,8,8,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,0,0,7,7,7,7,0,0,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,0,7,0,0,0,0,7,0,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,7,0,0,0,0,0,0,7,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,7,7,7,7,7,7,7,7,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,7,0,0,7,7,0,0,7,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,7,0,0,7,7,0,0,7,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,0,7,0,7,7,0,7,0,0,0,0,0,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,0,0,0,0,0,0,7,7,7,7,0,0,0,0,0,0,8,8,8,8,8,8,8,8],]

roadMap=[8,8,7,7,6,6,5,5,4,4,3,3,2,2,
         2,2,3,3,4,4,5,5,6,6,7,7,8,8,
         8,8,9,9,10,10,11,11,12,12,
         12,12,11,11,10,10,9,9,8,8]
tt=0



BLACK= (  0,  0,  0)    #0
RED  = (255,  0,  0)    #1
GREEN= ( 0, 255,  0)    #2
YELLO= (255,255,  0)    #3
BLUE = (  0,  0,255)    #4
PINK = (255,  0,255)    #5
CYAN = (  0,255,255)    #6
WHITE= (255,255,255)    #7


 
LED_init()
  
done= False
handle=8
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                pygame.quit()
                sys.exit()

##    screen.fill(BLACK)

    if roadMap[tt//5]>handle:
        if handle<14:
            handle+=1
    elif roadMap[tt//5]<handle:
        if handle>0:
            handle-=1

    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            if handle>1:
                handle-=1
        elif event.key==pygame.K_LEFT:
            if handle<14:
                handle+=1

    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            if handle>1:
                handle-=1
        elif event.key==pygame.K_LEFT:
            if handle<14:
                handle+=1
                
    drive(handle)
    tt+=1
    if tt>185:
        tt=0
    if handle==13 or handle==1:
        for i in range(32):
            for j in range(16):
                LMD.set_pixel(j,i,1)
        print("Game Over")
##        pygame.quit()
        break
    
    pygame.display.update()
    clock.tick(15)
