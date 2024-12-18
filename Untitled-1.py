from tkinter import *
import turtle
import pygame
import tkinter as tk
from random import randint

def main():
 

    brick = Button(window, text='Brick Breaker', width=9,height=4, bd='5', command=Game)
    brick.place(x=100, y=152)
    but = Button(window, text='xoxo', width=9,height=4, bd='5', command= lambda: [window.withdraw(), xoxo()])
    but.place(x=415, y=152)
    
    window.mainloop()

def Game():
    window.withdraw()
    window1=Tk()
    window1.title('ping bomb')
    title = Label(window1, text="Game", bg="grey", font=("bold", 30))
    title.pack()
    btn = Button(window1, text='Quit', width=7,height=2, bd='10', command=window1.destroy)
    btn.place(x=295, y=525)
    btn1 = Button(window1, text='Go back', width=7,height=2, bd='10', command=lambda:[window1.withdraw(),window.deiconify()])
    btn1.place(x=220, y=525)

    window1.mainloop()


def xoxo():
    """xoxo with a twist, game ends when hit draw"""
    window.withdraw()
    global n, player1_name, player2_name, player1_score, player2_score, l 
    n=1
    player1_score = 0
    player2_score = 0
    player1_name = "Player 1"
    player2_name = "Player 2"
    window2 = Tk()
    window2.title('XOXO')
    window2.geometry('600x600')
    window2.config(bg='grey')
    btn = Button(window2, text='Leave', width=7,height=2, bd='10', command=window2.destroy)
    btn.place(x=305, y=530)
    btn1 = Button(window2, text='Go Back', width=7,height=2, bd='10', command=lambda:[window2.withdraw(), window.deiconify()])
    btn1.place(x=230, y=530)

    window2.mainloop()


window=Tk()
window.geometry('600x600')
window.configure(bg='#ffffff')
title = Label(window, text="Home", fg='red',bg="#ffffff" , font=("Comic Sans MS", 30, 'bold'))
title.pack()
can= Canvas(window, width=50, height=50, bg='#ffffff')
can.place(x=270, y=525)
btn = Button(window, text='Leave', width=7,height=2, bd='10', command=window.destroy)
btn.place(x=270, y=525)
can1= Canvas(window, width=85, height=80, bg='#ffffff')
can1.place(x=95, y=147)
brick = Button(window, text='Brick Breaker', width=9,height=4, bd='5', command=Game)
brick.place(x=100, y=152)
#ph1= Canvas(window, width=110, height=115, bg='#ffffff')
#ph1.place(x=80, y=230)
#photo1 = PhotoImage(file ="C:\\Users\\ElieH\\Desktop\\python\\Elie.png")
#item = ph1.create_image (60,60, image =photo1)

can2= Canvas(window, width=85, height=80, bg='#ffffff')
can2.place(x=412, y=147)
but = Button(window, text='xoxo', width=9,height=4, bd='5', command=xoxo)
but.place(x=415, y=152)
#ph2= Canvas(window, width=110, height=115, bg='#ffffff')
#ph2.place(x=395, y=230)
#photo2 = PhotoImage(file ="")
#item = ph2.create_image (60,60, image =photo2)

#ph3= Canvas(window, width=110, height=210, bg='#ffffff')
#ph3.place(x=250, y=230)
#photo3 = PhotoImage(file ="")
#item = ph3.create_image (60,110, image =photo3)


window.mainloop()
