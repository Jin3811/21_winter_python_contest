# start : 2021.12.18
# end :
# made by Heo jin woo
# background picture source : https://github.com/gabrielecirulli/2048/tree/master/meta (2048 origin maker's source)

from tkinter import *
from random import *
import time



def whereis(event): # 
    print(event.x, " ", event.y)
    
WIDTH = 640 # interface width. treat as constant
HEIGHT = 920 # interface height. treat as constant
tk = Tk()
tk.title("2048!")
tk.geometry(str(WIDTH) + "x" + str(HEIGHT))

backgroundPicture = PhotoImage(file="picture\\bg.png")
test = PhotoImage(file="picture\\강아지.png")
bg = Label(tk, image = backgroundPicture, compound="bottom")

label2 = Label(tk, background="Yellow", image = test)

bg.place(x = 0, y = 0)
label2.place(x=64, y=331)

tk.bind("<Button-1>", whereis)
tk.mainloop()   