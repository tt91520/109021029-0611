from tkinter import *

flag = True

def OOXX(num):
    global flag
    if num == 0:
        if flag:
            btn0.config(text="O", state=DISABLED)
        else:
            btn0.config(text="X", state=DISABLED)
    elif num == 1:
        if flag:
            btn1.config(text="O", state=DISABLED)
        else:
            btn1.config(text="X", state=DISABLED)
    elif num == 2:
        if flag:
            btn2.config(text="O", state=DISABLED)
        else:
            btn2.config(text="X", state=DISABLED)
    elif num == 3:
        if flag:
            btn3.config(text="O", state=DISABLED)
        else:
            btn3.config(text="X", state=DISABLED)
    elif num == 4:
        if flag:
            btn4.config(text="O", state=DISABLED)
        else:
            btn4.config(text="X", state=DISABLED)
    elif num == 5:
        if flag:
            btn5.config(text="O", state=DISABLED)
        else:
            btn5.config(text="X", state=DISABLED)
    elif num == 6:
        if flag:
            btn6.config(text="O", state=DISABLED)
        else:
            btn6.config(text="X", state=DISABLED)
    elif num == 7:
        if flag:
            btn7.config(text="O", state=DISABLED)
        else:
            btn7.config(text="X", state=DISABLED)
    elif num == 8:
        if flag:
            btn8.config(text="O", state=DISABLED)
        else:
            btn8.config(text="X", state=DISABLED)
    flag = not flag

    if btn0.cget('text') == btn1.cget('text') and btn0.cget('text') == btn2.cget('text') and btn0.cget('text') != "":
        if btn0.cget('text') == "O":
            print("player 1 win")
        else:
            print("player 2 win")
    elif btn3.cget('text') == btn4.cget('text') and btn3.cget('text') == btn5.cget('text') and btn3.cget('text') != "":
        if btn3.cget('text') == "O":
            print("player 1 win")
        else:
            print("player 2 win")
    elif btn6.cget('text') == btn7.cget('text') and btn6.cget('text') == btn8.cget('text') and btn6.cget('text') != "":
        if btn6.cget('text') == "O":
            print("player 1 win")
        else:
            print("player 2 win")
    elif btn0.cget('text') == btn3.cget('text') and btn0.cget('text') == btn6.cget('text') and btn0.cget('text') != "":
        if btn0.cget('text') == "O":
            print("player 1 win")
        else:
            print("player 2 win")
    elif btn1.cget('text') == btn4.cget('text') and btn1.cget('text') == btn7.cget('text') and btn1.cget('text') != "":
        if btn1.cget('text') == "O":
            print("player 1 win")
        else:
            print("player 2 win")
    elif btn2.cget('text') == btn5.cget('text') and btn2.cget('text') == btn8.cget('text') and btn2.cget('text') != "":
        if btn2.cget('text') == "O":
            print("player 1 win")
        else:
            print("player 2 win")
    elif btn0.cget('text') == btn4.cget('text') and btn0.cget('text') == btn8.cget('text') and btn0.cget('text') != "":
        if btn0.cget('text') == "O":
            print("player 1 win")
        else:
            print("player 2 win")
    elif btn2.cget('text') == btn4.cget('text') and btn2.cget('text') == btn6.cget('text') and btn2.cget('text') != "":
        if btn2.cget('text') == "O":
            print("player 1 win")
        else:
            print("player 2 win")


screen = Tk()
screen.geometry("400x400+200+100")
screen.title = "Button Test"
screen.rowconfigure(0, weight=1)
screen.rowconfigure(1, weight=1)
screen.rowconfigure(2, weight=1)
screen.columnconfigure(0, weight=1)
screen.columnconfigure(1, weight=1)
screen.columnconfigure(2, weight=1)

btn0 = Button(screen, text="", command=lambda:OOXX(0))
btn0.grid(row=0, column=0, sticky=NSEW)
btn1 = Button(screen, text="", command=lambda:OOXX(1))
btn1.grid(row=0, column=1, sticky=NSEW)
btn2 = Button(screen, text="", command=lambda:OOXX(2))
btn2.grid(row=0, column=2, sticky=NSEW)

btn3 = Button(screen, text="", command=lambda:OOXX(3))
btn3.grid(row=1, column=0, sticky=NSEW)
btn4 = Button(screen, text="", command=lambda:OOXX(4))
btn4.grid(row=1, column=1, sticky=NSEW)
btn5 = Button(screen, text="", command=lambda:OOXX(5))
btn5.grid(row=1, column=2, sticky=NSEW)

btn6 = Button(screen, text="", command=lambda:OOXX(6))
btn6.grid(row=2, column=0, sticky=NSEW)
btn7 = Button(screen, text="", command=lambda:OOXX(7))
btn7.grid(row=2, column=1, sticky=NSEW)
btn8 = Button(screen, text="", command=lambda:OOXX(8))
btn8.grid(row=2, column=2, sticky=NSEW)

screen.mainloop()