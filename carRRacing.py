import pygame
import sys
from pygame.locals import *
import RPi.GPIO as GPIO
import time

#r36 r32 r26 r21 r15 r8 r3


delay = 0.000001

GPIO.setmode(GPIO.BCM)
red1_pin = 11
green1_pin = 27
blue1_pin = 7
red2_pin = 8
green2_pin = 9
blue2_pin = 10
clock_pin = 17
a_pin = 22
b_pin = 23
c_pin = 24
latch_pin = 4
oe_pin = 18

GPIO.setup(red1_pin, GPIO.OUT)
GPIO.setup(green1_pin, GPIO.OUT)
GPIO.setup(blue1_pin, GPIO.OUT)
GPIO.setup(red2_pin, GPIO.OUT)
GPIO.setup(green2_pin, GPIO.OUT)
GPIO.setup(blue2_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(a_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.OUT)
GPIO.setup(c_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)
GPIO.setup(oe_pin, GPIO.OUT)

screen = [[0 for x in range(32)] for x in range(16)]

def clock():
    GPIO.output(clock_pin, 1)
    GPIO.output(clock_pin, 0)

def latch():
    GPIO.output(latch_pin, 1)
    GPIO.output(latch_pin, 0)

def bits_from_int(x):
    a_bit = x & 1
    b_bit = x & 2
    c_bit = x & 4
    return (a_bit, b_bit, c_bit)

def set_row(row):
    #time.sleep(delay)
    a_bit, b_bit, c_bit = bits_from_int(row)
    GPIO.output(a_pin, a_bit)
    GPIO.output(b_pin, b_bit)
    GPIO.output(c_pin, c_bit)
    #time.sleep(delay)

def set_color_top(color):
    #time.sleep(delay)
    red, green, blue = bits_from_int(color)
    GPIO.output(red1_pin, red)
    GPIO.output(green1_pin, green)
    GPIO.output(blue1_pin, blue)
    #time.sleep(delay)

def set_color_bottom(color):
    #time.sleep(delay)
    red, green, blue = bits_from_int(color)
    GPIO.output(red2_pin, red)
    GPIO.output(green2_pin, green)
    GPIO.output(blue2_pin, blue)
    #time.sleep(delay)

def refresh():
    for row in range(8):
        GPIO.output(oe_pin, 1)
        set_color_top(0)
        set_row(row)
        #time.sleep(delay)
        for col in range(32):
            set_color_top(screen[row][col])
            set_color_bottom(screen[row+8][col])
            clock()
        #GPIO.output(oe_pin, 0)
        latch()
        GPIO.output(oe_pin, 0)
        time.sleep(delay)


def set_pixel(x, y, color):
    screen[y][x] = color
    refresh()

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
        set_pixel(j, 0, matrix[0][j+ta-8])
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
        set_pixel(j, 1, matrix[0][j+tb-8])
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
        set_pixel(j, 2, matrix[0][j+tc-8])
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
        set_pixel(j, 3, matrix[0][j+td-8])
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
        set_pixel(j, 4, matrix[0][j+te-8])
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
        set_pixel(j, 5, matrix[0][j+tf-8])
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
        set_pixel(j, 6, matrix[0][j+tg-8])
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
        set_pixel(j, 7, matrix[0][j+th-8])
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
        set_pixel(j, 8, matrix[0][j+ti-8])
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
        set_pixel(j, 9, matrix[0][j+tj-8])
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
        set_pixel(j, 10, matrix[0][j+tk-8])
##        
    for i in range(11,22):
##        for j in range(8,24):
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
            set_pixel(j, i, matrix[0][j])


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

pygame.init()

BLACK= (  0,  0,  0)    #0
RED  = (255,  0,  0)    #1
GREEN= ( 0, 255,  0)    #2
YELLO= (255,255,  0)    #3
BLUE = (  0,  0,255)    #4
PINK = (255,  0,255)    #5
CYAN = (  0,255,255)    #6
WHITE= (255,255,255)    #7


 
size  = [320,640]
screen= pygame.display.set_mode(size)
  
pygame.display.set_caption("Jiney Racing 2020")
  
done= False
handle=8
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

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
        screen.fill(WHITE)
        print("Game Over")
        pygame.quit()
        break
    
    pygame.display.update()
    clock.tick(15)
