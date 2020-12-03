from matrix import *
import pygame
import sys
import LED_display as LMD
import threading
import time
import random

def molegame():
    #게임 초기화
    #pygame.init()
    #게임창 옵션 설정, pygame관련 설정들
    WINDOWWIDTH = 480
    WINBOWHEIGHT = 800
    screen = pygame.display.set_mode((500, 500))
    done = False
    title = "Mole game"
    pygame.display.set_caption(title) #게임 이름

    clock = pygame.time.Clock()
    #기본 설정
    color = (0,0,0)
    black = (0,0,0)
    white = (255,255,255)
    BLUE = (0,0,155)
    x, y = 450, 250
    x1, y1 = 450, 250

    #g_Point =[ [125,375], [250,375], [375,375],[125,250],[250,250],[375,250],[375,125],[250,125],[125,125]]
    g_Point  = [[13, 8],[9,8], [5,8],
                [13, 14], [9,14], [5,14],
                [13,20],[9, 20],[5, 20]]

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

    #빈화면
    arrayScreen = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


    #게임화면

    gameScreen = [
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,7,7,7,7,0,0,7,7,7,7,0,0,7,7,7,7,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,7,0,0,7,0,0,7,0,0,7,0,0,7,0,0,7,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,7,0,0,7,0,0,7,0,0,7,0,0,7,0,0,7,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,7,7,7,7,0,0,7,7,7,7,0,0,7,7,7,7,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,7,7,7,7,0,0,7,7,7,7,0,0,7,7,7,7,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,7,0,0,7,0,0,7,0,0,7,0,0,7,0,0,7,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,7,0,0,7,0,0,7,0,0,7,0,0,7,0,0,7,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,7,7,7,7,0,0,7,7,7,7,0,0,7,7,7,7,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,7,7,7,7,0,0,7,7,7,7,0,0,7,7,7,7,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,7,0,0,7,0,0,7,0,0,7,0,0,7,0,0,7,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,7,0,0,7,0,0,7,0,0,7,0,0,7,0,0,7,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,7,7,7,7,0,0,7,7,7,7,0,0,7,7,7,7,0,0,0,0,0,0,0,0,0]]

    endScreen = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    mole_led = [[4,4],[4,4]]
    moletop = 0
    moleleft = 0
    hammerledup =[[5,5,0],[5,5,5],[5,5,0]]
    hammerleddown = [[0,5,0],[5,5,5],[5,5,5]]
    hammertop =0
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
        array = m.get_array()
        for y in range(32):
            for x in range(16):
                if array[x][y] == 0:
                    LMD.set_pixel(y, x, 0)
                elif array[x][y] == 1:
                    LMD.set_pixel(y, x, 1)
                elif array[x][y] == 2:
                    LMD.set_pixel(y, x, 2)
                elif array[x][y] == 3:
                    LMD.set_pixel(y, x, 3)
                elif array[x][y] == 4:
                    LMD.set_pixel(y, x, 4)
                elif array[x][y] == 5:
                    LMD.set_pixel(y, x, 5)
                elif array[x][y] == 6:
                    LMD.set_pixel(y, x, 6)
                elif array[x][y] == 7:
                    LMD.set_pixel(y, x, 7)
                elif array[x][y] == 9:
                    LMD.set_pixel(y, x, 1)
                elif array[x][y] == 12:
                    LMD.set_pixel(y, x, 5)
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
        array = m.get_array()
        for y in range(32):
            for x in range(16):
                if (array[x][y] == 9):
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
                    hammertop, hammerleft = 13, 20
                    hammerstyle = hammerleddown
                if event.key == pygame.K_2:
                    hammerstyle = hammerleddown
                    hammertop, hammerleft = 9, 20
                if event.key == pygame.K_3:
                    hammerstyle = hammerleddown
                    hammertop, hammerleft = 5, 20
                if event.key == pygame.K_4:
                    hammerstyle = hammerleddown
                    hammertop, hammerleft = 13, 14
                if event.key == pygame.K_5:
                    hammerstyle = hammerleddown
                    hammertop, hammerleft = 9, 14
                if event.key == pygame.K_6:
                    hammerstyle = hammerleddown
                    hammertop, hammerleft = 5, 14
                if event.key == pygame.K_7:
                    hammerstyle = hammerleddown
                    hammertop, hammerleft = 13, 8
                if event.key == pygame.K_8:
                    hammerstyle = hammerleddown
                    hammertop, hammerleft = 9, 8
                if event.key == pygame.K_9:
                    hammerstyle = hammerleddown
                    hammertop, hammerleft = 5, 8
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    hammertop, hammerleft = 0, 13
                    hammerstyle = hammerledup
                if event.key == pygame.K_2:
                    hammertop, hammerleft = 0, 13
                    hammerstyle = hammerledup
                if event.key == pygame.K_3:
                    hammertop, hammerleft = 0, 13
                    hammerstyle = hammerledup
                if event.key == pygame.K_4:
                    hammerstyle = hammerledup
                    hammertop, hammerleft = 0, 13
                if event.key == pygame.K_5:
                    hammertop, hammerleft = 0, 13
                    hammerstyle = hammerledup
                if event.key == pygame.K_6:
                    hammertop, hammerleft = 0, 13
                    hammerstyle = hammerledup
                if event.key == pygame.K_7:
                    hammertop, hammerleft = 0, 13
                    hammerstyle = hammerledup
                if event.key == pygame.K_8:
                    hammertop, hammerleft = 0, 13
                    hammerstyle = hammerledup
                if event.key == pygame.K_9:
                    hammertop, hammerleft = 0, 13
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
#             time.sleep(2)
            #screen.fill(black)
            #screen.blit(end_message, [200, 250])
            #pygame.display.update()
            check = False
            break

    #pygame.time.delay(2000)
    #pygame.quit()
    #while True:
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #pygame.quit()
                #sys.exit()
        #screen.fill(black)
        #screen.blit(end_message, [200, 250])
    pygame.quit()

def snakeGame():
    pygame.init()
    def LED_init():
        thread=threading.Thread(target=LMD.main, args=())
        thread.setDaemon(True)
        thread.start()
        return
    LED_init()
     
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
     
    dis_width = 160
    dis_height = 320
     
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game by Edureka')
     
    clock = pygame.time.Clock()
     
    snake_block = 10
    snake_speed = 15
     
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)
     
     
    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, yellow)
        dis.blit(value, [0, 0])
     
     
     
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
            if int(x[1]/10)>=0 and int(x[1]/10)<32:
                if int(x[0]/10)>=0 and int(x[0]/10)<16:
                    LMD.set_pixel(int(x[1]/10),15-int(x[0]/10),6)
            print(x[0],end=' ')
            print(x[1])
     
     
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])
     
     
    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2
     
        x1_change = 0
        y1_change = 0
     
        snake_List = []
        Length_of_snake = 1
     
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
     
        while not game_over:
            for i in range(32):
                for j in range(16):
                    LMD.set_pixel(i,j,0)
     
            while game_close == True:
#                 dis.fill(blue)
#                 message("C-Play Again or Q-Quit", red)
                Your_score(Length_of_snake - 1)
                pygame.display.update()
                game_over = True
                game_close = False
#                 for event in pygame.event.get():
#                     if event.type == pygame.KEYDOWN:
#                         if event.key == pygame.K_q:
#                             game_over = True
#                             game_close = False
#                         if event.key == pygame.K_c:
#                             gameLoop()
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
     
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            LMD.set_pixel(int(foody/10),15-int(foodx/10),3)
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
     
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
     
            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)
     
            pygame.display.update()
     
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1
     
            clock.tick(snake_speed)
        endScreen = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        for i in range(32):
            for j in range(16):
                LMD.set_pixel(i,j,endScreen[j][i])
        pygame.quit()
     
     
    gameLoop()

def tetris():
    def LED_init():
        thread=threading.Thread(target=LMD.main, args=())
        thread.setDaemon(True)
        thread.start()
        return

    def draw_matrix(m):
        array = m.get_array()
        for y in range(m.get_dy()-4):
            for x in range(4, m.get_dx()-4):
                if array[y][x] == 0:
                    print("□", end='')
                    LMD.set_pixel(y, 19-x, 0)
                elif array[y][x] == 1:
                    print("■", end='')
                    LMD.set_pixel(y, 19-x, 4)
                else:
                    print("XX", end='')
                    continue
            print()

    def deleteFullLines(s,b,top,dy,dx,dw):
        global score
        if b == None :
            return s
        nDeleted = 0
        nScanned = b.get_dy()
        if top + b.get_dy() -1 >= dy :
            nScanned -= (top+b.get_dy()-dy)
        zero = Matrix(dx-2*dw)
        for y in range(nScanned-1,-1,-1):
            cy = top+y+nDeleted
            line = s.clip(cy,0,cy+1,s.get_dx())
            if line.sum() == s.get_dx() :
                temp = s.clip(0,0,cy,s.get_dx())
                s.paste(temp,1,0)
                s.paste(zero,0,dw)
                score += 1
                nDeleted = nDeleted +1
        return s

    def transpose(a):
        m = len(a)
        ret = [[0] * m for _ in range(m)]

        for r in range(m):
            for c in range(m):
                ret[c][m-1-r] = a[r][c]
        a=ret
        return a

    ###
    ### initialize variables
    ###     


    arrayBlk = [[ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ],
                [ [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 1 ]],
                [ [ 1,1],[1,1]],
                [ [ 0, 1, 0 ], [ 1, 1, 0 ], [ 0, 1, 0 ]],
                [ [ 0, 1, 0 ], [ 0, 1, 0 ], [ 1, 1, 0 ]],
                [ [ 0, 1, 1 ], [ 1, 1, 0 ], [ 0, 0, 0 ]],
                [ [ 1, 1, 0 ], [ 0, 1, 1 ], [ 0, 0, 0 ]]]

    ### integer variables: must always be integer!
    iScreenDy = 32
    iScreenDx = 16
    iScreenDw = 4
    top = 0
    left = iScreenDw + iScreenDx//2 - 2

    newBlockNeeded = False

    arrayScreen = [
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]]
    ###
    ### prepare the initial screen output
    ###  
    iScreen = Matrix(arrayScreen)
    oScreen = Matrix(iScreen)
    abc=random.randrange(0,7)# 시작할때 abc라는 수를 뽑아서
    currBlk = Matrix(arrayBlk[abc])
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    oScreen.paste(tempBlk, top, left)
    LED_init()
    draw_matrix(oScreen); print()
    start = int(time.time())
    aaa=(arrayBlk[abc])
    score = 0
    ###
    ### execute the loop
    ###

    while True:
        key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
        if key == 'q':
            print('Game terminated...')
            break
        elif key == 'a': # move left
            left -= 1
        elif key == 'd': # move right
            left += 1
        elif key == 's': # move down
            top += 1
        elif key == 'w': # rotate the block clockwise
            currBlk = Matrix(transpose(aaa))
            aaa=transpose(aaa)
        elif key == ' ': # drop the block
            while tempBlk.anyGreaterThan(1) == False:
                top += 1
                tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
                tempBlk = tempBlk + currBlk
        else:
            print('Wrong key!!!')
            continue

        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            if key == 'a': # undo: move right
                left += 1
            elif key == 'd': # undo: move left
                left -= 1
            elif key == 's': # undo: move up
                top -= 1
                newBlockNeeded = True
            elif key == 'w': # undo: rotate the block counter-clockwise
                for i in range(3):
                    aaa=transpose(aaa)
                currBlk = Matrix((aaa))
            elif key == ' ': # undo: move up
                top -= 1
                newBlockNeeded = True

            tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
            tempBlk = tempBlk + currBlk

        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()

        if newBlockNeeded:
            oScrean = deleteFullLines(oScreen, currBlk, top, iScreenDy, iScreenDx, iScreenDw)   
            iScreen = Matrix(oScreen)
            top = 0
            left = iScreenDw + iScreenDx//2 - 2
            newBlockNeeded = False
            abc=random.randrange(0,7)
            currBlk = Matrix(arrayBlk[abc])
            aaa=(arrayBlk[abc])
            tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
            tempBlk = tempBlk + currBlk
            if tempBlk.anyGreaterThan(1):
                print('Game Over!!!')
                break
            if score == 1:
                end = int(time.time())
                timespent = end - start
                print('You spent %d time!!!'%timespent)
                break
            oScreen = Matrix(iScreen)
            oScreen.paste(tempBlk, top, left)
            draw_matrix(oScreen); print()
            
    ###
    ### end of the loop
    ###
def carRRacing():
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
            LMD.set_pixel(0,j-8, matrix[0][j+ta-8])
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
            LMD.set_pixel(1,j-8, matrix[1][j+tb-8])
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
            LMD.set_pixel(2,j-8, matrix[2][j+tc-8])
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
            LMD.set_pixel(3,j-8, matrix[3][j+td-8])
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
            LMD.set_pixel(4,j-8, matrix[4][j+te-8])
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
            LMD.set_pixel(5,j-8, matrix[5][j+tf-8])
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
            LMD.set_pixel(6,j-8, matrix[6][j+tg-8])
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
            LMD.set_pixel(7,j-8, matrix[7][j+th-8])
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
            LMD.set_pixel(8,j-8, matrix[8][j+ti-8])
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
            LMD.set_pixel(9,j-8, matrix[9][j+tj-8])
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
            LMD.set_pixel(10,j-8, matrix[10][j+tk-8])
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
                LMD.set_pixel(i,j-8, matrix[i][j])


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

    roadMap=[8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1,
             1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,
             8,8,9,9,10,10,11,11,12,12,13,13,
             13,13,12,12,11,11,10,10,9,9,8,8]
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
        if tt>225:
            tt=0
        if handle==13 or handle==1:
            for i in range(32):
                for j in range(16):
                    LMD.set_pixel(i,j,0)
            for i in range(32):
                for j in range(16):
                    LMD.set_pixel(i,j,7)
            time.sleep(1)
            for i in range(32):
                for j in range(16):
                    LMD.set_pixel(i,j,0)
            for i in range(0,32,2):
                for j in range(0,16,2):
                    LMD.set_pixel(i,j,7)
            time.sleep(0.5)
            for i in range(32):
                for j in range(16):
                    LMD.set_pixel(i,j,0)
            for i in range(0,32,3):
                for j in range(0,16,3):
                    LMD.set_pixel(i,j,7)
            time.sleep(1)
            
            print("Game Over")
    ##        pygame.quit()
            break
        
        pygame.display.update()
        clock.tick(15)
    endScreen = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    for i in range(32):
            for j in range(16):
                LMD.set_pixel(i,j,endScreen[j][i])
    pygame.quit()

def yut_game_2p():
    def LED_init():
        thread=threading.Thread(target=LMD.main, args=())
        thread.setDaemon(True)
        thread.start()
        return
    board = [\
        ["◎ ","   "," ○","   ","○","   ","○","   ","○ ","   "," ◎"],\
        [" "," ○ "," ","   ","   ","   ","   ","   ","", " ○ "," "],\
        ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
        [" ","   ","  "," ○ ","  ","   ","  "," ○ ","  ","   "," "],\
        ["○","    "," ","    "," ","   ","  ","   ","  ","   ","○"],\
        [" ","   ","  ","   ","  "," ◎ ","  ","   ","  ","   ","  "],\
        ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
        [" ","   ","  "," ○ ","  ","   ","  "," ○ "," ","   ","  "],\
        ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
        [" "," ○ ","  ","   ","  ","   ","  ","   ","  "," ○ "," "],\
        ["◎ ","   "," ○","   ","○","   ","○","   ","○ ","   ","  ◎"]]

    arrayScreen = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    arrayboard = [
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,7,0,7,0,7,0,7,0,7,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,7,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,7,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,7,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,7,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,7,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,7,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,7,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,7,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,7,0,7,0,7,0,7,0,7,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    #y1 도

    y1 = [[0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1]]
    #y2 빽도

    y2 = [[0,0,0,0],
          [1,1,1,1],
          [1,3,3,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1]]

    #y3 개

    y3 = [[0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1]]
    #y4 걸


    y4 = [[0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1]]
    #y5 윷
    y5 =  [[0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1]]

    #y6 모

    y6 =  [[0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1]]

    #A
    ater = [[1]]
    atop = 14
    aleft = 20
    #b턴
    bter = [[4]]
    btop = 14
    btop = 20
    ter = ater

    ah1 = [[1]]
    ah2 = [[1]]
    ah3 = [[1]]
    ah4 = [[1]]

    bh1 = [[4]]
    bh2 = [[4]]
    bh3 = [[4]]
    bh4 = [[4]]

    ah1top = 14
    ah2top = 13
    ah3top = 12
    ah4top = 11

    bh1top = 9
    bh2top = 8
    bh3top = 7
    bh4top = 6

    ah1left = 22
    ah2left = 22
    ah3left = 22
    ah4left = 22

    bh1left = 22
    bh2left = 22
    bh3left = 22
    bh4left = 22

    ah1Blk= Matrix(ah1)
    ah2Blk= Matrix(ah2)
    ah3Blk= Matrix(ah3)
    ah4Blk= Matrix(ah4)

    bh1Blk= Matrix(bh1)
    bh2Blk= Matrix(bh1)
    bh3Blk= Matrix(bh1)
    bh4Blk= Matrix(bh1)
    #endgame A

    endgameA =  [
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,3,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    #endgame B

    endgameB =  [
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,4,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,4,0,4,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,3,0,0,0,0,0,0,0,4,0,4,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    top = 0
    left = 15
    iScreen = Matrix(arrayboard)
    oScreen = Matrix(iScreen)

    ah1Blk= Matrix(ah1)
    ah2Blk= Matrix(ah2)
    ah3Blk= Matrix(ah3)
    ah4Blk= Matrix(ah4)

    bh1Blk= Matrix(bh1)
    bh2Blk= Matrix(bh2)
    bh3Blk= Matrix(bh3)
    bh4Blk= Matrix(bh4)



    yutBlk = Matrix(y1)
    yuttop = 0
    turleft = 15
    #led그리
    def drawmatrix(m):
        array = m.get_array()
        for y in range(32):
            for x in range(16): #m.get_dx()
                
                if array[x][y] == 0:
                    LMD.set_pixel(y, x, 0)
                elif array[x][y] == 1:
                    LMD.set_pixel(y, x, 1)
                elif array[x][y] == 2:
                    LMD.set_pixel(y, x, 2)
                elif array[x][y] == 3:
                    LMD.set_pixel(y, x, 3)
                elif array[x][y] == 4:
                    LMD.set_pixel(y, x, 4)
                elif array[x][y] == 5:
                    LMD.set_pixel(y, x, 5)
                elif array[x][y] == 6:
                    LMD.set_pixel(y, x, 6)
                elif array[x][y] == 7:
                    LMD.set_pixel(y,x, 7)
                elif array[x][y] == 8:
                    LMD.set_pixel(y,x, 1)
                elif array[x][y] == 11:
                    LMD.set_pixel(y,x, 4)
                else:
                    continue
            print()


    members = {}
    members['A'] = ('A',0,0)
    members['B']=('B',0,0)
    def divide(x,y):
        return x/y if y > 0 else 0

    def store_members(members):
        
        names = members.keys()
        for name in names:
            passwd, tries, wins = members[name]



    def where(message):
        answer = input(message)
        while not (answer.isdigit() == False and (answer == 'y' or answer =='n')):#(반복 조건):
            answer = input(message)
        return answer == 'y'

    def up(num,x,y):
        num = num * 2
        if x - num >= 0:
            return (0, x-num, y)
        elif x - num < 0:
            num = num - x
            return num // 2, 0, 10

    def left(num,x,y):
        num = num * 2
        if num-y <= 0:
            if num-y == 0:
                return (0,0,y-num)
            else:
                return (0, 0, y-num)
        elif num-y > 0:
            num = num - y
            return num // 2, 0, 0

    def down(num,x,y):
        num = num * 2
        if x + num <= 11:
            return 0,x+num,0
        elif x + num > 11:
            num = num - (10-x)
            return num // 2, 10, 0

    def right(num,x,y): # 2, 10, 0
        num = num * 2
        if y + num < 10:
            return 0,10,y+num
        elif y + num >= 10:
            print("해당 말이 완주했습니다!")
        return 0, 20, 20

    def set(x,y):
        test1 = "board" + "[" + str(x) + "][" + str(y) + "]"
        small = ['board[0][2]','board[0][4]','board[0][6]','board[0][8]','board[2][0]','board[2][10]','board[4][0]','board[4][10]','board[6][0]','board[6][10]','board[8][0]','board[8][10]','board[10][2]','board[10][4]','board[10][6]','board[10][8]']
        large = ['board[0][0]','board[0][10]','board[10][0]','board[10][10]','board[10][0]','board[10][10]']
        mid1 = ['board[5][5]']
        cross1 = ['board[1][2]','board[9][1]']
        board[10][10] = "◎"
        if test1 in small:
            board[x][y] = "○"
        elif test1 in large:
            board[x][y] = "◎"
        elif test1 in mid1:
            board[x][y] = " ◎ "
        elif test1 in cross1:
            board[x][y] = " ○ "
        else:
            board[x][y] = " ○ "
        # 말 위치값이 10, 10이 아니면 보드판에 모든 말의 위치값을 표시

    def cross(num,x,y):
        set(x,y)
        num = num * 2
        if (x == 0 and y == 10) or (x == 0 and y == 0):
            if x == 0 and y == 10:
                num -= 2
                return cross(num//2, 1, 9)
            else:
                num -= 2
                return cross(num//2, 1, 1)
        elif (1<=x<=4 and 6<=y<=9) or (6<=x<=9 and 1<=y<=4):
             if y - num > 0:
                 return 0, x+num, y-num
             elif y - num < 0:
                 return right((num - y)//2, 10, 0)
             elif y - num == 0:
                 return 0, 10, 0
        elif (1<=x<=4 and 1<=y<=4) or (6<=x<=9 and 6<=y<=9):
             if y + num < 10:
                return 0, x+num, y+num
             elif y + num > 10:
                 print("해당 말이 완주했습니다!")
                 return 0, 20, 20
        elif x == y:
             if where("꺾기? (y/n)"):
                 if y + num < 10:
                     return 0, x + num, y + num
                 elif y + num > 10:
                     print("해당 말이 완주했습니다!")
                     return 0, 20, 20
             else:
                 if y - num > 0:
                     return 0, x - num, y - num
                 elif y - num < 0:
                     return right((num - y) // 2, 10, 0)
                 elif y - num == 0:
                     return 0, 10, 0

    def move(num,x,y,move_num):
        down1 = ['board[0][0]','board[2][0]','board[4][0]','board[6][0]','board[8][0]']
        left1 = ['board[0][2]','board[0][4]','board[0][6]','board[0][8]','board[0][10]']
        right1 = ['board[10][0]','board[10][2]','board[10][4]','board[10][6]','board[10][8]']
        up1 = ['board[2][10]','board[4][10]','board[6][10]','board[8][10]','board[10][10]']
        cross1 = ['board[1][1]','board[2][2]','board[3][3]','board[4][4]','board[5][5]',
                  'board[6][6]','board[7][7]','board[8][8]','board[9][9]','board[1][9]',
                  'board[3][7]','board[7][3]','board[9][1]']
        test = "board" + "[" + str(x) + "][" + str(y) + "]"
        if x == 0 and y == 10 and move_num == 0 and num > 0:
            if where("꺾기? (y/n)"):
                move_num  += 1
                return cross(num, x, y)
            else:
                move_num += 1
                return left(num, x, y)
        elif x == 0 and y == 0 and move_num == 0 and num > 0:
            if where("꺾기? (y/n)"):
                return cross(num, x, y)
            else:
                return right(num, x, y)
        elif num > 0:
            if test in right1:
                num,x,y = right(num,x,y)
                return num,x,y
            elif test in down1:
                num,x,y = down(num,x,y)
                return num,x,y
            elif test in left1:
                num,x,y = left(num,x,y)
                return num, x, y
            elif test in up1:
                num,x,y = up(num,x,y)
                return num,x,y
            elif test in cross1:
                num,x,y = cross(num,x,y)
                return num,x,y
        elif num < 0:
            if test in down1:
                if x == 0:
                    return 0, 0, 2
                else:
                    return 0, x-2, 0
            elif test in right1:
                if y == 0:
                    if where("꺾기? (y/n)")==True:
                        return 0, 9, 1
                    else:
                        return 0, 8, 0
                else:
                    return 0, 10, y-2
            elif test in up1:
                if x == 8:
                    print("해당 말이 완주했습니다!")
                    return 0, 20, 20
                else:
                    return 0, x+2, 10
            elif test in left1:
                if y == 10:
                    return 0, 2, 10
                else:
                    return 0, 0, y+2

            elif test in cross1:
                if y == 5:
                    if where("왼쪽으로 꺾기? (y/n)"):
                        return 0, 3, 7
                    else:
                        return 0, 3, 3
                elif (1<=x<=4 and 6<=y<=9) or (6<=x<=9 and 1<=y<=4):
                    if x==1 and y==9:
                        return 0, 0, 10
                    return 0, x-2, y+2
                elif (1<=x<=4 and 1<=y<=4) or (6<=x<=9 and 6<=y<=9):
                    if x == 1 and y == 1:
                       return 0, 0, 0
                    return 0, x-2, y-2
        return num,x,y

    def fin(num,x,y):
        move_num = 0
        while num != 0:
            set(x,y)
            num,x,y = move(num,x,y,move_num)
            move_num += 1
        return x, y

    def mal_num_A(A1,mum,x,y):
        if mum == 0:
            return A1
        else:
            A1[mum - 1][0] = x
            A1[mum - 1][1] = y
            return A1

    def mal_num_B(B1,mum,x,y):
        if mum == 0:
            return B1
        else:
            B1[mum - 1][0] = x
            B1[mum - 1][1] = y
            return B1

    def throw():
        import random
        jipab = [{'도': 1}, {'도': 1}, {'도': 1},{'도': 1},\
             {'개': 2}, {'개': 2},{'개': 2},{'개': 2},{'개': 2},{'개': 2},\
             {'걸' : 3},{'걸' : 3},{'걸' : 3},{'걸' : 3}, \
             {'윷': 4},\
             {'모': 5}, {'빽도': -1}]
        n, k = [], []
        random.shuffle(jipab)
        j = jipab[random.randint(0, 15)]

        while j == {'윷' : 4} or j == {'모': 5}:
            
            print(list(j.keys())[0] + "!")
            if (list(j.keys())[0] == '도'):
                yutBlk = Matrix(y1)
                yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
                yuttBlk = yuttBlk+yutBlk
                oScreen.paste(yuttBlk, yuttop, turleft)
                drawmatrix(oScreen); print()
            elif (list(j.keys())[0] == '개'):
                yutBlk = Matrix(y3)
                yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
                yuttBlk = yuttBlk+yutBlk
                oScreen.paste(yuttBlk, yuttop, turleft)
                drawmatrix(oScreen); print()
            elif (list(j.keys())[0] == '걸'):
                yutBlk = Matrix(y4)
                yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
                yuttBlk = yuttBlk+yutBlk
                oScreen.paste(yuttBlk, yuttop, turleft)
                drawmatrix(oScreen); print()
            elif (list(j.keys())[0] == '윷'):
                yutBlk = Matrix(y5)
                yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
                yuttBlk = yuttBlk+yutBlk
                oScreen.paste(yuttBlk, yuttop, turleft)
                drawmatrix(oScreen); print()
            elif (list(j.keys())[0] == '모'):
                yutBlk = Matrix(y6)
                yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
                yuttBlk = yuttBlk+yutBlk
                oScreen.paste(yuttBlk, yuttop, turleft)
                drawmatrix(oScreen); print()
            elif (j == {'빽도': -1}):
                yutBlk = Matrix(y2)
                yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
                yuttBlk = yuttBlk+yutBlk
                oScreen.paste(yuttBlk, yuttop, turleft)
                drawmatrix(oScreen); print()
            input("한번 더!(엔터를 눌러주세요.)")
            n += list(j.keys())
            k.append(j)
            j = jipab[random.randint(0, 15)]
        print(list(j.keys())[0] + "!")
        if (list(j.keys())[0] == '도'):
            yutBlk = Matrix(y1)
            yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
            yuttBlk = yuttBlk+yutBlk
            oScreen.paste(yuttBlk, yuttop, turleft)
            drawmatrix(oScreen); print()
        elif (list(j.keys())[0] == '개'):
            yutBlk = Matrix(y3)
            yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
            yuttBlk = yuttBlk+yutBlk
            oScreen.paste(yuttBlk, yuttop, turleft)
            drawmatrix(oScreen); print()
        elif (list(j.keys())[0] == '걸'):
            yutBlk = Matrix(y4)
            yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
            yuttBlk = yuttBlk+yutBlk
            oScreen.paste(yuttBlk, yuttop, turleft)
            drawmatrix(oScreen); print()
        elif (list(j.keys())[0] == '윷'):
            yutBlk = Matrix(y5)
            yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
            yuttBlk = yuttBlk+yutBlk
            oScreen.paste(yuttBlk, yuttop, turleft)
            drawmatrix(oScreen); print()
        elif (list(j.keys())[0] == '모'):
           
            yutBlk = Matrix(y6)
            yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
            yuttBlk = yuttBlk+yutBlk
            oScreen.paste(yuttBlk, yuttop, turleft)
            drawmatrix(oScreen); print()
        elif (j == {'빽도': -1}):
            yutBlk = Matrix(y2)
            yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
            yuttBlk = yuttBlk+yutBlk
            oScreen.paste(yuttBlk, yuttop, turleft)
            drawmatrix(oScreen); print()
        k.append(j)
        n += list(j.keys())
        return n, k

    def where1(message):
        answer = input(message)
        while not (answer.isdigit() == True and (answer == '1' or answer =='2' or answer =='3' or answer =='4')):#(반복 조건):
            answer = input(message)
        return int(answer)#그냥 answer로 리턴하던 것에 int를 씌웠다.

    def origin_board():#깨끗한 놀이판, show_board에서만 사용한다.
        return [\
        ["◎ ","   ","○ ","   ","○","   ","○","   "," ○","   "," ◎"],\
        [" "," ○ "," ","   ","   ","   ","   ","   ","", " ○ "," "],\
        ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
        [" ","   ","  "," ○ ","  ","   ","  "," ○ ","  ","   "," "],\
        ["○","    "," ","    "," ","   ","  ","   ","  ","   ","○"],\
        [" ","   ","  ","   ","  "," ◎ ","  ","   ","  ","   ","  "],\
        ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
        [" ","   ","  "," ○ ","  ","   ","  "," ○ "," ","   ","  "],\
        ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
        [" "," ○ ","  ","   ","  ","   ","  ","   ","  "," ○ "," "],\
        ["◎ ","   ","○ ","   ","○","   ","○","   "," ○","   ","  ◎"]]
        
    def Acheck(top, left, acheck):
        if (acheck ==1):
            ah1top = top
            ah1left = left
            ah11Blk = iScreen.clip(ah1top, ah1left, ah1top+ah1Blk.get_dy(), ah1left+ah1Blk.get_dx())
            ah11Blk = ah11Blk+ah1Blk
            oScreen.paste(ah11Blk, ah1top, ah1left)
        elif (acheck ==2):
            ah2top = top
            ah2left = left
            
            ah22Blk = iScreen.clip(ah2top, ah2left, ah2top+ah2Blk.get_dy(), ah2left+ah2Blk.get_dx())
            ah22Blk = ah22Blk+ah2Blk
            oScreen.paste(ah22Blk, ah2top, ah2left)
        elif (acheck ==3):
            ah3top = top
            ah3left = left
            
            ah33Blk = iScreen.clip(ah3top, ah3left, ah3top+ah3Blk.get_dy(), ah3left+ah3Blk.get_dx())
            ah33Blk = ah33Blk+ah3Blk
            oScreen.paste(ah33Blk, ah3top, ah3left)
        elif (acheck ==4):
            ah4top = top
            ah4left = left
            
            ah44Blk = iScreen.clip(ah4top, ah4left, ah4top+ah4Blk.get_dy(), ah4left+ah4Blk.get_dx())
            ah44Blk = ah44Blk+ah4Blk
            oScreen.paste(ah44Blk, ah4top, ah4left)
            
            
    def Bcheck(top, left, bcheck):
        if (bcheck ==1):
            bh1top = top
            bh1left = left
        
            bh11Blk = iScreen.clip(bh1top, bh1left, bh1top+bh1Blk.get_dy(), bh1left+bh1Blk.get_dx())
            bh11Blk = bh11Blk+bh1Blk
            oScreen.paste(bh11Blk, bh1top, bh1left)
        elif (bcheck ==2):
            bh2top = top
            bh2left = left
            
            bh22Blk = iScreen.clip(bh2top, bh2left, bh2top+bh2Blk.get_dy(), bh2left+bh2Blk.get_dx())
            bh22Blk = bh22Blk+bh2Blk
            oScreen.paste(bh22Blk, bh2top, bh2left)
        elif (bcheck ==3):
            bh3top = top
            bh3left = left
            
            bh33Blk = iScreen.clip(bh3top, bh3left, bh3top+bh3Blk.get_dy(), bh3left+bh3Blk.get_dx())
            bh33Blk = bh33Blk+bh3Blk
            oScreen.paste(bh33Blk, bh3top, bh3left)
        elif (bcheck ==4):
            bh4top = top
            bh4left = left
            
            bh44Blk = iScreen.clip(bh4top, bh4left, bh4top+bh4Blk.get_dy(), bh4left+bh4Blk.get_dx())
            bh44Blk = bh44Blk+bh4Blk
            oScreen.paste(bh44Blk, bh4top, bh4left)

    def show_board(A1, B1, X, Y):
        board = origin_board()#깨끗한 놀이판
        iScreen = Matrix(arrayScreen)
        oScreen = Matrix(iScreen)
        mum = 0
        acheck = 0
        bcheck = 0
        for i in A1:#A팀의 말 입력
            acheck += 1
            if i != [10,10] and i != [20,20]:
                if (i == [0,0]):
                    top =13
                    left = 1
                    Acheck(top, left, acheck)
                    
                elif (i == [0,2]):
                    
                    top = 11
                    left = 1
                    Acheck(top, left, acheck)
                    
                elif (i == [0,4]):
                    top = 9
                    left = 1
                    Acheck(top, left, acheck)
                    
                elif (i == [0,6]):
                    
                    top = 7
                    left = 1
                    Acheck(top, left, acheck)
                    
                elif (i == [0,8]):
                    top = 5
                    left = 1
                    Acheck(top, left, acheck)
                    
                elif (i == [0,10]):
                    
                    top = 3
                    left = 1
                    Acheck(top, left, acheck)
                    
                elif (i == [1,1]):
                    
                    top = 12
                    left = 2
                    Acheck(top, left, acheck)
                    
                elif (i == [1,9]):
                    
                    top = 4
                    left = 2
                    Acheck(top, left, acheck)
                    
                elif (i == [2,0]):
                    
                    top = 13
                    left = 3
                    Acheck(top, left, acheck)
                    
                elif (i == [2,10]):
                    
                    top = 3
                    left = 3
                    Acheck(top, left, acheck)
                    
                elif (i == [3,3]):
                    
                    top = 10
                    left = 4
                    Acheck(top, left, acheck)
                    
                elif (i == [3,7]):
                    
                    top = 6
                    left = 4
                    Acheck(top, left, acheck)
                    
                elif (i == [4,0]):
                    
                    top = 13
                    left = 5
                    Acheck(top, left, acheck)
                    
                elif (i == [4,10]):
                    
                    top = 3
                    left = 5
                    Acheck(top, left, acheck)
                    
                elif (i == [5,5]):
                    
                    top = 8
                    left = 6
                    Acheck(top, left, acheck)
                    
                elif (i == [6,0]):
                   
                    top = 13
                    left = 7
                    Acheck(top, left, acheck)
                    
                elif (i == [6,10]):
                    
                    top = 3
                    left = 7
                    Acheck(top, left, acheck)
                    
                elif (i == [7,3]):
                    
                    top = 10
                    left = 8
                    Acheck(top, left, acheck)
                    
                elif (i == [7,7]):
                    
                    top = 6
                    left = 8
                    Acheck(top, left, acheck)
                    
                elif (i == [8,0]):
                    
                    ah1top =13
                    ah1left = 9
                    Acheck(top, left, acheck)
                    
                elif (i == [8,10]):
                    
                    top = 3
                    left = 9
                    Acheck(top, left, acheck)
                    
                elif (i == [9,1]):
                    
                    top = 12
                    left = 10
                    Acheck(top, left, acheck)
                    
                elif (i == [9,9]):
                    
                    top = 4
                    left = 10
                    Acheck(top, left, acheck)
                    
                elif (i == [10,0]):
                    
                    top = 13
                    left = 11
                    Acheck(top, left, acheck)
                    
                elif (i == [10,2]):
                    
                    top = 11
                    left = 11
                    Acheck(top, left, acheck)
                    
                elif (i == [10,4]):
                    
                    top = 9
                    left = 11
                    Acheck(top, left, acheck)
                    
                elif (i == [10,6]):
                    
                    top = 7
                    left = 11
                    Acheck(top, left, acheck)
                    
                elif (i == [10,8]):
                    
                    top = 5
                    left = 11
                    Acheck(top, left, acheck)
                    
                elif (i == [10,10]):
                    top = 3
                    left = 11
                    Acheck(top, left, acheck)
                
                board[i[0]][i[1]] = X[mum]
            mum += 1
        mum = 0
        for i in B1:#B팀의 말 입력
            bcheck += 1
            if i != [10,10] and i != [20,20]:
                if (i == [0,0]):
                    
                    top = 13
                    left = 1
                    Bcheck(top, left, bcheck)
                    
                elif (i == [0,2]):
                    
                    top = 11
                    left = 1
                    Bcheck(top, left, bcheck)
                elif (i == [0,4]):
                    top = 9
                    left = 1
                    Bcheck(top, left, bcheck)
                elif (i == [0,6]):
                    
                    top = 7
                    left = 1
                    Bcheck(top, left, bcheck)
                elif (i == [0,8]):
                    top = 5
                    left = 1
                    Bcheck(top, left, bcheck)
                elif (i == [0,10]):
                    
                    top = 3
                    left = 1
                    Bcheck(top, left, bcheck)
                elif (i == [1,1]):
                    
                    top = 12
                    left = 2
                    Bcheck(top, left, bcheck)
                elif (i == [1,9]):
                    
                    top = 4
                    left = 2
                    Bcheck(top, left, bcheck)
                elif (i == [2,0]):
                    
                    top = 13
                    left = 3
                    Bcheck(top, left, bcheck)
                elif (i == [2,10]):
                    
                    top = 3
                    left = 3
                    Bcheck(top, left, bcheck)
                elif (i == [3,3]):
                    
                    top = 10
                    left = 4
                    Bcheck(top, left, bcheck)
                elif (i == [3,7]):
                    
                    top = 6
                    left = 4
                    Bcheck(top, left, bcheck)
                elif (i == [4,0]):
                    
                    top = 13
                    left = 5
                    Bcheck(top, left, bcheck)
                elif (i == [4,10]):
                    
                    top = 3
                    left = 5
                    Bcheck(top, left, bcheck)
                elif (i == [5,5]):
                    
                    top = 8
                    left = 6
                    Bcheck(top, left, bcheck)
                elif (i == [6,0]):
                    
                    top = 13
                    left = 7
                    Bcheck(top, left, bcheck)
                elif (i == [6,10]):
                    
                    top = 3
                    left = 7
                    Bcheck(top, left, bcheck)
                elif (i == [7,3]):
                    
                    top = 10
                    left = 8
                    Bcheck(top, left, bcheck)
                elif (i == [7,7]):
                    
                    top = 6
                    left = 8
                    Bcheck(top, left, bcheck)
                elif (i == [8,0]):
                    
                    top = 13
                    left = 9
                    Bcheck(top, left, bcheck)
                elif (i == [8,10]):
                    
                    top = 3
                    left = 9
                    Bcheck(top, left, bcheck)
                elif (i == [9,1]):
                    
                    top = 12
                    left = 10
                    Bcheck(top, left, bcheck)
                elif (i == [9,9]):
                    
                    top = 4
                    left = 10
                    Bcheck(top, left, bcheck)
                elif (i == [10,0]):
                    
                    top = 13
                    left = 11
                    Bcheck(top, left, bcheck)
                elif (i == [10,2]):
                    
                    top = 11
                    left = 11
                    Bcheck(top, left, bcheck)
                elif (i == [10,4]):
                    
                    top = 9
                    left = 11
                    Bcheck(top, left, bcheck)
                elif (i == [10,6]):
                    
                    top = 7
                    left = 11
                    Bcheck(top, left, bcheck)
                elif (i == [10,8]):
                   
                    top = 5
                    left = 11
                    Bcheck(top, left, bcheck)
                elif (i == [10,10]):
                    
                    top = 3
                    left = 11
                    Bcheck(top, left, bcheck)
                board[i[0]][i[1]] = Y[mum]
            mum += 1
        drawmatrix(oScreen); print()
        for row in board:
            for x in range(11):
                print(row[x], end='')
            print()

    def same_pos_A(mum,A1,B1):
        for i in range(2):
            if (mum-1 != i) and (A1[mum-1] == A1[i]) and (A1[mum-1] != [10,10]) and (A1[mum-1] != [20,20]):
               return 1 #아군의 말과 같은 위치일 때
            elif (A1[mum-1] == B1[i]) and (B1[i] != [10,10]) and (B1[i] != [20,20]):
                 B1[i] = [10,10]
                 return 0
        return 2

    def same_pos_B(mum,A1,B1):
        for i in range(2):
            if (mum-1 != i) and (B1[mum-1] == B1[i]) and (B1[mum-1] != [10,10]) and (B1[mum-1] != [20,20]):
               return 1
            elif B1[mum-1] == A1[i] and (A1[i] != [10,10]) and (A1[i] != [20,20]):
                 A1[i] = [10,10]
                 return 0
        return 2

    def mal_E_up_seong(X):
        count = 0
        for a in X:
            if a in [[10,10],[20,20]]:
               count += 1
        if count == 4:
           return True
        else:
            return False
    LED_init()
    def main_game():
        print("Contradiction 윷놀이에 오신 것을 환영합니다!")
        usernameA, passwdA, triesA, winsA = 'A', 'A', 0,0
        usernameB, passwdB, triesB, winsB = 'B','B',0,0
        Games = 1
        X = ["❶", "❷"]
        Y = ["➀", "➁"]
        A1 = [[10, 10], [10, 10]]
        B1 = [[10, 10], [10, 10]]
        n, k = [],[]
        check = True
        while check:
         
              ter = ater
              aBlk = Matrix(ter)
              aattBlk = iScreen.clip(atop, aleft, atop+aBlk.get_dy(), aleft+aBlk.get_dx())
              aattBlk = aattBlk+aBlk
              oScreen.paste(aattBlk, atop, aleft)
              drawmatrix(oScreen); print()
              
              input("A팀의 턴입니다!\n엔터키를 눌러 윷을 던져주세요.")
              n1, k1 = throw()
              n += n1
              k += k1
              while n != []:
                    if n == ['빽도'] and mal_E_up_seong(A1):
                       print("이런! 움직일 수 있는 말이 없네요. 턴이 넘어갑니다.")
                       n,k = [],[]#빽도 치워주기
                       break
                    if len(n)>1:#윷을 여러번 던졌을 때
                       print(n)
                       z = input("어느 것으로 먼저 움직이시겠습니까? A는 도 B는 개 C는 걸 D는 윷 E는 모 F는 빽도")
                       while not ((z == "A") or (z == "B") or (z == "C") or (z == "D") or (z == "E") or (z == "F")):
                             if z not in n:#한글이 맞지만 뽑은 것이 아닐 경우
                                z = input("제대로 선택해 주십시오.")
                             else:#뭣도 아닐 경우
                                 z = input("제대로 선택해 주십시오")
                       if (z == "A"):
                           z = "도"
                       elif (z == "B"):
                           z = "개"
                       elif (z == "C"):
                           z = "걸"
                       elif (z == "D"):
                           z = "윷"
                       elif (z == "E"):
                           z = "모"
                       elif (z == "F"):
                           z = "빽도"
                    else:#한번만 뽑았을 때
                        z = n[0]
                    mum = where1("몇번 말을 움직이시겠습니까?")
                    while z == '빽도' and A1[mum-1] == [10,10]:
                          mum = where1("해당 말은 빽도로 움직일 수 없는 위치에 있습니다.\n다른 말을 선택해 주세요.")
                    while A1[mum-1] == [20,20]:#이미 완주한 말을 움직이려 할 때
                          mum = int(input("해당 말은 이미 완주했습니다.\n다른 말을 선택해 주세요."))
                    x1, y1 = A1[mum - 1][0], A1[mum - 1][1]#움직이려는 말의 위치정보
                    x, y = fin(k[n.index(z)][z],x1,y1)#움직였을 때의 위치정보
                    A1 = mal_num_A(A1, mum, x, y)
                    p = same_pos_A(mum,A1,B1)#p는 0에서2중에 하나의 정수
                    while p == 1 or p == 0:
                          if p == 1:
                             x, y = fin(1,A1[mum-1][0],A1[mum-1][1])
                             A1 = mal_num_A(A1, mum, x, y)
                             print('점프!')
                             p = same_pos_A(mum,A1,B1)
                          elif p == 0:
                               show_board(A1, B1, X, Y)
                               print("상대의 말을 잡았습니다!")
                               input("한번 더 윷을 던질 수 있습니다. 엔터를 눌러주세요.")
                               n1, k1 = throw()#추가던지기
                               n += n1
                               k += k1
                               p = same_pos_A(mum,A1,B1)
                    show_board(A1, B1, X, Y)
                    k.remove(k[n.index(z)])
                    n.remove(z)
                    if A1 == [[20,20],[20,20]]:#승리조건
                        WA, WB = 1, 0
                        members[usernameA] = (passwdA, triesA + Games, winsA + WA)
                        members[usernameB] = (passwdB, triesB + Games, winsB + WB)
                        endScreen = Matrix(endgameA)
                        draw_matrix(endScreen); print()
                        time.sleep(1)
                        check = False
                        return print("A팀의 승리입니다!")
               #파란색이 경우 B팀 턴
              ter = bter
              aBlk = Matrix(ter)
              aattBlk = iScreen.clip(atop, aleft, atop+aBlk.get_dy(), aleft+aBlk.get_dx())
              aattBlk = aattBlk+aBlk
              oScreen.paste(aattBlk, atop, aleft)
              drawmatrix(oScreen); print()
              
              input("B팀의 턴입니다!\n엔터키를 눌러 윷을 던져주세요.")
              n1, k1 = throw()
              n += n1
              k += k1
              while n != []:
                    if n == ['빽도'] and mal_E_up_seong(B1):
                       print("이런! 움직일 수 있는 말이 없네요. 턴이 넘어갑니다.")
                       n, k = [], []
                       break
                    if len(n)>1:
                       print(n)
                       z = input("어느 것으로 먼저 움직이시겠습니까? A는 도 B는 개 C는 걸 D는 윷 E는 모 F는 빽도")
                       while not ((z == "A") or (z == "B") or (z == "C") or (z == "D") or (z == "E") or (z == "F")):
                             if z not in n:
                                z = input("제대로 선택해 주십시오.")
                             else:
                                 z = input("제대로 선택해 주십시오")
                       if (z == "A"):
                           z = "도"
                       elif (z == "B"):
                           z = "개"
                       elif (z == "C"):
                           z = "걸"
                       elif (z == "D"):
                           z = "윷"
                       elif (z == "E"):
                           z = "모"
                       elif (z == "F"):
                           z = "빽도"
                    else:
                        z = n[0]
                    mum = where1("몇번 말을 움직이시겠습니까?")
                    while (z == '빽도' and B1[mum-1] == [10,10]):
                          mum = where1("해당 말은 빽도로 움직일 수 없는 위치에 있습니다.\n다른 말을 선택해 주세요.")
                    while B1[mum - 1] == [20, 20]:
                        mum = int(input("해당 말은 이미 완주했습니다.\n다른 말을 선택해 주세요."))
                    x1, y1 = B1[mum - 1][0], B1[mum - 1][1]
                    x, y = fin(k[n.index(z)][z], x1, y1)
                    B1 = mal_num_B(B1, mum, x, y)
                    p = same_pos_B(mum, A1, B1)
                    while p == 1 or p == 0:
                          if p == 1:
                             x, y = fin(1, B1[mum-1][0], B1[mum-1][1])
                             B1 = mal_num_B(B1, mum, x, y)
                             print('점프!')
                             p = same_pos_B(mum, A1, B1)
                          elif p == 0:
                               show_board(A1, B1, X, Y)
                               print("상대의 말을 잡았습니다!")
                               input("한번 더 윷을 던질 수 있습니다. 엔터를 눌러주세요.")
                               n1, k1 = throw()
                               n += n1
                               k += k1
                               p = same_pos_B(mum, A1, B1)
                    show_board(A1, B1, X, Y)
                    k.remove(k[n.index(z)])
                    n.remove(z)
                    if B1 == [[20,20],[20,20]]:
                        WA, WB = 0, 1
                        members[usernameA] = (passwdA, triesA + Games, winsA + WA)
                        members[usernameB] = (passwdB, triesB + Games, winsB + WB)
                        endScreen = Matrix(endgameB)
                        draw_matrix(endScreen); print()
                        time.sleep(1)
                        check = False
                        
                        return print("B팀의 승리입니다!")

    main_game()
def yut_game():
    def LED_init():
        thread=threading.Thread(target=LMD.main, args=())
        thread.setDaemon(True)
        thread.start()
        return
    board = [\
        ["◎ ","   "," ○","   ","○","   ","○","   ","○ ","   "," ◎"],\
        [" "," ○ "," ","   ","   ","   ","   ","   ","", " ○ "," "],\
        ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
        [" ","   ","  "," ○ ","  ","   ","  "," ○ ","  ","   "," "],\
        ["○","    "," ","    "," ","   ","  ","   ","  ","   ","○"],\
        [" ","   ","  ","   ","  "," ◎ ","  ","   ","  ","   ","  "],\
        ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
        [" ","   ","  "," ○ ","  ","   ","  "," ○ "," ","   ","  "],\
        ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
        [" "," ○ ","  ","   ","  ","   ","  ","   ","  "," ○ "," "],\
        ["◎ ","   "," ○","   ","○","   ","○","   ","○ ","   ","  ◎"]]

    #led기본화면설정

    arrayScreen = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    arrayboard = [
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,7,0,7,0,7,0,7,0,7,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,7,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,7,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,7,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,7,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,7,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,7,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,7,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,7,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,7,0,7,0,7,0,7,0,7,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    #y1 도

    y1 = [[0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1]]
    #y2 빽도

    y2 = [[0,0,0,0],
          [1,1,1,1],
          [1,3,3,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1]]

    #y3 개

    y3 = [[0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1]]
    #y4 걸


    y4 = [[0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1]]
    #y5 윷
    y5 =  [[0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1]]

    #y6 모

    y6 =  [[0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [1,2,2,1],
          [1,1,1,1]]

    #A
    ater = [[1]]
    atop = 14
    aleft = 20
    #b턴
    bter = [[4]]
    btop = 14
    btop = 20
    ter = ater

    ah1 = [[1]]
    ah2 = [[1]]
    ah3 = [[1]]
    ah4 = [[1]]

    bh1 = [[4]]
    bh2 = [[4]]
    bh3 = [[4]]
    bh4 = [[4]]

    ah1top = 14
    ah2top = 13
    ah3top = 12
    ah4top = 11

    bh1top = 9
    bh2top = 8
    bh3top = 7
    bh4top = 6

    ah1left = 22
    ah2left = 22
    ah3left = 22
    ah4left = 22

    bh1left = 22
    bh2left = 22
    bh3left = 22
    bh4left = 22

    ah1Blk= Matrix(ah1)
    ah2Blk= Matrix(ah2)
    ah3Blk= Matrix(ah3)
    ah4Blk= Matrix(ah4)

    bh1Blk= Matrix(bh1)
    bh2Blk= Matrix(bh1)
    bh3Blk= Matrix(bh1)
    bh4Blk= Matrix(bh1)


    #endgame A

    endgameA =  [
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,3,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    #endgame B

    endgameB =  [
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,4,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,4,0,4,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,3,0,0,0,0,0,0,0,4,0,4,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    top = 0
    left = 15
    iScreen = Matrix(arrayboard)
    oScreen = Matrix(iScreen)

    ah1Blk= Matrix(ah1)
    ah2Blk= Matrix(ah2)
    ah3Blk= Matrix(ah3)
    ah4Blk= Matrix(ah4)

    bh1Blk= Matrix(bh1)
    bh2Blk= Matrix(bh2)
    bh3Blk= Matrix(bh3)
    bh4Blk= Matrix(bh4)
    yutBlk = Matrix(y1)
    yuttop = 0
    turleft = 15
    #led그리
    def drawmatrix(m):
        array = m.get_array()
        for y in range(32):
            for x in range(16): #m.get_dx()
                
                if array[x][y] == 0:
                    LMD.set_pixel(y, x, 0)
                elif array[x][y] == 1:
                    LMD.set_pixel(y, x, 1)
                elif array[x][y] == 2:
                    LMD.set_pixel(y, x, 2)
                elif array[x][y] == 3:
                    LMD.set_pixel(y, x, 3)
                elif array[x][y] == 4:
                    LMD.set_pixel(y, x, 4)
                elif array[x][y] == 5:
                    LMD.set_pixel(y, x, 5)
                elif array[x][y] == 6:
                    LMD.set_pixel(y, x, 6)
                elif array[x][y] == 7:
                    LMD.set_pixel(y,x, 7)
                elif array[x][y] == 8:
                    LMD.set_pixel(y,x, 1)
                elif array[x][y] == 11:
                    LMD.set_pixel(y,x, 4)
                else:
                    continue
            print()
    members = {}
    members['A'] = ('A',0,0)
    members['B']=('B',0,0)
    def divide(x,y):
        return x/y if y > 0 else 0

    def store_members(members):
        
        names = members.keys()
        for name in names:
            passwd, tries, wins = members[name]



    def where(message):
        answer = input(message)
        while not (answer.isdigit() == False and (answer == 'y' or answer =='n')):#(반복 조건):
            answer = input(message)
        return answer == 'y'

    def up(num,x,y):
        num = num * 2
        if x - num >= 0:
            return (0, x-num, y)
        elif x - num < 0:
            num = num - x
            return num // 2, 0, 10

    def left(num,x,y):
        num = num * 2
        if num-y <= 0:
            if num-y == 0:
                return (0,0,y-num)
            else:
                return (0, 0, y-num)
        elif num-y > 0:
            num = num - y
            return num // 2, 0, 0

    def down(num,x,y):
        num = num * 2
        if x + num <= 11:
            return 0,x+num,0
        elif x + num > 11:
            num = num - (10-x)
            return num // 2, 10, 0

    def right(num,x,y): # 2, 10, 0
        num = num * 2
        if y + num < 10:
            return 0,10,y+num
        elif y + num >= 10:
            print("해당 말이 완주했습니다!")
        return 0, 20, 20

    def set(x,y):
        test1 = "board" + "[" + str(x) + "][" + str(y) + "]"
        small = ['board[0][2]','board[0][4]','board[0][6]','board[0][8]','board[2][0]','board[2][10]','board[4][0]','board[4][10]','board[6][0]','board[6][10]','board[8][0]','board[8][10]','board[10][2]','board[10][4]','board[10][6]','board[10][8]']
        large = ['board[0][0]','board[0][10]','board[10][0]','board[10][10]','board[10][0]','board[10][10]']
        mid1 = ['board[5][5]']
        cross1 = ['board[1][2]','board[9][1]']
        board[10][10] = "◎"
        if test1 in small:
            board[x][y] = "○"
        elif test1 in large:
            board[x][y] = "◎"
        elif test1 in mid1:
            board[x][y] = " ◎ "
        elif test1 in cross1:
            board[x][y] = " ○ "
        else:
            board[x][y] = " ○ "
        # 말 위치값이 10, 10이 아니면 보드판에 모든 말의 위치값을 표시

    def cross(num,x,y):
        set(x,y)
        num = num * 2
        if (x == 0 and y == 10) or (x == 0 and y == 0):
            if x == 0 and y == 10:
                num -= 2
                return cross(num//2, 1, 9)
            else:
                num -= 2
                return cross(num//2, 1, 1)
        elif (1<=x<=4 and 6<=y<=9) or (6<=x<=9 and 1<=y<=4):
             if y - num > 0:
                 return 0, x+num, y-num
             elif y - num < 0:
                 return right((num - y)//2, 10, 0)
             elif y - num == 0:
                 return 0, 10, 0
        elif (1<=x<=4 and 1<=y<=4) or (6<=x<=9 and 6<=y<=9):
             if y + num < 10:
                return 0, x+num, y+num
             elif y + num > 10:
                 print("해당 말이 완주했습니다!")
                 return 0, 20, 20
        elif x == y:
             if where("꺾기? (y/n)"):
                 if y + num < 10:
                     return 0, x + num, y + num
                 elif y + num > 10:
                     print("해당 말이 완주했습니다!")
                     return 0, 20, 20
             else:
                 if y - num > 0:
                     return 0, x - num, y - num
                 elif y - num < 0:
                     return right((num - y) // 2, 10, 0)
                 elif y - num == 0:
                     return 0, 10, 0

    def move(num,x,y,move_num):
        down1 = ['board[0][0]','board[2][0]','board[4][0]','board[6][0]','board[8][0]']
        left1 = ['board[0][2]','board[0][4]','board[0][6]','board[0][8]','board[0][10]']
        right1 = ['board[10][0]','board[10][2]','board[10][4]','board[10][6]','board[10][8]']
        up1 = ['board[2][10]','board[4][10]','board[6][10]','board[8][10]','board[10][10]']
        cross1 = ['board[1][1]','board[2][2]','board[3][3]','board[4][4]','board[5][5]',
                  'board[6][6]','board[7][7]','board[8][8]','board[9][9]','board[1][9]',
                  'board[3][7]','board[7][3]','board[9][1]']
        test = "board" + "[" + str(x) + "][" + str(y) + "]"
        if x == 0 and y == 10 and move_num == 0 and num > 0:
            if where("꺾기? (y/n)"):
                move_num  += 1
                return cross(num, x, y)
            else:
                move_num += 1
                return left(num, x, y)
        elif x == 0 and y == 0 and move_num == 0 and num > 0:
            if where("꺾기? (y/n)"):
                return cross(num, x, y)
            else:
                return right(num, x, y)
        elif num > 0:
            if test in right1:
                num,x,y = right(num,x,y)
                return num,x,y
            elif test in down1:
                num,x,y = down(num,x,y)
                return num,x,y
            elif test in left1:
                num,x,y = left(num,x,y)
                return num, x, y
            elif test in up1:
                num,x,y = up(num,x,y)
                return num,x,y
            elif test in cross1:
                num,x,y = cross(num,x,y)
                return num,x,y
        elif num < 0:
            if test in down1:
                if x == 0:
                    return 0, 0, 2
                else:
                    return 0, x-2, 0
            elif test in right1:
                if y == 0:
                    if where("꺾기? (y/n)")==True:
                        return 0, 9, 1
                    else:
                        return 0, 8, 0
                else:
                    return 0, 10, y-2
            elif test in up1:
                if x == 8:
                    print("해당 말이 완주했습니다!")
                    return 0, 20, 20
                else:
                    return 0, x+2, 10
            elif test in left1:
                if y == 10:
                    return 0, 2, 10
                else:
                    return 0, 0, y+2

            elif test in cross1:
                if y == 5:
                    if where("왼쪽으로 꺾기? (y/n)"):
                        return 0, 3, 7
                    else:
                        return 0, 3, 3
                elif (1<=x<=4 and 6<=y<=9) or (6<=x<=9 and 1<=y<=4):
                    if x==1 and y==9:
                        return 0, 0, 10
                    return 0, x-2, y+2
                elif (1<=x<=4 and 1<=y<=4) or (6<=x<=9 and 6<=y<=9):
                    if x == 1 and y == 1:
                       return 0, 0, 0
                    return 0, x-2, y-2
        return num,x,y

    def fin(num,x,y):
        move_num = 0
        while num != 0:
            set(x,y)
            num,x,y = move(num,x,y,move_num)
            move_num += 1
        return x, y

    def mal_num_A(A1,mum,x,y):
        if mum == 0:
            return A1
        else:
            A1[mum - 1][0] = x
            A1[mum - 1][1] = y
            return A1

    def mal_num_B(B1,mum,x,y):
        if mum == 0:
            return B1
        else:
            B1[mum - 1][0] = x
            B1[mum - 1][1] = y
            return B1

    def throw():
        import random
        jipab = [{'도': 1}, {'도': 1}, {'도': 1},{'도': 1},\
             {'개': 2}, {'개': 2},{'개': 2},{'개': 2},{'개': 2},{'개': 2},\
             {'걸' : 3},{'걸' : 3},{'걸' : 3},{'걸' : 3}, \
             {'윷': 4},\
             {'모': 5}, {'빽도': -1}]
        n, k = [], []
        random.shuffle(jipab)
        j = jipab[random.randint(0, 15)]

        while j == {'윷' : 4} or j == {'모': 5}:
            
            print(list(j.keys())[0] + "!")
            if (list(j.keys())[0] == '도'):
                yutBlk = Matrix(y1)
                yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
                yuttBlk = yuttBlk+yutBlk
                oScreen.paste(yuttBlk, yuttop, turleft)
                drawmatrix(oScreen); print()
            elif (list(j.keys())[0] == '개'):
                yutBlk = Matrix(y3)
                yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
                yuttBlk = yuttBlk+yutBlk
                oScreen.paste(yuttBlk, yuttop, turleft)
                drawmatrix(oScreen); print()
            elif (list(j.keys())[0] == '걸'):
                yutBlk = Matrix(y4)
                yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
                yuttBlk = yuttBlk+yutBlk
                oScreen.paste(yuttBlk, yuttop, turleft)
                drawmatrix(oScreen); print()
            elif (list(j.keys())[0] == '윷'):
                yutBlk = Matrix(y5)
                yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
                yuttBlk = yuttBlk+yutBlk
                oScreen.paste(yuttBlk, yuttop, turleft)
                drawmatrix(oScreen); print()
            elif (list(j.keys())[0] == '모'):
                yutBlk = Matrix(y6)
                yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
                yuttBlk = yuttBlk+yutBlk
                oScreen.paste(yuttBlk, yuttop, turleft)
                drawmatrix(oScreen); print()
            elif (j == {'빽도': -1}):
                yutBlk = Matrix(y2)
                yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
                yuttBlk = yuttBlk+yutBlk
                oScreen.paste(yuttBlk, yuttop, turleft)
                drawmatrix(oScreen); print()
            input("한번 더!(엔터를 눌러주세요.)")
            n += list(j.keys())
            k.append(j)
            j = jipab[random.randint(0, 15)]
        print(list(j.keys())[0] + "!")
        if (list(j.keys())[0] == '도'):
            yutBlk = Matrix(y1)
            yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
            yuttBlk = yuttBlk+yutBlk
            oScreen.paste(yuttBlk, yuttop, turleft)
            drawmatrix(oScreen); print()
        elif (list(j.keys())[0] == '개'):
            yutBlk = Matrix(y3)
            yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
            yuttBlk = yuttBlk+yutBlk
            oScreen.paste(yuttBlk, yuttop, turleft)
            drawmatrix(oScreen); print()
        elif (list(j.keys())[0] == '걸'):
            yutBlk = Matrix(y4)
            yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
            yuttBlk = yuttBlk+yutBlk
            oScreen.paste(yuttBlk, yuttop, turleft)
            drawmatrix(oScreen); print()
        elif (list(j.keys())[0] == '윷'):
            yutBlk = Matrix(y5)
            yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
            yuttBlk = yuttBlk+yutBlk
            oScreen.paste(yuttBlk, yuttop, turleft)
            drawmatrix(oScreen); print()
        elif (list(j.keys())[0] == '모'):
            yutBlk = Matrix(y6)
            yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
            yuttBlk = yuttBlk+yutBlk
            oScreen.paste(yuttBlk, yuttop, turleft)
            drawmatrix(oScreen); print()
        elif (j == {'빽도': -1}):
            yutBlk = Matrix(y2)
            yuttBlk = iScreen.clip(yuttop, turleft, yuttop+yutBlk.get_dy(), turleft+yutBlk.get_dx())
            yuttBlk = yuttBlk+yutBlk
            oScreen.paste(yuttBlk, yuttop, turleft)
            drawmatrix(oScreen); print()
        k.append(j)
        n += list(j.keys())
        return n, k

    def where1(message):
        answer = input(message)
        while not (answer.isdigit() == True and (answer == '1' or answer =='2' or answer =='3' or answer =='4')):#(반복 조건):
            answer = input(message)
        return int(answer)#그냥 answer로 리턴하던 것에 int를 씌웠다.

    def origin_board():#깨끗한 놀이판, show_board에서만 사용한다.
        return [\
        ["◎ ","   ","○ ","   ","○","   ","○","   "," ○","   "," ◎"],\
        [" "," ○ "," ","   ","   ","   ","   ","   ","", " ○ "," "],\
        ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
        [" ","   ","  "," ○ ","  ","   ","  "," ○ ","  ","   "," "],\
        ["○","    "," ","    "," ","   ","  ","   ","  ","   ","○"],\
        [" ","   ","  ","   ","  "," ◎ ","  ","   ","  ","   ","  "],\
        ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
        [" ","   ","  "," ○ ","  ","   ","  "," ○ "," ","   ","  "],\
        ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
        [" "," ○ ","  ","   ","  ","   ","  ","   ","  "," ○ "," "],\
        ["◎ ","   ","○ ","   ","○","   ","○","   "," ○","   ","  ◎"]]

    def Acheck(top, left, acheck):
        if (acheck ==1):
            ah1top = top
            ah1left = left
            ah11Blk = iScreen.clip(ah1top, ah1left, ah1top+ah1Blk.get_dy(), ah1left+ah1Blk.get_dx())
            ah11Blk = ah11Blk+ah1Blk
            oScreen.paste(ah11Blk, ah1top, ah1left)
        elif (acheck ==2):
            ah2top = top
            ah2left = left
            
            ah22Blk = iScreen.clip(ah2top, ah2left, ah2top+ah2Blk.get_dy(), ah2left+ah2Blk.get_dx())
            ah22Blk = ah22Blk+ah2Blk
            oScreen.paste(ah22Blk, ah2top, ah2left)
        elif (acheck ==3):
            ah3top = top
            ah3left = left
            
            ah33Blk = iScreen.clip(ah3top, ah3left, ah3top+ah3Blk.get_dy(), ah3left+ah3Blk.get_dx())
            ah33Blk = ah33Blk+ah3Blk
            oScreen.paste(ah33Blk, ah3top, ah3left)
        elif (acheck ==4):
            ah4top = top
            ah4left = left
            
            ah44Blk = iScreen.clip(ah4top, ah4left, ah4top+ah4Blk.get_dy(), ah4left+ah4Blk.get_dx())
            ah44Blk = ah44Blk+ah4Blk
            oScreen.paste(ah44Blk, ah4top, ah4left)
                        
    def Bcheck(top, left, bcheck):
        if (bcheck ==1):
            bh1top = top
            bh1left = left
        
            bh11Blk = iScreen.clip(bh1top, bh1left, bh1top+bh1Blk.get_dy(), bh1left+bh1Blk.get_dx())
            bh11Blk = bh11Blk+bh1Blk
            oScreen.paste(bh11Blk, bh1top, bh1left)
        elif (bcheck ==2):
            bh2top = top
            bh2left = left
            
            bh22Blk = iScreen.clip(bh2top, bh2left, bh2top+bh2Blk.get_dy(), bh2left+bh2Blk.get_dx())
            bh22Blk = bh22Blk+bh2Blk
            oScreen.paste(bh22Blk, bh2top, bh2left)
        elif (bcheck ==3):
            bh3top = top
            bh3left = left
            
            bh33Blk = iScreen.clip(bh3top, bh3left, bh3top+bh3Blk.get_dy(), bh3left+bh3Blk.get_dx())
            bh33Blk = bh33Blk+bh3Blk
            oScreen.paste(bh33Blk, bh3top, bh3left)
        elif (bcheck ==4):
            bh4top = top
            bh4left = left
            
            bh44Blk = iScreen.clip(bh4top, bh4left, bh4top+bh4Blk.get_dy(), bh4left+bh4Blk.get_dx())
            bh44Blk = bh44Blk+bh4Blk
            oScreen.paste(bh44Blk, bh4top, bh4left)

    def show_board(A1, B1, X, Y):
        board = origin_board()#깨끗한 놀이판
        mum = 0
        #iScreen = Matrix(arrayboard)
        #oScreen = Matrix(iScreen)
        acheck = 0
        bcheck = 0
        for i in A1:#A팀의 말 입력
            acheck += 1
            if i != [10,10] and i != [20,20]:
                if (i == [0,0]):
                    top =13
                    left = 1
                    Acheck(top, left, acheck)
                    
                elif (i == [0,2]):
                    
                    top = 11
                    left = 1
                    Acheck(top, left, acheck)
                    
                elif (i == [0,4]):
                    top = 9
                    left = 1
                    Acheck(top, left, acheck)
                    
                elif (i == [0,6]):
                    
                    top = 7
                    left = 1
                    Acheck(top, left, acheck)
                    
                elif (i == [0,8]):
                    top = 5
                    left = 1
                    Acheck(top, left, acheck)
                    
                elif (i == [0,10]):
                    
                    top = 3
                    left = 1
                    Acheck(top, left, acheck)
                    
                elif (i == [1,1]):
                    
                    top = 12
                    left = 2
                    Acheck(top, left, acheck)
                    
                elif (i == [1,9]):
                    
                    top = 4
                    left = 2
                    Acheck(top, left, acheck)
                    
                elif (i == [2,0]):
                    
                    top = 13
                    left = 3
                    Acheck(top, left, acheck)
                    
                elif (i == [2,10]):
                    
                    top = 3
                    left = 3
                    Acheck(top, left, acheck)
                    
                elif (i == [3,3]):
                    
                    top = 10
                    left = 4
                    Acheck(top, left, acheck)
                    
                elif (i == [3,7]):
                    
                    top = 6
                    left = 4
                    Acheck(top, left, acheck)
                    
                elif (i == [4,0]):
                    
                    top = 13
                    left = 5
                    Acheck(top, left, acheck)
                    
                elif (i == [4,10]):
                    
                    top = 3
                    left = 5
                    Acheck(top, left, acheck)
                    
                elif (i == [5,5]):
                    
                    top = 8
                    left = 6
                    Acheck(top, left, acheck)
                    
                elif (i == [6,0]):
                   
                    top = 13
                    left = 7
                    Acheck(top, left, acheck)
                    
                elif (i == [6,10]):
                    
                    top = 3
                    left = 7
                    Acheck(top, left, acheck)
                    
                elif (i == [7,3]):
                    
                    top = 10
                    left = 8
                    Acheck(top, left, acheck)
                    
                elif (i == [7,7]):
                    
                    top = 6
                    left = 8
                    Acheck(top, left, acheck)
                    
                elif (i == [8,0]):
                    
                    ah1top =13
                    ah1left = 9
                    Acheck(top, left, acheck)
                    
                elif (i == [8,10]):
                    
                    top = 3
                    left = 9
                    Acheck(top, left, acheck)
                    
                elif (i == [9,1]):
                    
                    top = 12
                    left = 10
                    Acheck(top, left, acheck)
                    
                elif (i == [9,9]):
                    
                    top = 4
                    left = 10
                    Acheck(top, left, acheck)
                    
                elif (i == [10,0]):
                    
                    top = 13
                    left = 11
                    Acheck(top, left, acheck)
                    
                elif (i == [10,2]):
                    
                    top = 11
                    left = 11
                    Acheck(top, left, acheck)
                    
                elif (i == [10,4]):
                    
                    top = 9
                    left = 11
                    Acheck(top, left, acheck)
                    
                elif (i == [10,6]):
                    
                    top = 7
                    left = 11
                    Acheck(top, left, acheck)
                    
                elif (i == [10,8]):
                    
                    top = 5
                    left = 11
                    Acheck(top, left, acheck)
                    
                elif (i == [10,10]):
                    top = 3
                    left = 11
                    Acheck(top, left, acheck)
                    
            
                board[i[0]][i[1]] = X[mum]
            elif i == [10,10] and i == [20,20]:
                top = 14
                left = 22
                Acheck(top, left, acheck)
            mum += 1
        mum = 0
        for i in B1:#B팀의 말 입력
            bcheck += 1
            if i != [10,10] and i != [20,20]:
                if (i == [0,0]):
                    
                    top = 13
                    left = 1
                    Bcheck(top, left, bcheck)
                    
                elif (i == [0,2]):
                    
                    top = 11
                    left = 1
                    Bcheck(top, left, bcheck)
                elif (i == [0,4]):
                    top = 9
                    left = 1
                    Bcheck(top, left, bcheck)
                elif (i == [0,6]):
                    
                    top = 7
                    left = 1
                    Bcheck(top, left, bcheck)
                elif (i == [0,8]):
                    top = 5
                    left = 1
                    Bcheck(top, left, bcheck)
                elif (i == [0,10]):
                    
                    top = 3
                    left = 1
                    Bcheck(top, left, bcheck)
                elif (i == [1,1]):
                    
                    top = 12
                    left = 2
                    Bcheck(top, left, bcheck)
                elif (i == [1,9]):
                    
                    top = 4
                    left = 2
                    Bcheck(top, left, bcheck)
                elif (i == [2,0]):
                    
                    top = 13
                    left = 3
                    Bcheck(top, left, bcheck)
                elif (i == [2,10]):
                    
                    top = 3
                    left = 3
                    Bcheck(top, left, bcheck)
                elif (i == [3,3]):
                    
                    top = 10
                    left = 4
                    Bcheck(top, left, bcheck)
                elif (i == [3,7]):
                    
                    top = 6
                    left = 4
                    Bcheck(top, left, bcheck)
                elif (i == [4,0]):
                    
                    top = 13
                    left = 5
                    Bcheck(top, left, bcheck)
                elif (i == [4,10]):
                    
                    top = 3
                    left = 5
                    Bcheck(top, left, bcheck)
                elif (i == [5,5]):
                    
                    top = 8
                    left = 6
                    Bcheck(top, left, bcheck)
                elif (i == [6,0]):
                    
                    top = 13
                    left = 7
                    Bcheck(top, left, bcheck)
                elif (i == [6,10]):
                    
                    top = 3
                    left = 7
                    Bcheck(top, left, bcheck)
                elif (i == [7,3]):
                    
                    top = 10
                    left = 8
                    Bcheck(top, left, bcheck)
                elif (i == [7,7]):
                    
                    top = 6
                    left = 8
                    Bcheck(top, left, bcheck)
                elif (i == [8,0]):
                    
                    top = 13
                    left = 9
                    Bcheck(top, left, bcheck)
                elif (i == [8,10]):
                    
                    top = 3
                    left = 9
                    Bcheck(top, left, bcheck)
                elif (i == [9,1]):
                    
                    top = 12
                    left = 10
                    Bcheck(top, left, bcheck)
                elif (i == [9,9]):
                    
                    top = 4
                    left = 10
                    Bcheck(top, left, bcheck)
                elif (i == [10,0]):
                    
                    top = 13
                    left = 11
                    Bcheck(top, left, bcheck)
                elif (i == [10,2]):
                    
                    top = 11
                    left = 11
                    Bcheck(top, left, bcheck)
                elif (i == [10,4]):
                    
                    top = 9
                    left = 11
                    Bcheck(top, left, bcheck)
                elif (i == [10,6]):
                    
                    top = 7
                    left = 11
                    Bcheck(top, left, bcheck)
                elif (i == [10,8]):
                   
                    top = 5
                    left = 11
                    Bcheck(top, left, bcheck)
                elif (i == [10,10]):
                    
                    top = 3
                    left = 11
                    Bcheck(top, left, bcheck)
                board[i[0]][i[1]] = Y[mum]
            mum += 1
        #ah11Blk = iScreen.clip(ah1top, ah1left, ah1top+ah1Blk.get_dy(), ah1left+ah1Blk.get_dx())
        #ah11Blk = ah11Blk+ah1Blk
        #oScreen.paste(ah11Blk, ah1top, ah1left)
        #ah11Blk = iScreen.clip(ah2top, ah2left, ah2top+ah2Blk.get_dy(), ah2left+ah2Blk.get_dx())
        #ah11Blk = ah11Blk+ah1Blk
        #ah33Blk = iScreen.clip(ah3top, ah3left, ah3top+ah3Blk.get_dy(), ah3left+ah3Blk.get_dx())
        #ah33Blk = ah33Blk+ah3Blk
        #oScreen.paste(ah33Blk, ah3top, ah3left)
        #ah44Blk = iScreen.clip(ah4top, ah4left, ah4top+ah4Blk.get_dy(), ah4left+ah4Blk.get_dx())
        #ah44Blk = ah44Blk+ah4Blk
        #oScreen.paste(ah44Blk, ah4top, ah4left)
        #bh11Blk = iScreen.clip(bh1top, bh1left, bh1top+bh1Blk.get_dy(), bh1left+bh1Blk.get_dx())
        #bh11Blk = bh11Blk+bh1Blk
        #oScreen.paste(bh11Blk, bh1top, bh1left)
        #bh22Blk = iScreen.clip(bh2top, bh2left, bh2top+bh2Blk.get_dy(), bh2left+bh2Blk.get_dx())
        #bh22Blk = bh22Blk+bh2Blk
        #oScreen.paste(bh22Blk, bh2top, bh2left)
        #bh33Blk = iScreen.clip(bh3top, bh3left, bh3top+bh3Blk.get_dy(), bh3left+bh3Blk.get_dx())
        #bh33Blk = bh33Blk+bh3Blk
        #oScreen.paste(bh33Blk, bh3top, bh3left)
        #bh44Blk = iScreen.clip(bh4top, bh4left, bh4top+bh4Blk.get_dy(), bh4left+bh4Blk.get_dx())
        #bh44Blk = bh44Blk+bh4Blk
        #oScreen.paste(bh44Blk, bh4top, bh4left)
        #drawmatrix(oScreen); print()
        for row in board:
            for x in range(11):
                print(row[x], end='')
            print()
        

    def same_pos_A(mum,A1,B1):
        for i in range(4):
            if (mum-1 != i) and (A1[mum-1] == A1[i]) and (A1[mum-1] != [10,10]) and (A1[mum-1] != [20,20]):
               return 1 #아군의 말과 같은 위치일 때
            elif (A1[mum-1] == B1[i]) and (B1[i] != [10,10]) and (B1[i] != [20,20]):
                 B1[i] = [10,10]
                 return 0
        return 2

    def same_pos_B(mum,A1,B1):
        for i in range(4):
            if (mum-1 != i) and (B1[mum-1] == B1[i]) and (B1[mum-1] != [10,10]) and (B1[mum-1] != [20,20]):
               return 1
            elif B1[mum-1] == A1[i] and (A1[i] != [10,10]) and (A1[i] != [20,20]):
                 A1[i] = [10,10]
                 return 0
        return 2

    def mal_E_up_seong(X):
        count = 0
        for a in X:
            if a in [[10,10],[20,20]]:
               count += 1
        if count == 4:
           return True
        else:
            return False
    LED_init()
    def main():
        print("Contradiction 윷놀이에 오신 것을 환영합니다!")
        usernameA, passwdA, triesA, winsA = 'A', 'A', 0,0
        usernameB, passwdB, triesB, winsB = 'B','B',0,0
        Games = 1
        X = ["❶", "❷", "❸", "❹"]
        Y = ["➀", "➁", "➂", "➃"]
        A1 = [[10, 10], [10, 10], [10, 10], [10, 10]]
        B1 = [[10, 10], [10, 10], [10, 10], [10, 10]]
        n, k = [],[]
        while True:
              #iScreen = Matrix(arrayboard)
              #oScreen = Matrix(iScreen)
              ter = ater
              aBlk = Matrix(ter)
              aattBlk = iScreen.clip(atop, aleft, atop+aBlk.get_dy(), aleft+aBlk.get_dx())
              aattBlk = aattBlk+aBlk
              oScreen.paste(aattBlk, atop, aleft)
              drawmatrix(oScreen); print()
            
              input("A팀의 턴입니다!\n엔터키를 눌러 윷을 던져주세요.")
              n1, k1 = throw()
              n += n1
              k += k1
              while n != []:
                    if n == ['빽도'] and mal_E_up_seong(A1):
                       print("이런! 움직일 수 있는 말이 없네요. 턴이 넘어갑니다.")
                       n,k = [],[]#빽도 치워주기
                       break
                    if len(n)>1:#윷을 여러번 던졌을 때
                       print(n)
                       z = input("어느 것으로 먼저 움직이시겠습니까? A는 도 B는 개 C는 걸 D는 윷 E는 모 F는 빽도")
                       while not ((z == "A") or (z == "B") or (z == "C") or (z == "D") or (z == "E") or (z == "F")):
                             if z not in n:#한글이 맞지만 뽑은 것이 아닐 경우
                                z = input("제대로 선택해 주십시오.")
                             else:#뭣도 아닐 경우
                                 z = input("제대로 선택해 주십시오")
                       if (z == "A"):
                           z = "도"
                       elif (z == "B"):
                           z = "개"
                       elif (z == "C"):
                           z = "걸"
                       elif (z == "D"):
                           z = "윷"
                       elif (z == "E"):
                           z = "모"
                       elif (z == "F"):
                           z = "빽도"
                                
                    else:#한번만 뽑았을 때
                        z = n[0]
                    mum = where1("몇번 말을 움직이시겠습니까?")
                    while z == '빽도' and A1[mum-1] == [10,10]:
                          mum = where1("해당 말은 빽도로 움직일 수 없는 위치에 있습니다.\n다른 말을 선택해 주세요.")
                    while A1[mum-1] == [20,20]:#이미 완주한 말을 움직이려 할 때
                          mum = int(input("해당 말은 이미 완주했습니다.\n다른 말을 선택해 주세요."))
                    x1, y1 = A1[mum - 1][0], A1[mum - 1][1]#움직이려는 말의 위치정보
                    x, y = fin(k[n.index(z)][z],x1,y1)#움직였을 때의 위치정보
                    A1 = mal_num_A(A1, mum, x, y)
                    p = same_pos_A(mum,A1,B1)#p는 0에서2중에 하나의 정수
                    while p == 1 or p == 0:
                          if p == 1:
                             x, y = fin(1,A1[mum-1][0],A1[mum-1][1])
                             A1 = mal_num_A(A1, mum, x, y)
                             print('점프!')
                             p = same_pos_A(mum,A1,B1)
                          elif p == 0:
                               show_board(A1, B1, X, Y)
                               print("상대의 말을 잡았습니다!")
                               input("한번 더 윷을 던질 수 있습니다. 엔터를 눌러주세요.")
                               n1, k1 = throw()#추가던지기
                               n += n1
                               k += k1
                               p = same_pos_A(mum,A1,B1)
                    ah1Blk= Matrix(ah1)
                    
                    show_board(A1, B1, X, Y)
                    k.remove(k[n.index(z)])
                    n.remove(z)
                    if A1 == [[20,20],[20,20],[20,20],[20,20]]:#승리조건
                        WA, WB = 1, 0
                        members[usernameA] = (passwdA, triesA + Games, winsA + WA)
                        members[usernameB] = (passwdB, triesB + Games, winsB + WB)
                        endScreen = Matrix(endgameA)
                        draw_matrix(endScreen); print()
                        return print("A팀의 승리입니다!")
              ter = bter
              aBlk = Matrix(ter)
              aattBlk = iScreen.clip(atop, aleft, atop+aBlk.get_dy(), aleft+aBlk.get_dx())
              aattBlk = aattBlk+aBlk
              oScreen.paste(aattBlk, atop, aleft)
              drawmatrix(oScreen); print()
              input("B팀의 턴입니다!\n엔터키를 눌러 윷을 던져주세요.")
              n1, k1 = throw()
              n += n1
              k += k1
              while n != []:
                    if n == ['빽도'] and mal_E_up_seong(B1):
                       print("이런! 움직일 수 있는 말이 없네요. 턴이 넘어갑니다.")
                       n, k = [], []
                       break
                    if len(n)>1:
                       print(n)
                       z = input("어느 것으로 먼저 움직이시겠습니까? A는 도 B는 개 C는 걸 D는 윷 E는 모 F는 빽도")
                       while not ((z == "A") or (z == "B") or (z == "C") or (z == "D") or (z == "E") or (z == "F")):
                             if z not in n:
                                z = input("제대로 선택해 주십시오.")
                             else:
                                 z = input("제대로 선택해 주십시오")
                       if (z == "A"):
                           z = "도"
                       elif (z == "B"):
                           z = "개"
                       elif (z == "C"):
                           z = "걸"
                       elif (z == "D"):
                           z = "윷"
                       elif (z == "E"):
                           z = "모"
                       elif (z == "F"):
                           z = "빽도"
                        
                        
                    else:
                        z = n[0]
                    mum = where1("몇번 말을 움직이시겠습니까?")
                    while (z == '빽도' and B1[mum-1] == [10,10]):
                          mum = where1("해당 말은 빽도로 움직일 수 없는 위치에 있습니다.\n다른 말을 선택해 주세요.")
                    while B1[mum - 1] == [20, 20]:
                        mum = int(input("해당 말은 이미 완주했습니다.\n다른 말을 선택해 주세요."))
                    x1, y1 = B1[mum - 1][0], B1[mum - 1][1]
                    x, y = fin(k[n.index(z)][z], x1, y1)
                    B1 = mal_num_B(B1, mum, x, y)
                    p = same_pos_B(mum, A1, B1)
                    while p == 1 or p == 0:
                          if p == 1:
                             x, y = fin(1, B1[mum-1][0], B1[mum-1][1])
                             B1 = mal_num_B(B1, mum, x, y)
                             print('점프!')
                             p = same_pos_B(mum, A1, B1)
                          elif p == 0:
                               show_board(A1, B1, X, Y)
                               print("상대의 말을 잡았습니다!")
                               input("한번 더 윷을 던질 수 있습니다. 엔터를 눌러주세요.")
                               n1, k1 = throw()
                               n += n1
                               k += k1
                               p = same_pos_B(mum, A1, B1)
                    show_board(A1, B1, X, Y)
                    k.remove(k[n.index(z)])
                    n.remove(z)
                    if B1 == [[20, 20], [20, 20], [20, 20], [20, 20]]:
                        WA, WB = 0, 1
                        members[usernameA] = (passwdA, triesA + Games, winsA + WA)
                        members[usernameB] = (passwdB, triesB + Games, winsB + WB)
                  
                        endScreen = Matrix(endgameB)
                        draw_matrix(endScreen); print()
                        return print("B팀의 승리입니다!")
    main()
    
while True:
    a=input("1.DuDuZi\n2.Baam\n3.tetris\n4.carRRacing\n5.yut_game_2p\n6.yut_game\n\n")
    if a=='1':
        molegame()
    elif a=='2':
        snakeGame()
    elif a=='3':
        tetris()
    elif a=='4':
        carRRacing()
    elif a=='5':
        yut_game_2p()
    elif a=='6':
        yut_game()