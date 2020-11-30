from matrix import *
import LED_display as LMD
import threading

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

arrayboard = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,7,0,7,0,7,0,7,0,7,0,7,0,0,0],
    [0,0,0,7,0,0,0,0,0,0,0,7,0,0,0,0],
    [0,0,7,0,0,0,0,0,0,0,0,0,7,0,0,0],
    [0,0,0,0,0,7,0,0,0,7,0,0,0,0,0,0],
    [0,0,7,0,0,0,0,0,0,0,0,0,7,0,0,0],
    [0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0],
    [0,0,7,0,0,0,0,0,0,0,0,0,7,0,0,0],
    [0,0,0,0,0,7,0,0,0,7,0,0,0,0,0,0],
    [0,0,7,0,0,0,0,0,0,0,0,0,7,0,0,0],
    [0,0,0,7,0,0,0,0,0,0,0,7,0,0,0,0],
    [0,0,7,0,7,0,7,0,7,0,7,0,7,0,0,0],
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
#y1 도
y1 = [[1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0],
      [1,2,1,0,1,2,1,0,1,2,1,0,1,1,1,0],
      [1,2,1,0,1,2,1,0,1,2,1,0,1,1,1,0],
      [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0]]
#y2 빽도
y2 = [[1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0],
      [1,2,1,0,1,2,1,0,1,2,1,0,1,3,1,0],
      [1,2,1,0,1,2,1,0,1,2,1,0,1,3,1,0],
      [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0]]
#y3 개
y3 = [[1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0],
      [1,2,1,0,1,2,1,0,1,1,1,0,1,1,1,0],
      [1,2,1,0,1,2,1,0,1,1,1,0,1,1,1,0],
      [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0]]
#y4 걸
y4 = [[1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0],
      [1,2,1,0,1,1,1,0,1,1,1,0,1,1,1,0],
      [1,2,1,0,1,1,1,0,1,1,1,0,1,1,1,0],
      [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0]]
#y5 윷
y5 = [[1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0],
      [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0],
      [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0],
      [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0]]

#y6 모
y6 = [[1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0],
      [1,2,1,0,1,2,1,0,1,2,1,0,1,2,1,0],
      [1,2,1,0,1,2,1,0,1,2,1,0,1,2,1,0],
      [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0]]
#A
ater = [[1]]
atop = 20
aleft = 1
#b턴
bter = [[4]]
btop = 20
btop = 1
ter = ater
#endgame A
endgameA = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,3,0,0,0,0,3,0,0,0,0,3,0,0,0],
    [0,0,3,3,0,0,3,0,3,0,0,3,3,0,0,0],
    [0,0,3,0,3,3,0,0,0,3,3,0,3,0,0,0],
    [0,0,3,0,0,0,0,0,0,0,0,0,3,0,0,0],
    [0,0,3,0,0,0,0,0,0,0,0,0,3,0,0,0],
    [0,0,3,0,0,0,0,0,0,0,0,0,3,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
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

#endgame B
endgameB = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,3,0,0,0,0,3,0,0,0,0,3,0,0,0],
    [0,0,3,3,0,0,3,0,3,0,0,3,3,0,0,0],
    [0,0,3,0,3,3,0,0,0,3,3,0,3,0,0,0],
    [0,0,3,0,0,0,0,0,0,0,0,0,3,0,0,0],
    [0,0,3,0,0,0,0,0,0,0,0,0,3,0,0,0],
    [0,0,3,0,0,0,0,0,0,0,0,0,3,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,4,4,4,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,4,0,0,4,0,0,0,0,0,0],
    [0,0,0,0,0,0,4,4,4,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,4,0,0,4,0,0,0,0,0,0],
    [0,0,0,0,0,0,4,0,0,4,0,0,0,0,0,0],
    [0,0,0,0,0,0,4,4,4,0,0,0,0,0,0,0],
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
top = 15
left = 0
iScreen = Matrix(arrayboard)
oScreen = Matrix(iScreen)
yutBlk = Matrix(y1)
yuttop = 15
turleft = 0
#led그리
def drawmatrix(m):
    array = m.get_array()
    for x in range(len(array)):
        for y in range(len(array[0])):
            if array[x][y] == 0:
                LMD.set_pixel(x, y, 0)
            elif array[x][y] == 1:
                LMD.set_pixel(x, y, 1)
            elif array[x][y] == 2:
                LMD.set_pixel(x, y, 2)
            elif array[x][y] == 3:
                LMD.set_pixel(x, y, 3)
            elif array[x][y] == 4:
                LMD.set_pixel(x, y, 4)
            elif array[x][y] == 5:
                LMD.set_pixel(x, y, 5)
            elif array[x][y] == 6:
                LMD.set_pixel(x, y, 6)
            elif array[x][y] == 7:
                LMD.set_pixel(x, y, 7)
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



def show_board(A1, B1, X, Y):
    board = origin_board()#깨끗한 놀이판
    mum = 0
    iScreen = Matrix(arrayScreen)
    oScreen = Matrix(iScreen)
    arrayScreen1 = list(arrayScreen)
    for i in A1:#A팀의 말 입력
        if i != [10,10] and i != [20,20]:
            if (i == [0,0]):
                arrayScreen1[1][2] = 1
            elif (i == [0,2]):
                arrayScreen1[1][4] = 1
            elif (i == [0,4]):
                arrayScreen1[1][6] = 1
            elif (i == [0,6]):
                arrayScreen1[1][8] = 1
            elif (i == [0,8]):
                arrayScreen1[1][10] = 1
            elif (i == [0,10]):
                arrayScreen1[1][12] = 1
            elif (i == [1,1]):
                arrayScreen1[2][3] = 1
            elif (i == [1,9]):
                arrayScreen1[2][11] = 1
            elif (i == [2,0]):
                arrayScreen1[3][2] = 1
            elif (i == [2,10]):
                arrayScreen1[3][12] = 1
            elif (i == [3,3]):
                arrayScreen1[4][5] = 1
            elif (i == [3,7]):
                arrayScreen1[4][9] = 1
            elif (i == [4,0]):
                arrayScreen1[5][2] = 1
            elif (i == [4,10]):
                arrayScreen1[5][12] = 1
            elif (i == [5,5]):
                arrayScreen1[6][7] = 1
            elif (i == [6,0]):
                arrayScreen1[7][2] = 1
            elif (i == [6,10]):
                arrayScreen1[7][12] = 1
            elif (i == [7,3]):
                arrayScreen1[8][5] = 1
            elif (i == [7,7]):
                arrayScreen1[8][9] = 1
            elif (i == [8,0]):
                arrayScreen1[9][2] = 1
            elif (i == [8,10]):
                arrayScreen1[9][12] = 1
            elif (i == [9,1]):
                arrayScreen1[10][3] = 1
            elif (i == [9,9]):
                arrayScreen1[10][11] = 1
            elif (i == [10,0]):
                arrayScreen1[11][2] = 1
            elif (i == [10,2]):
                arrayScreen1[11][4] = 1
            elif (i == [10,4]):
                arrayScreen1[11][6] = 1
            elif (i == [10,6]):
                arrayScreen1[11][8] = 1
            elif (i == [10,8]):
                arrayScreen1[11][10] = 1
            elif (i == [10,10]):
                arrayScreen1[11][12] = 1
            board[i[0]][i[1]] = X[mum]
        mum += 1
    mum = 0
    for i in B1:#B팀의 말 입력
        if i != [10,10] and i != [20,20]:
            if (i == [0,0]):
                arrayScreen1[1][2] = 4
            elif (i == [0,2]):
                arrayScreen1[1][4] = 4
            elif (i == [0,4]):
                arrayScreen1[1][6] = 4
            elif (i == [0,6]):
                arrayScreen1[1][8] = 4
            elif (i == [0,8]):
                arrayScreen1[1][10] = 4
            elif (i == [0,10]):
                arrayScreen1[1][12] = 4
            elif (i == [1,1]):
                arrayScreen1[2][3] = 4
            elif (i == [1,9]):
                arrayScreen1[2][11] = 4
            elif (i == [2,0]):
                arrayScreen1[3][2] = 4
            elif (i == [2,10]):
                arrayScreen1[3][12] = 4
            elif (i == [3,3]):
                arrayScreen1[4][5] = 4
            elif (i == [3,7]):
                arrayScreen1[4][9] = 4
            elif (i == [4,0]):
                arrayScreen1[5][2] = 4
            elif (i == [4,10]):
                arrayScreen1[5][12] = 4
            elif (i == [5,5]):
                arrayScreen1[6][7] = 4
            elif (i == [6,0]):
                arrayScreen1[7][2] = 4
            elif (i == [6,10]):
                arrayScreen1[7][12] = 4
            elif (i == [7,3]):
                arrayScreen1[8][5] = 4
            elif (i == [7,7]):
                arrayScreen1[8][9] = 4
            elif (i == [8,0]):
                arrayScreen1[9][2] = 4
            elif (i == [8,10]):
                arrayScreen1[9][12] = 4
            elif (i == [9,1]):
                arrayScreen1[10][3] = 4
            elif (i == [9,9]):
                arrayScreen1[10][11] = 4
            elif (i == [10,0]):
                arrayScreen1[11][2] = 4
            elif (i == [10,2]):
                arrayScreen1[11][4] = 4
            elif (i == [10,4]):
                arrayScreen1[11][6] = 4
            elif (i == [10,6]):
                arrayScreen1[11][8] = 4
            elif (i == [10,8]):
                arrayScreen1[11][10] = 4
            elif (i == [10,10]):
                arrayScreen1[11][12] = 4
            board[i[0]][i[1]] = Y[mum]
        mum += 1
    iScreen = Matrix(arrayScreen1)
    oScreen = Matrix(iScreen)
    drawmatrix(oScreen); print()
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
def main_game():
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
                   z = input("어느 것으로 먼저 움직이시겠습니까?")
                   while not ((z == "도") or (z == "개") or (z == "걸") or (z == "윷") or (z == "모") or (z == "빽도")):
                         if z not in n:#한글이 맞지만 뽑은 것이 아닐 경우
                            z = input("제대로 선택해 주십시오.")
                         else:#뭣도 아닐 경우
                             z = input("제대로 선택해 주십시오")
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
                if A1 == [[20,20],[20,20],[20,20],[20,20]]:#승리조건
                    WA, WB = 1, 0
                    members[usernameA] = (passwdA, triesA + Games, winsA + WA)
                    members[usernameB] = (passwdB, triesB + Games, winsB + WB)

                    return print("A팀의 승리입니다!")
          ter = ater
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
                   z = input("어느 것으로 먼저 움직이시겠습니까?")
                   while not ((z == "도") or (z == "개") or (z == "걸") or (z == "윷") or (z == "모") or (z == "빽도")):
                         if z not in n:
                            z = input("제대로 선택해 주십시오.")
                         else:
                             z = input("제대로 선택해 주십시오")
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

                    return print("B팀의 승리입니다!")

main_game()
# throw()
# show_board()
