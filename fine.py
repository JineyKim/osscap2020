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
            time.sleep(2)
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



molegame()
snakeGame()