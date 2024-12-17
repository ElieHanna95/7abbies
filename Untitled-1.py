from tkinter import *
import turtle
import tkinter as tk
from random import randint

def main():

    fen = Tk()
    fen.geometry('600x600')
    fen.configure(bg='#ffffff')
    title = Label(fen, text="Home", bg="#ffffff", fg='red', font=("Comic Sans MS", 30, 'bold'))
    title.pack()
    can= Canvas(fen, width=50, height=50, bg='#ffffff')
    can.place(x=270, y=525)
    btn = Button(fen, text='Quit', width=7,height=2, bd='10', command=fen.destroy)
    btn.place(x=270, y=525)
   
    can1= Canvas(fen, width=85, height=80, bg='#ffffff')
    can1.place(x=95, y=147)
    hang = Button(fen, text='Brick Breaker', width=9,height=4, bd='5', command=Game)
    hang.place(x=100, y=152)
    ph1= Canvas(fen, width=110, height=115, bg='#ffffff')
    ph1.place(x=80, y=230)
    photo1 = PhotoImage(file ="")
    item = ph1.create_image (60,60, image =photo1)

    can2= Canvas(fen, width=85, height=80, bg='#ffffff')
    can2.place(x=412, y=147)
    but = Button(fen, text='xoxo', width=9,height=4, bd='5', command= lambda: [fen.withdraw(), xoxo()])
    but.place(x=415, y=152)
    ph2= Canvas(fen, width=110, height=115, bg='#ffffff')
    ph2.place(x=395, y=230)
    photo2 = PhotoImage(file ="")
    item = ph2.create_image (60,60, image =photo2)

    ph3= Canvas(fen, width=110, height=210, bg='#ffffff')
    ph3.place(x=250, y=230)
    photo3 = PhotoImage(file ="")
    item = ph3.create_image (60,110, image =photo3)
    fen.mainloop()

def Game():
    fen.withdraw()
    fen1=Tk()
    title = Label(fen1, text="Game", bg="grey", font=("bold", 30))
    title.pack()
    btn = Button(fen1, text='Quit', width=7,height=2, bd='10', command=fen1.destroy)
    btn.place(x=295, y=525)
    btn1 = Button(fen1, text='Go back', width=7,height=2, bd='10', command=lambda:[fen1.withdraw(),fen.deiconify()])
    btn1.place(x=220, y=525)

    fen1.mainloop()


