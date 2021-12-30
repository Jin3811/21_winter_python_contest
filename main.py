# start : 2021.12.18
# end :
# made by Heo jin woo

from tkinter import *
from tkinter import font
from random import *

def whereis(event): 
    print(event.x, " ", event.y)

def is_GameOver():
    global board

def generateNumberBlock(): 
    temp = randint(1, 10)
    if temp < 10 : return 2
    else : return 4

def display():
    if (is_GameOver()):
        label_gameover.place(x = 0, y = 530)
    else :
        global board, boardLabel
        xlist = [66, 211, 356, 479]
        ylist = [357, 622, 765, 886]
        for y in range(4):
            for x in range(4):
                if board[y][x] == 0:
                    pass
                elif board[y][x] <= 2048:
                    boardLabel[y][x] = numBlockData[board[y][x]]
                else:
                    boardLabel[y][x] = numBlockData["super"]
                    boardLabel[y][x].config(text=str(board[y][x]))
                    
        for ycor in range(4):
            for xcor in range(4):
                if not board[ycor][xcor] == 0:
                    boardLabel[ycor][xcor].place(x = xlist[xcor], y = ylist[ycor])

def gameInit():
    global board, score, boardLabel
    i = 0
    score = 0
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    boardLabel = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    cnt = randint(1,2)
    
    while (i < cnt):
        x, y = randint(0, 3), randint(0, 3)
        
        if board[y][x] == 0 : # 중복방지
            board[y][x] = generateNumberBlock()
            i += 1
        else : # 중복된 블럭을 선택했다면 다시 한다.
            i -= 1
    label_gameover.place(x = 3000, y = 3000)
        
def rotateUp(event):
    pass

def rotateDown(event):
    pass

def rotateLeft(event):
    pass

def rotateRight(event):
    pass

def newGameStart():
    pass


board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
boardLabel = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
scoreMax = 0
score = 0
tk = Tk() # main window
remote = Tk() # remote window

# font/GameBold2048.ttf, need to download
# ("GameBold2048", 22)
gamefont = font.Font(family = "GameBold2048", size = 22)


numBlockData = {
    0 : Label(tk, width = 7, height = 3, bg = "#cdc1b4", ),
    2 : Label(tk, text = "2", font = gamefont, width = 7, height = 3, bg = "#eee4da", fg = "black"),
    4 : Label(tk, text = "4", font = gamefont, width = 7, height = 3, bg = "#ede0c8", fg = "black"),
    8 : Label(tk, text = "8", font = gamefont, width = 7, height = 3, bg = "#f2b179", fg = "#f9f6f2"),
    16 : Label(tk, text = "16", font = gamefont, width = 7, height = 3, bg = "#f59563", fg = "#f9f6f2"),
    32 : Label(tk, text = "32", font = gamefont, width = 7, height = 3, bg = "#f67c5f", fg = "#f9f6f2"),
    64 : Label(tk, text = "64", font = gamefont, width = 7, height = 3, bg = "#f65e3b", fg = "#f9f6f2"),
    128 : Label(tk, text = "128", font = gamefont, width = 7, height = 3, bg = "#edcf72", fg = "#f9f6f2"),
    256 : Label(tk, text = "256", font = gamefont, width = 7, height = 3, bg = "#edcc61", fg = "#f9f6f2"),
    512 : Label(tk, text = "512", font = gamefont, width = 7, height = 3, bg = "#edc850", fg = "#f9f6f2"),
    1024 : Label(tk, text = "1024", font = gamefont, width = 7, height = 3, bg = "#edc53f", fg = "#f9f6f2"),
    2048 : Label(tk, text = "2048", font = gamefont, width = 7, height = 3, bg = "#edc22e", fg = "#f9f6f2"),
    "super" : Label(tk, text = "super", font = gamefont, width = 7, height = 3, bg = "#3c3a32", fg = "#f9f6f2") # if (tile > 2048) == True
}

# window setup
tk.title("2048!")
remote.title("2048! remote")
tk.geometry("688x900+100+0")
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
label_gameover = Label(tk, text = "Game Over!!", font = gamefont, width = 40, height = 3)
label_guide = Label(tk, text = "please, download font,\nGameBold2048.ttf", font = ("GameBold2048", 16) , bg = "#f9f6f2", fg = "black")
label_gameboard = Label(tk, width = 71, height = 30, bg = "#bbada0")

label_bg.place(x = 0, y = 0)
label_title.place(x = 73, y = 61)
label_scoreboard.place(x = 341, y = 60)
label_maxScoreboard.place(x = 478, y = 60)
label_score.place(x = 341, y = 133)
label_maxScore.place(x = 478, y = 133) # 137
label_guide.place(x = 73, y = 210)
label_gameboard.place(x = 55, y = 300)
# label_gameover.place(x = 0, y = 530)

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
display()

tk.bind("<Button-1>", whereis)

# mainloop
tk.mainloop()
remote.mainloop()