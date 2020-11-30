from matrix import *
import pygame
import random
import time
import sys
import LED_display as LMD
import threading

#게임 초기화
#pygame.init()
#게임창 옵션 설정, pygame관련 설정들
WINDOWWIDTH = 480
WINBOWHEIGHT = 800
#screen = pygame.display.set_mode((500, 500))
done = False
#title = "Mole game"
#pygame.display.set_caption(title) #게임 이름

clock = pygame.time.Clock()
#기본 설정
color = (0,0,0)
black = (0,0,0)
white = (255,255,255)
BLUE = (0,0,155)
x, y = 450, 250
x1, y1 = 450, 250

#g_Point =[ [125,375], [250,375], [375,375],[125,250],[250,250],[375,250],[375,125],[250,125],[125,125]]
g_Point  = [[8, 1],[8,5], [8,9],
            [14, 1], [14,5], [14,9],
            [20,1],[20, 5],[20, 9]]

#mole1 =pygame.image.load("망1.png")
#mole1 = pygame.transform.scale(mole1, (50,50))
#mole1_width = mole1.get_rect().size[0]
#mole1_height = mole1.get_rect().size[1]
#mole2 =pygame.image.load("망2.png")
#mole2 = pygame.transform.scale(mole2,(50,50))
#mole4 = pygame.image.load("두더지.png")
#mole4 = pygame.transform.scale(mole4,(30,30))
#mole4_width = mole4.get_rect().size[0]
#mole4_height = mole4.get_rect().size[1]
#led화면관련 기본설정들

iscreen = [[ 0 for x in range (16)] for x in range (32)]
#빈화면
arrayScreen = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]
#게임화면
gameScreen = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0],
    [7,0,0,7,7,0,0,7,7,0,0,7,0,0,0,0],
    [7,0,0,7,7,0,0,7,7,0,0,7,0,0,0,0],
    [7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0],
    [7,0,0,7,7,0,0,7,7,0,0,7,0,0,0,0],
    [7,0,0,7,7,0,0,7,7,0,0,7,0,0,0,0],
    [7,7,7,7,7,7,7,7,7,7,7,7,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0],
    [7,0,0,7,7,0,0,7,7,0,0,7,0,0,0,0],
    [7,0,0,7,7,0,0,7,7,0,0,7,0,0,0,0],
    [7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]

endScreen = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,3,3,3,3,0,0,0,0,0,0,0,3,0,0],
    [0,0,3,0,0,0,0,0,0,0,0,0,0,3,0,0],
    [0,0,3,3,3,3,0,3,3,3,0,3,3,3,0,0],
    [0,0,3,0,0,0,0,3,0,3,0,3,0,3,0,0],
    [0,0,3,3,3,3,0,3,0,3,0,3,3,3,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]
mole_led = [[4,4],[4,4]]
moletop = 0
moleleft = 0
hammerledup =[[5,5,5],[5,5,5],[0,5,0]]
hammerleddown = [[5,5,0],[5,5,5],[5,5,0]]
hammertop =13
hammerleft =13
hammerstyle = hammerledup
#text_level = myFont.render("Level %d" %level, True, BLUE)
#text_s = myFont.render("score %d" %score, True, BLUE)
#end_message = myFont.render("Game over", True, BLUE)
#각종 입력 감지           
          
#pygame.event.get() 각종 입력을 실시간으로 받을수있게함
#for을 쓰는 이유는 여러입력이 동시에 들어왔을때를 고려
#LED 패널 출력

def draw_matrix(m):
    for y in range(len(m[0])):
        for x in range(len(m)):
            if m[x][y] == 0:
                LMD.set_pixel(x, y, 0)
            elif m[x][y] == 1:
                LMD.set_pixel(x, y, 1)
            elif m[x][y] == 2:
                LMD.set_pixel(x, y, 2)
            elif m[x][y] == 3:
                LMD.set_pixel(x, y, 3)
            elif m[x][y] == 4:
                LMD.set_pixel(x, y, 4)
            elif m[x][y] == 5:
                LMD.set_pixel(x, y, 1)
            elif m[x][y] == 6:
                LMD.set_pixel(x, y, 6)
            elif m[x][y] == 7:
                LMD.set_pixel(x, y, 7)
            elif m[x][y] == 9:
                LMD.set_pixel(x, y, 1)
            else:
                continue
        print()
#0 무색, 1 빨강, 2그린 3 노랑 4 파랑 5 분홍 6 하늘 7 흰색
#그리기
#screen.fill(color)
#pygame.display.flip() #게임화면 업데이트
#led
def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return
#두더지
def mole():
    ran = g_Point[random.randint(0, 8)]
    a = ran[0]
    b = ran[1]
    #enemy = pygame.Rect(a,b,30,30)
    #pygame.draw.rect(screen, BLUE, enemy)
    #screen.blit(mole4, [a,b])
    
    return a, b

#망치

#def Hammer(x , y):
 #   if (x == 450 and y == 250):
  #      screen.blit(mole2, [x,y])
   # else:
    #    screen.blit(mole1, [x,y])

#충돌
def bre(m, score1):
    for y in range(len(m[0])):
        for x in range(len(m)):
            if (m[x][y] == 9):
                score1 += 1
                return score1
    return score1
#레벨 올리기
def level_check(score1, level1, timec, checkscore, checktime,speed):
    if (score >checkscore):
        level1 +=1
        score1 = 0
        timec = 0
        checkscore += 5
        #screen.blit(myFont.render("Level %d" %level, True, white), [250, 50])
    if (level1 % 5 ==0):
        checkscore = 5
        checktime -= 5
    if(level1 % 10 ==0):
        speed += 10
    return score1, level1, timec, checkscore, checktime,speed

#시간정하기
def time_check(time):
    if time> 1:
        time = 0
#게임 연습
level = 1
score = 0
speed = 10
timec = 0
checktime = 50
checkscore = 5
check = True
iScreen = Matrix(gameScreen)
LED_init()
while check:
    start = time.time()
    dt = clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                x1 , y1 = 125,375
                hammertop, hammerleft = 20, 1
                hammerstyle = hammerleddown
            if event.key == pygame.K_2:
                hammerstyle = hammerleddown
                hammertop, hammerleft = 20, 5
            if event.key == pygame.K_3:
                hammerstyle = hammerleddown
                hammertop, hammerleft = 20, 9
            if event.key == pygame.K_4:
                hammerstyle = hammerleddown
                hammertop, hammerleft = 14, 1
            if event.key == pygame.K_5:
                hammerstyle = hammerleddown
                hammertop, hammerleft = 14, 5
            if event.key == pygame.K_6:
                hammerstyle = hammerleddown
                hammertop, hammerleft = 14, 9
            if event.key == pygame.K_7:
                hammerstyle = hammerleddown
                hammertop, hammerleft = 8, 1
            if event.key == pygame.K_8:
                hammerstyle = hammerleddown
                hammertop, hammerleft = 8, 1
            if event.key == pygame.K_9:
                hammerstyle = hammerleddown
                hammertop, hammerleft = 8, 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                hammertop, hammerleft = 13, 13
                hammerstyle = hammerledup
            if event.key == pygame.K_2:
                hammertop, hammerleft = 13, 13
                hammerstyle = hammerledup
            if event.key == pygame.K_3:
                hammertop, hammerleft = 13, 13
                hammerstyle = hammerledup
            if event.key == pygame.K_4:
                hammerstyle = hammerledup
                hammertop, hammerleft = 13, 13
            if event.key == pygame.K_5:
                hammertop, hammerleft = 13, 13
                hammerstyle = hammerledup
            if event.key == pygame.K_6:
                hammertop, hammerleft = 13, 13
                hammerstyle = hammerledup
            if event.key == pygame.K_7:
                hammertop, hammerleft = 13, 13
                hammerstyle = hammerledup
            if event.key == pygame.K_8:
                hammertop, hammerleft = 13, 13
                hammerstyle = hammerledup
            if event.key == pygame.K_9:
                hammertop, hammerleft = 13, 13
                hammerstyle = hammerledup

    
    #pygame.display.flip()
    iScreen = Matrix(gameScreen)
    oScreen = Matrix(iScreen)
    currBlk = Matrix(hammerstyle)
    tempBlk = iScreen.clip(hammertop, hammerleft, hammertop+currBlk.get_dy(), hammerleft+currBlk.get_dx())
    tempBlk = tempBlk+ currBlk
    oScreen.paste(tempBlk, hammertop, hammerleft)
    moletop, moleleft = mole()
    moleBlk = Matrix(mole_led)
    moleeBlk = iScreen.clip(moletop, moleleft, moletop+moleBlk.get_dy(), moleleft+moleBlk.get_dx())
    moleeBlk = moleeBlk+moleBlk
    oScreen.paste(moleeBlk, moletop, moleleft)
    draw_matrix(oScreen); print()

    score = bre(oScreen, score)
    
    #score = bre(a,b,x,y, score)
    #rect 정보 업데이트
    #mole11  = pygame.Rect(x1, y1, 50, 50)
    #mole44= pygame.Rect(a, b, 30, 30)
    #mole1_rect = mole1.get_rect()
    #mole1_rect.left = x1
    #mole1_rect.top = y1
    #mole4_rect = mole4.get_rect()
    #mole4_rect.left = a
    #mole4_rect.top = b
    #if mole4_rect.colliderect(mole1_rect):
        #score += 1
    #if (x1+mole1_width > a) and (x1<a+mole4_width) and (y1 < b + mole4_height)and(y1+mole1_height > b):
        #score += 1
    
    #score, level = level_check(score, level)
    score, level, timec, checkscore, checktime,speed = level_check(score, level, timec, checkscore, checktime,speed)
    #screen.blit(myFont.render("score %d Level %d"  %(score,level), True,white), [50, 50])
    #s = myFont.render("score {} Level {} target score {}".format(int(score),int(level), int(checkscore)),True,white)
    #screen.blit(s, [50, 50])
    #pygame.display.update()
    end = time.time()
    timec += (end - start)
    #timer = myFont.render("Time : {}".format(int(checktime-timec)),True,white)
    #screen.blit(timer, [300, 50])
    #s = myFont.render("score {} Level {} target score {} Time : {}".format(int(score),int(level), int(checkscore),int(checktime-timec)),True,white)
    #screen.blit(s, [50, 50])
    clock.tick(speed)
    
    if (timec> checktime):
        endScreen = Matrix(endScreen)
        draw_matrix(endScreen); print()
        time.sleep(1)
        #screen.fill(black)
        #screen.blit(end_message, [200, 250])
        #pygame.display.update()
        check = False

#pygame.time.delay(2000)
#pygame.quit()
#while True:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #pygame.quit()
            #sys.exit()
    #screen.fill(black)
    #screen.blit(end_message, [200, 250])

