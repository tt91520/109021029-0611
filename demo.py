from tkinter import *

def chageText(num):
    if int(lab['text']) != 0:
        lab['text'] = lab['text'] + num
    else:
        lab['text'] = num

def clean():
    lab.config(text = '0')

screen = Tk()
screen.title("Digital Keyboard")
screen.geometry("400x500+200+100")
screen.rowconfigure(1, weight=1)
screen.rowconfigure(2, weight=1)
screen.rowconfigure(3, weight=1)
screen.rowconfigure(4, weight=1)
screen.rowconfigure(5, weight=1)
screen.columnconfigure(0, weight=1)
screen.columnconfigure(1, weight=1)
screen.columnconfigure(2, weight=1)
screen.columnconfigure(3, weight=1)

lab = Label(screen, text="0", justify=RIGHT, anchor=E, font=("GungsuhCheI", 50, 'bold'), background="#ffddcc")
lab.grid(row=0, column=0, columnspan=4, sticky=EW)

btn7 = Button(screen, text="7", font=("GungsuhCheI", 25, 'bold'), command=lambda:chageText('7'))
btn7.grid(row=1, column=0, sticky=NSEW)
btn8 = Button(screen, text="8", font=("GungsuhCheI", 25, 'bold'), command=lambda:chageText('8'))
btn8.grid(row=1, column=1, sticky=NSEW)
btn9 = Button(screen, text="9", font=("GungsuhCheI", 25, 'bold'), command=lambda:chageText('9'))
btn9.grid(row=1, column=2, sticky=NSEW)

btn4 = Button(screen, text="4", font=("GungsuhCheI", 25, 'bold'), command=lambda:chageText('4'))
btn4.grid(row=2, column=0, sticky=NSEW)
btn5 = Button(screen, text="5", font=("GungsuhCheI", 25, 'bold'), command=lambda:chageText('5'))
btn5.grid(row=2, column=1, sticky=NSEW)
btn6 = Button(screen, text="6", font=("GungsuhCheI", 25, 'bold'), command=lambda:chageText('6'))
btn6.grid(row=2, column=2, sticky=NSEW)

btn1 = Button(screen, text="1", font=("GungsuhCheI", 25, 'bold'), command=lambda:chageText('1'))
btn1.grid(row=3, column=0, sticky=NSEW)
btn2 = Button(screen, text="2", font=("GungsuhCheI", 25, 'bold'), command=lambda:chageText('2'))
btn2.grid(row=3, column=1, sticky=NSEW)
btn3 = Button(screen, text="3", font=("GungsuhCheI", 25, 'bold'), command=lambda:chageText('3'))
btn3.grid(row=3, column=2, sticky=NSEW)

btn0 = Button(screen, text="0", font=("GungsuhCheI", 25, 'bold'), command=lambda:chageText('0'))
btn0.grid(row=4, column=0, sticky=NSEW)
btnExit = Button(screen, text="EXIT", font=("GungsuhCheI", 10, 'bold'), command=screen.destroy)
btnExit.grid(row=4, column=2, sticky=NSEW)
btnpoint = Button(screen, text=".", font=("GungsuhCheI", 25, 'bold'), command=lambda:chageText('.'))
btnpoint.grid(row=4, column=1, sticky=NSEW)

btnd = Button(screen, text="C", font=("GungsuhCheI", 25, 'bold'), command=clean)
btnd.grid(row=1, column=3, sticky=NSEW)
btna = Button(screen, text="+", font=("GungsuhCheI", 25, 'bold'))
btna.grid(row=2, column=3, sticky=NSEW)
btnb = Button(screen, text="-", font=("GungsuhCheI", 25, 'bold'))
btnb.grid(row=3, column=3, sticky=NSEW)
btnc = Button(screen, text="=", font=("GungsuhCheI", 25, 'bold'))
btnc.grid(row=4, column=3, sticky=NSEW)

screen.mainloop()