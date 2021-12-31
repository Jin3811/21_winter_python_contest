# start : 2021.12.18
# end : 2021.12.31
# made by Heo jin woo

from tkinter import *
from tkinter import font, messagebox
from random import randint

def gameover(): # 게임 오버 안내화면
    messagebox.showinfo("2048!", "Gameover!")
    
def success():
    messagebox.showinfo("congratuation!", "Success!!")

def is_success(): # 2048을 만드는데 성공했는지 판단하는 함수
    global board
    
    for i in board:
        for j in i:
            if j == 2048: # 2048이 있으면 
                return True
    
    return False # 없다면 false

def is_GameOver(): # 게임오버인지 판단하는 함수
    global board # board를 전역에서 갖고 온다.
    
    # 세로 방향으로 먼저 판단한다
    for y in range(4):
        column = board[y][0]
        if column == 0: # 빈 블럭이라면
            return False # 움직이는게 가능하므로 false
        else :
            for x in range(1, 4): # 2번째 줄부터 비교한다
                if board[y][x] == column or board[y][x] == 0: # 바로 아래의 블럭이 같은 숫자거나, 비어있다면
                    return False # 움직는게 가능하므로 false 
                else : # 아니라면 
                    column = board[y][x] # 블럭 갱신
    
    # 가로방향으로 판단, 방법은 위와 동일
    for x in range(4):
        row = board[0][x]
        if row == 0:
            return False
        for y in range(1, 4):
            if board[y][x] == row or board[y][x] == 0:
                return False
            else:
                row = board[y][x]
    
    # 위 과정을 모두 거쳐 return false가 일어나지 않았다는 것은 곧 True라는 뜻.
    return True

# 확률적으로 초기 블럭을 생성하는 함수. 90%의 확률로 2, 10%의 확률로 4가 나온다.
def generateNumberBlock(): 
    temp = randint(1, 10)
    if temp < 10 : 
        return 2
    else : 
        return 4

def display(): # 블록을 출력하는 함수
    global board, boardLabel, score, scoreMax # 전역에서 가져온다.
    
    # 각 블록의 숫자에 맞춰 블록의 정보를 갱신
    for y in range(4):
        for x in range(4):
            if board[y][x] <= 2048:
                blockData = numBlockData[board[y][x]]
                boardLabel[y][x].config(text = blockData[0], bg = blockData[1], fg = blockData[2])
            else:
                blockData = numBlockData["super"]
                boardLabel[y][x].config(text=str(board[y][x]), bg = blockData[1], fg = blockData[2])
    
    # 만약 게임 오버라면
    if is_GameOver():
        # 최고 기록 갱신
        if score > scoreMax: 
            scoreMax = score
            
        gameover() # 게임오버 처리
    
    # 2048을 만드는데 성공했다면
    elif is_success():
        success() # 성공 안내.
    
    # 점수 출력
    label_score.config(text = str(score))
    label_maxScore.config(text = str(scoreMax))
    

def gameInit(): # 게임 초기화
    global board, score, scoreMax, boardLabel # 전역에서 가지고 온다.
    i = 0 # 반복을 위한 인자
    if score > scoreMax: # 현 점수가 최고기록이라면
        scoreMax = score # 최고기록 갱신
    score = 0 # 점수 초기화
    
    # 맨 처음 모든 블럭을 빈 블럭으로 바꾼다.
    blockdata = numBlockData[0] 
    for y in range(4):
        for x in range(4):
            board[y][x] = 0
            boardLabel[y][x].config(text = blockdata[0], bg = blockdata[1], fg = blockdata[2])
    
    cnt = randint(1,2) # 블럭을 한번 생성할지 두번 생성할지 랜덤으로 결정
    
    # 생성
    while i < cnt: 
        x, y = randint(0, 3), randint(0, 3)
        
        if board[y][x] == 0 : # 중복방지
            board[y][x] = generateNumberBlock()
            i += 1
        else : # 중복된 블럭을 선택했다면 다시 한다.
            i -= 1
    
    # 생성한 후에 출력한다.
    display()

def rotate(n): # 시계방향으로 90*n 도 만큼 회전시킨다.
    global board
    
    # n번 회전한다.
    for i in range(n):
        templist = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
        
        # board의 원형을 복사한다.
        for y in range(4):
            for x in range(4):
                templist[y][x] = board[y][x]
        
        # 시계방향 90도 회전시킨다.
        for y in range(4):
            for x in range(4):
                board[x][3 - y] = templist[y][x]
    
def moveBlock(): # 모든 블록을 위로 올리는 함수.
    global board, score
    is_moved = False # 이동이 있었는지 검사하는 변수
    is_plus = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]] # 합쳐진 블럭의 위치를 저장할 리스트
    tempYcor = -1 # 자신의 윗 블럭의 y좌표를 저장할 변수
    
    for y in range(1, 4):
        for x in range(4):
            if board[y][x] != 0: # 숫자 블록이라면
                tempYcor = y - 1 # board[y][x]의 윗블록을 지정
                
                while tempYcor > 0 and board[tempYcor][x] == 0: # 윗 블록이 최상단이 아니고, 빈 블럭이라면 
                    tempYcor -= 1 # 그 윗블록으로 이동 -> 이 과정을 통해, 최상단에 도달하거나, 숫자블록의 위치를 알게 된다.
                
                if board[tempYcor][x] == 0: # 이 경우에 잡히는 경우는, board[y][x]의 위에 아무 블록도 없는 경우이다.
                    board[tempYcor][x] = board[y][x] # 숫자를 이동시키고,
                    board[y][x] = 0 # 원래 위치를 비운다.
                    is_moved = True # 이동이 발생했으므로 true를 대입
                
                elif board[tempYcor][x] != board[y][x]: # board[y][x] 위에 블럭이 있고, 이 블럭이 자신과 숫자가 같지 않다면
                    if tempYcor == y - 1: # 그 블록이 board[y][x]의 바로 위에 있다면,
                        continue # 반복문으로 돌아간다
                    
                    else : # 바로 위의 블록이 아니라면,
                        board[tempYcor + 1][x] = board[y][x] # 숫자가 다르기 때문에, 합치지 않고, 그 밑으로 이동시킨다.
                        board[y][x] = 0 # 원래 위치는 비운다.
                        is_moved = True # 이동이 발생했으므로 true를 대입

                else : # board[y][x] 위에 블럭이 있고 숫자가 같다면,
                    if is_plus[tempYcor][x] == 0: # 합쳐지지 않은 블럭이라면
                        board[tempYcor][x] *= 2 # 블럭을 합친다.
                        score += board[tempYcor][x] # 만들어낸 블럭의 숫자만큼 점수 증가
                        board[y][x] = 0 # 원래 위치는 비운다.
                        is_plus[tempYcor][x] = 1 # 합쳐졌으므로 기록
                        is_moved = True # 이동이 발생했으므로 true를 대입
                    
                    else : # 이전에 합쳐진 블럭이라면
                        board[tempYcor + 1][x] = board[y][x] # 합쳐졌던 블럭에는 합치면 안되므로, 그 아래로 이동한다.
                        board[y][x] = 0 # 원래 위치는 비운다.
                        is_moved = True # 이동이 발생했으므로 true를 대입
                        
    if is_moved: # 움직임이 있다면
        while True: # 빈 블럭을 찾는다
            x, y = randint(0, 3), randint(0, 3)
            if board[y][x] == 0: break
        board[y][x] = generateNumberBlock() # 빈 블럭에 랜덤으로 숫자 블럭 생성
               
def rotateUp(): # 윗버튼이 눌렸을 때
    moveBlock() # 위로 올리고
    display() # 출력

def rotateDown(): # 아래버튼이 눌렸을 때
    rotate(2) # 시계방향으로 180도 돌린 후에,
    moveBlock() # 위로 올리고
    rotate(2) # 원상태로 다시 돌린다
    display() # 출력
    
def rotateLeft(): # 왼쪽 버튼이 눌렸을 때
    rotate(1) # 시계방향으로 90도 돌리고
    moveBlock() # 위로 올린 후에
    rotate(3) # 원상태로 돌리고
    display() # 출력

def rotateRight():
    rotate(3) # 시계방향으로 270도 돌리고
    moveBlock() # 위로 올린 후에
    rotate(1) # 원상태로 돌리고
    display() # 출력

board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] # 게임 상황을 숫자로 저장
scoreMax = 0 # 최대 점수
score = 0 # 현재 점수
tk = Tk() # main window
remote = Tk() # remote window

# font/GameBold2048.ttf, need to download
# ("GameBold2048", 22)
gamefont = font.Font(family = "GameBold2048", size = 22) # 폰트 설정

numBlockData = { # 각 블록의 숫자, 색상을 저장한 딕셔너리
    # (text, bg, fg) -> tuple
    0 : (" ", "#cdc1b4", "black"),
    2 : ("2", "#eee4da", "black"),
    4 : ("4", "#ede0c8", "black"),
    8 : ("8", "#f2b179", "#f9f6f2"),
    16 : ("16", "#f59563", "#f9f6f2"),
    32 : ("32", "#f67c5f", "#f9f6f2"),
    64 : ("64", "#f65e3b", "#f9f6f2"),
    128 : ("128", "#edcf72", "#f9f6f2"),
    256 : ("256", "#edcc61", "#f9f6f2"),
    512 : ("512", "#edc850", "#f9f6f2"),
    1024 : ("1024", "#edc53f", "#f9f6f2"),
    2048 : ("2048", "#edc22e", "#f9f6f2"),
    "super" : ("super", "#3c3a32", "#f9f6f2") # if (tile > 2048) == True
}

# window setup
tk.title("2048!")
remote.title("2048! remote")
tk.geometry("688x989")
remote.geometry("500x400")
tk.resizable(False, False)
remote.resizable(False, False)

# tk window setup
label_bg = Label(tk, width = 100, height = 100, bg = "#f9f6f2") # 백그라운드 색을 위한 라벨
label_title = Label(tk, text = "2048!", font = ("GameBold2048", 56), bg = "#f9f6f2", fg = "#8f7a66")  # 게임 이름을 위한 라벨
label_score = Label(tk, text = "0", font = gamefont, width = 7, height = 1, bg = "#bbada0", fg = "white") # 점수 라벨
label_scoreboard = Label(tk, text = "SCORE", font = gamefont, width = 7, height = 2, bg = "#bbada0", fg = "white") # 점수 라벨을 보여주는 블록
label_maxScore = Label(tk, text = "0", font = gamefont, width = 7, height = 1, bg = "#bbada0", fg = "white") # 최대 점수 라벨 
label_maxScoreboard = Label(tk, text = "BEST", font = gamefont, width = 7, height = 2, bg = "#bbada0", fg = "white") # 최대 점수를 보여주는 블록
label_guide = Label(tk, text = "please, download font,\nGameBold2048.ttf", font = ("GameBold2048", 16) , bg = "#f9f6f2", fg = "black") # 폰트파일을 받도록 안내하는 라벨
label_gameboard = Label(tk, width = 71, height = 30, bg = "#bbada0") # 게임 보드

# 숫자 블록
label_block_1_1 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_1_2 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_1_3 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_1_4 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_2_1 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_2_2 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_2_3 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_2_4 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_3_1 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_3_2 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_3_3 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_3_4 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_4_1 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_4_2 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_4_3 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)
label_block_4_4 = Label(tk, text = " ", font = gamefont, width = 7, height = 3)

# 조작하기 쉽게 숫자 블록들을 리스트로 묶어놓는다.
boardLabel = [
    [label_block_1_1, label_block_1_2, label_block_1_3, label_block_1_4],
    [label_block_2_1, label_block_2_2, label_block_2_3, label_block_2_4],
    [label_block_3_1, label_block_3_2, label_block_3_3, label_block_3_4],
    [label_block_4_1, label_block_4_2, label_block_4_3, label_block_4_4],
]

# 각 숫자 블록이 위치하게 하는 절대좌표
xlist = [70, 210, 350, 490]
ylist = [322, 459, 596, 733]

# 라벨 배치
label_bg.place(x = 0, y = 0)
label_title.place(x = 73, y = 61)
label_scoreboard.place(x = 341, y = 60)
label_maxScoreboard.place(x = 478, y = 60)
label_score.place(x = 341, y = 133)
label_maxScore.place(x = 478, y = 133) # 137
label_guide.place(x = 73, y = 210)
label_gameboard.place(x = 55, y = 300)

# 반복문을 통해 배치한다
for ycor in ylist:
    for xcor in xlist:
        boardLabel[ycor][xcor].place(x = xcor, y = ycor)

# remote window setup
button_up = Button(remote, text = "↑", font = ("GameBold2048", 14), bg = "black", fg = "white", width = 3, height = 3, command = rotateUp) # 윗 버튼
button_down = Button(remote, text = "↓", font = ("GameBold2048", 14), bg = "black", fg = "white", width = 3, height = 3, command = rotateDown) # 아랫 버튼
button_left = Button(remote, text = "←", font = ("GameBold2048", 14), bg = "black", fg = "white", width = 8, height = 1, command = rotateLeft) # 왼쪽 버튼
button_right = Button(remote, text = "→", font = ("GameBold2048", 14), bg = "black", fg = "white", width = 8, height = 1, command = rotateRight) # 오른쪽 버튼
button_newGame = Button(remote, text = "New Game", font = ("GameBold2048", 22), width = 9, height = 1, bg = "#8f7a66", fg = "#f9f6f2", command = gameInit) # 새로운 게임을 시작하는 버튼

# 버튼 배치
button_up.place(x = 163, y = 47)
button_down.place(x = 163, y = 226)
button_left.place(x = 50, y = 163)
button_right.place(x = 220, y = 163)
button_newGame.place(x = 307, y = 310)

# 맨 처음 게임 초기화
gameInit()

# mainloop
tk.mainloop()
remote.mainloop()