# start : 2021.12.18
# end :
# made by Heo jin woo

from tkinter import *
from tkinter import font
from random import *

def whereis(event): 
    print(event.x, " ", event.y)
    
def test():
    label_test = Label(tk, text="444", bg = "black", fg="white", width=7, height=3, font=gamefont)
    label_test.place(x=66, y = 357)

def is_GameOver():
    global board

def generateNumberBlock(): 
    temp = randint(1, 10)
    if temp < 10 : return 2
    else : return 4

def display():
    global board, boardLabel
    xlist = [66, 211, 356, 479]
    ylist = [357, 622, 765, 886]
    for y in range(4):
        for x in range(4):
            if board[y][x] <= 2048:
                boardLabel[y][x] = numBlockData[board[y][x]]
            else:
                boardLabel[y][x] = boardLabel[y][x] = numBlockData["super"]
                boardLabel[y][x].config(text=str(board[y][x]))
                
    for ycor in range(4):
        for xcor in range(4):
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
    
    display()
        
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
gamefont = font.Font(family = "GameBold2048", size = 22)    

numBlockData = {
    0 : Label(tk, width = 7, height = 3, bg = "#cdc1b4", ),
    2 : Label(tk, text = "2", font = gamefont, width = 7, height = 3, bg = "#eee4da", fg = "#f9f6f2"),
    4 : Label(tk, text = "4", font = gamefont, width = 7, height = 3, bg = "#ede0c8", fg = "#f9f6f2"),
    8 : Label(tk, text = "8", font = gamefont, width = 7, height = 3, bg = "#f2b179", fg = "#f9f6f2"),
    16 : Label(tk, text = "16", font = gamefont, width = 7, height = 3, bg = "#f59563", fg = "#f9f6f2"),
    32 : Label(tk, text = "32", font = gamefont, width = 7, height = 3, bg = "#f67c5f", fg = "#f9f6f2"),
    64 : Label(tk, text = "64", font = gamefont, width = 7, height = 3, bg = "#f65e3b", fg = "#f9f6f2"),
    128 : Label(tk, text = "128", font = gamefont, width = 7, height = 3, bg = "#edcf72", fg = "#f9f6f2"),
    256 : Label(tk, text = "256", font = gamefont, width = 7, height = 3, bg = "#edcc61", fg = "#f9f6f2"),
    512 : Label(tk, text = "512", font = gamefont, width = 7, height = 3, bg = "#edc850", fg = "#f9f6f2"),
    1024 : Label(tk, text = "1024", font = gamefont, width = 7, height = 3, bg = "#edc53f", fg = "#f9f6f2"),
    2048 : Label(tk, text = "2048", font = gamefont, width = 7, height = 3, bg = "#edc22e", fg = "#f9f6f2"),
    "super" : Label(tk, text = "super", font = gamefont, width = 7, height = 3, bg = "#3c3a32", fg = "#f9f6f2") # (tile > 2048) == True
}


tk.title("2048!")
remote.title("2048! remote")
tk.geometry("688x989+100+0")
remote.geometry("500x400+1000+350")
tk.resizable(False, False)
remote.resizable(False, False)

backgroundPicture = PhotoImage(file = "picture\\bg.png")
bg = Label(tk, image = backgroundPicture)

# label2 = Label(tk, text="123", compound="center", width=114, height=114)
# label_test = Label(tk, text = "3", font = gamefont, width = 7, height = 3, bg = "yellow")

label_score = Label(tk, text = "0", font = gamefont, width = 5, height = 1, bg = "#bbada0", fg = "white")
label_maxScore = Label(tk, text = "0", font = gamefont, width = 5, height = 1, bg = "#bbada0", fg = "white")
label_gameover = Label(tk, text = "Game Over!!", width = 30, height = 9)
label_guide = Label(tk, text = "please, download font,\nGameBold2048.ttf", font = ("GameBold2048", 16) , bg = "#f9f6f2", fg = "black")

bg.place(x = 0, y = 0)
# label_test.place(x = 66, y = 357)
label_score.place(x = 401, y = 97)
label_maxScore.place(x = 538, y = 97) # 137
label_guide.place(x = 60, y = 232)

button_up = Button(remote, text = "↑", font = ("GameBold2048", 14), bg = "black", fg = "white", width = 3, height = 3)
button_down = Button(remote, text = "↓", font = ("GameBold2048", 14), bg = "black", fg = "white", width = 3, height = 3)
button_left = Button(remote, text = "←", font = ("GameBold2048", 14), bg = "black", fg = "white", width = 8, height = 1)
button_right = Button(remote, text = "→", font = ("GameBold2048", 14), bg = "black", fg = "white", width = 8, height = 1)
button_newGame = Button(remote, text = "New Game", font = ("GameBold2048", 22), width = 9, height = 1, bg = "#8f7a66", fg = "#f9f6f2", command = gameInit)

button_up.place(x = 163, y = 47)
button_down.place(x = 163, y = 226)
button_left.place(x = 50, y = 163)
button_right.place(x = 220, y = 163)
button_newGame.place(x = 307, y = 310)

# label_gameover.place(x=0, y=480)
# label_testest.place(x=0, y=0)

gameInit()

tk.bind("<Button-1>", whereis)

tk.mainloop()
remote.mainloop()