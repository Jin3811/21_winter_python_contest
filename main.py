# start : 2021.12.18
# end : 2021.12.31
# made by Heo jin woo

from tkinter import *
from tkinter import font, messagebox
from random import randint

def gameover():
    messagebox.showinfo("2048!", "Gameover!")

def is_GameOver():
    global board
    for y in range(4):
        column = board[y][0]
        if column == 0:
            return False
        else :
            for x in range(1, 4):
                if board[y][x] == column or board[y][x] == 0:
                    return False
                else :
                    column = board[y][x]
    
    for x in range(4):
        row = board[0][x]
        if row == 0:
            return False
        for y in range(1, 4):
            if board[y][x] == row or board[y][x] == 0:
                return False
            else:
                row = board[y][x]
    
    return True

def generateNumberBlock(): 
    temp = randint(1, 10)
    if temp < 10 : return 2
    else : return 4

def display():
    global board, boardLabel, score, scoreMax
    
    for y in range(4):
        for x in range(4):
            if board[y][x] <= 2048:
                blockData = numBlockData[board[y][x]]
                boardLabel[y][x].config(text = blockData[0], bg = blockData[1], fg = blockData[2])
            else:
                blockData = numBlockData["super"]
                boardLabel[y][x].config(text=str(board[y][x]), bg = blockData[1], fg = blockData[2])
    
    if is_GameOver():
        if score > scoreMax:
            scoreMax = score
        gameover()
        
    print(board, "  ", is_GameOver())
    label_score.config(text = str(score))
    label_maxScore.config(text = str(scoreMax))
    

def gameInit():
    global board, score, boardLabel
    i = 0
    score = 0
        
    blockdata = numBlockData[0]
    for y in range(4):
        for x in range(4):
            board[y][x] = 0
            boardLabel[y][x].config(text = blockdata[0], bg = blockdata[1], fg = blockdata[2])
    
    cnt = randint(1,2)
    while i < cnt:
        x, y = randint(0, 3), randint(0, 3)
        
        if board[y][x] == 0 : # 중복방지
            board[y][x] = generateNumberBlock()
            i += 1
        else : # 중복된 블럭을 선택했다면 다시 한다.
            i -= 1
    display()

def rotate(n):
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
               
def rotateUp():
    moveBlock()
    display()

def rotateDown():
    rotate(2)
    moveBlock()
    rotate(2)

    display()
def rotateLeft():
    rotate(1)
    moveBlock()
    rotate(3)
    display()

def rotateRight():
    rotate(3)
    moveBlock()
    rotate(1)
    display()

board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
scoreMax = 0
score = 0
tk = Tk() # main window
remote = Tk() # remote window

# font/GameBold2048.ttf, need to download
# ("GameBold2048", 22)
gamefont = font.Font(family = "GameBold2048", size = 22)

numBlockData = {
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
tk.geometry("688x989+100+0")
remote.geometry("500x400+1000+350")
tk.resizable(False, False)
remote.resizable(False, False)

# tk window setup
label_bg = Label(tk, width = 100, height = 100, bg = "#f9f6f2")
label_title = Label(tk, text = "2048!", font = ("GameBold2048", 56), bg = "#f9f6f2", fg = "#8f7a66")
label_score = Label(tk, text = "0", font = gamefont, width = 7, height = 1, bg = "#bbada0", fg = "white")
label_scoreboard = Label(tk, text = "SCORE", font = gamefont, width = 7, height = 2, bg = "#bbada0", fg = "white")
label_maxScore = Label(tk, text = "0", font = gamefont, width = 7, height = 1, bg = "#bbada0", fg = "white")
label_maxScoreboard = Label(tk, text = "BEST", font = gamefont, width = 7, height = 2, bg = "#bbada0", fg = "white")
label_guide = Label(tk, text = "please, download font,\nGameBold2048.ttf", font = ("GameBold2048", 16) , bg = "#f9f6f2", fg = "black")
label_gameboard = Label(tk, width = 71, height = 30, bg = "#bbada0")
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

boardLabel = [
    [label_block_1_1, label_block_1_2, label_block_1_3, label_block_1_4],
    [label_block_2_1, label_block_2_2, label_block_2_3, label_block_2_4],
    [label_block_3_1, label_block_3_2, label_block_3_3, label_block_3_4],
    [label_block_4_1, label_block_4_2, label_block_4_3, label_block_4_4],
]

xlist = [70, 210, 350, 490]
ylist = [322, 459, 596, 733]

label_bg.place(x = 0, y = 0)
label_title.place(x = 73, y = 61)
label_scoreboard.place(x = 341, y = 60)
label_maxScoreboard.place(x = 478, y = 60)
label_score.place(x = 341, y = 133)
label_maxScore.place(x = 478, y = 133) # 137
label_guide.place(x = 73, y = 210)
label_gameboard.place(x = 55, y = 300)

for y in range(4):
    for x in range(4):
        boardLabel[y][x].place(x = xlist[x], y = ylist[y])

# remote window setup
button_up = Button(remote, text = "↑", font = ("GameBold2048", 14), bg = "black", fg = "white", width = 3, height = 3, command = rotateUp)
button_down = Button(remote, text = "↓", font = ("GameBold2048", 14), bg = "black", fg = "white", width = 3, height = 3, command = rotateDown)
button_left = Button(remote, text = "←", font = ("GameBold2048", 14), bg = "black", fg = "white", width = 8, height = 1, command = rotateLeft)
button_right = Button(remote, text = "→", font = ("GameBold2048", 14), bg = "black", fg = "white", width = 8, height = 1, command = rotateRight)
button_newGame = Button(remote, text = "New Game", font = ("GameBold2048", 22), width = 9, height = 1, bg = "#8f7a66", fg = "#f9f6f2", command = gameInit)

button_up.place(x = 163, y = 47)
button_down.place(x = 163, y = 226)
button_left.place(x = 50, y = 163)
button_right.place(x = 220, y = 163)
button_newGame.place(x = 307, y = 310)

gameInit()

# mainloop
tk.mainloop()
remote.mainloop()