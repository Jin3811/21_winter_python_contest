# start : 2021.12.18
# end :
# made by Heo jin woo
# background picture source : https://github.com/gabrielecirulli/2048/tree/master/meta (2048 origin maker's source)

from tkinter import *
from random import *
import time

def whereis(event):
    print(event.x, " ", event.y)
    
WIDTH = 688 # interface width. treat as constant
HEIGHT = 989 # interface height. treat as constant  
tk = Tk()
tk.title("2048!")
tk.geometry(str(WIDTH) + "x" + str(HEIGHT))

backgroundPicture = PhotoImage(file="picture\\bg.png")
bg = Label(tk, image = backgroundPicture, compound="bottom")

# label2 = Label(tk, text="123", compound="center", width=114, height=114)
label_test = Label(tk, text="123", font=("", 22), width=7, height=4, bg="yellow")

label_score = Label(tk, text = "0", font=("", 20), width = 7, height=2, bg="#bbada0", fg="white")
label_maxScore = Label(tk, text = "0", font=("", 20), width = 7, height=2, bg="#bbada0", fg="white")

bg.place(x = 0, y = 0)
label_test.place(x=66, y=357)
label_score.place(x=388, y=93)
label_maxScore.place(x=525, y=93) # 137

tk.bind("<Button-1>", whereis)
tk.mainloop()   