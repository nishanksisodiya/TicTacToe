import tkinter as tk
import tkinter.messagebox as mb

win=tk.Tk()
bg=tk.Canvas(win, width=1920,height=1080,bg="#101010")
w=tk.Canvas(win, width=1920,height=1080,bg="#101010")
p=ord("X")
d={}

def onExitClk(event):
    win.quit()

def checkWin():
    print("\n")
    print(d)
    print("\n")
    if(d[1]==d[2]==d[3]):
        w.destroy()
        bg.create_text(960,540,text=chr(d[1])+" Wins",font=("moon", 100),fill="#88ff00")
    elif(d[4]==d[5]==d[6]):
        w.destroy()
        bg.create_text(960,540,text=chr(d[4])+" Wins",font=("moon", 100),fill="#88ff00")
    elif(d[7]==d[8]==d[9]):
        w.destroy()
        bg.create_text(960,540,text=chr(d[7])+" Wins",font=("moon", 100),fill="#88ff00")
    elif(d[7]==d[4]==d[1]):
        w.destroy()
        bg.create_text(960,540,text=chr(d[7])+" Wins",font=("moon", 100),fill="#88ff00")
    elif(d[8]==d[5]==d[2]):
        w.destroy()
        bg.create_text(960,540,text=chr(d[8])+" Wins",font=("moon", 100),fill="#88ff00")
    elif(d[9]==d[6]==d[3]):
        w.destroy()
        bg.create_text(960,540,text=chr(d[9])+" Wins",font=("moon", 100),fill="#88ff00")
    elif(d[7]==d[5]==d[3]):
        w.destroy()
        bg.create_text(960,540,text=chr(d[7])+" Wins",font=("moon", 100),fill="#88ff00")
    elif(d[9]==d[5]==d[1]):
        w.destroy()
        bg.create_text(960,540,text=chr(d[9])+" Wins",font=("moon", 100),fill="#88ff00")

def setNextMove():
    global p
    if(p==ord("X")):
        p=ord("O")
    elif(p==ord("O")):
        p=ord("X")
#Gameplay
def onClick(event):
    global p

    print("{},{}".format(event.x,event.y))
    x=event.x
    y=event.y
    print(p)
    #Upper Grid
    if x in range(800,901) and y in range(400,490):                                             #7th block
        if 7 not in d:
            w.create_text(850,445,text=chr(p),font=("moon bold", 30),fill="#88ff00")
            d[7]=p
            setNextMove()
    elif x in range(901,1020) and y in range(400,490):                                          #8th block
        if 8 not in d:
            w.create_text(960,445,text=chr(p),font=("moon bold", 30),fill="#88ff00")
            d[8]=p
            setNextMove()
    elif x in range(1021,1120) and y in range(400,490):                                         #9th block
        if 9 not in d:
            w.create_text(1070,445,text=chr(p),font=("moon bold", 30),fill="#88ff00")
            d[9]=p
            setNextMove()
    #Middle Grid
    elif x in range(800,901) and y in range(490,580):                                           #4th block
        if 4 not in d:
            w.create_text(850,535,text=chr(p),font=("moon bold", 30),fill="#88ff00")
            d[4]=p
            setNextMove()
    elif x in range(901,1020) and y in range(490,580):                                          #5th block
        if 5 not in d:
            w.create_text(960,535,text=chr(p),font=("moon bold", 30),fill="#88ff00")
            d[5]=p
            setNextMove()
    elif x in range(1021,1120) and y in range(490,580):                                         #6th block
        if 6 not in d:
            w.create_text(1070,535,text=chr(p),font=("moon bold", 30),fill="#88ff00")
            d[6]=p
            setNextMove()
    #Lower Grid
    elif x in range(800,901) and y in range(580,680):                                           #1st block
        if 1 not in d:
            w.create_text(850,630,text=chr(p),font=("moon bold", 30),fill="#88ff00")
            d[1]=p
            setNextMove()
    elif x in range(901,1020) and y in range(580,680):                                          #2nd block
        if 2 not in d:
            w.create_text(960,630,text=chr(p),font=("moon bold", 30),fill="#88ff00")
            d[2]=p
            setNextMove()
    elif x in range(1021,1120) and y in range(580,680):                                         #3rd block
        if 3 not in d:
            w.create_text(1070,630,text=chr(p),font=("moon bold", 30),fill="#88ff00")
            d[3]=p
            setNextMove()
    checkWin()

def menu():
    menu=tk.Menu(win)
    win.config(menu=menu)
    filemenu=tk.Menu(menu)
    helpmenu=tk.Menu(menu)
    menu.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="New Game")
    menu.add_cascade(label="Help",menu=helpmenu)
    helpmenu.add_command(label="About",command=callabt)
    helpmenu.add_command(label="Quit",command=win.quit)

def callabt():
    mb.showinfo("ABOUT","Version: 1.0.0\nDeveloped by Nishank Singh Sisodiya")


def ui():
    win.title("Tic Tac Toe 1.0.0")
    win.geometry("1920x1080")
    w.pack(fill='both', expand=True)
    bg.pack(fill='both', expand=True)
    w.create_text(960,100,text="TIC TAC TOE",font=("THE MAPLE ORIGINS", 100),fill="#88ff00")
    bg.create_text(960,100,text="TIC TAC TOE",font=("THE MAPLE ORIGINS", 100),fill="#88ff00")
    w.create_line(900,400,900,680,fill="#88ff00",width=5)
    w.create_line(1020,400,1020,680,fill="#88ff00",width=5)
    w.create_line(800,485,1120,485,fill="#88ff00",width=5)
    w.create_line(800,585,1120,585,fill="#88ff00",width=5)
    ExitBtn=w.create_rectangle(900,750,1020,780,fill="#88ff00",tags="exitbtn")
    ExitTxt=w.create_text(960,765,text="EXIT",font=("moon bold", 20),fill="#101010")
    ExitBtn1=bg.create_rectangle(900,750,1020,780,fill="#88ff00",tags="exitbtn")
    ExitTxt1=bg.create_text(960,765,text="EXIT",font=("moon bold", 20),fill="#101010")
    w.tag_bind(ExitBtn,  '<Button-1>', onExitClk)
    w.tag_bind(ExitTxt,  '<Button-1>', onExitClk)
    bg.tag_bind(ExitBtn1,  '<Button-1>', onExitClk)
    bg.tag_bind(ExitTxt1,  '<Button-1>', onExitClk)
    w.bind('<Button-1>', onClick)
    win.mainloop()
