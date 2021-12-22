# start : 2021.12.18
# end :
# made by Heo jin woo
# background picture source : https://github.com/gabrielecirulli/2048/tree/master/meta (2048 origin maker's source)

from tkinter import *
from tkinter import font
from random import *
from tkinter.font import Font

def whereis(event): 
    print(event.x, " ", event.y)

board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
scoreMax = 0
score = 0

def is_GameOver():
    global board

def generateNumberBlock():
    temp = randint(1, 10)
    if temp < 10 : return 2
    else : return 4

def gameInit():
    global board, score
    score = 0
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    cnt = randint(1,2)
    for i in range(cnt):
        x, y = randint(0, 3), randint(0, 3)
        
        if board[y][x] == 0 : board[y][x] = generateNumberBlock()
        else : i -= 1
        
def rotateUp(event):
    pass

def rotateDown(event):
    pass

def rotateLeft(event):
    pass

def rotateRight(event):
    pass



WIDTH = 688 # interface width. treat as constant
HEIGHT = 989 # interface height. treat as constant  


tk = Tk() # main window
# remote = Tk() # remote rotate
tk.title("2048!")
# remote.title("2048! remote")
tk.geometry(str(WIDTH) + "x" + str(HEIGHT) + "+100+0")
# remote.geometry("200x200+800+350")
tk.resizable(False, False)
# remote.resizable(False, False)
gamefont = font.Font(family = "GameBold2048", size = 22)

backgroundPicture = PhotoImage(file="picture\\bg.png")
bg = Label(tk, image = backgroundPicture, compound="bottom")

# label2 = Label(tk, text="123", compound="center", width=114, height=114)
label_test = Label(tk, text="3", font=gamefont, width=7, height=3, bg="yellow")

label_score = Label(tk, text = "0", font = gamefont, width = 5, height=1, bg="#bbada0", fg="white")
label_maxScore = Label(tk, text = "0", font = gamefont, width = 5, height=1, bg="#bbada0", fg="white")
label_gameover = Label(tk, text="Game Over!!", width=30, height=9)

# label_testest = Label(tk, width=5, height=5, text="12344", bg="black", fg="white")

bg.place(x = 0, y = 0)
label_test.place(x=66, y=357)
label_score.place(x=401, y=97)
label_maxScore.place(x=538, y=97) # 137
# label_gameover.place(x=0, y=480)
# label_testest.place(x=0, y=0)

tk.bind("<Button-1>", whereis)

tk.mainloop()
# remote.mainloop()