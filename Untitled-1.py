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
    window1.title('Ping Bomb')
    window1.geometry('700x650')
    window1.config(bg='#d8ccbe')
    title = Label(window1, text="Ping Bomb", bg="#d8ccbe", fg='black', font=("bold", 30))
    title.pack()
    btn = Button(window1, text='Leave', width=7,height=2, bd='10', command=window1.destroy)
    btn.place(x=350, y=590)
    btn1 = Button(window1, text='Go back', width=7,height=2, bd='10', command=lambda:[window1.withdraw(),window.deiconify()])
    btn1.place(x=270, y=590)

    class Object():
        def __init__(self, canvas, item):
            self.canvas = canvas
            self.item = item

        def get_coordinates(self):
            return self.canvas.coords(self.item)

        def move(self, x, y):
            self.canvas.move(self.item, x, y)

        def destroy(self):  # delete_component
            self.canvas.delete(self.item)


    class Ball(Object):
        def __init__(self, canvas, x, y):
            self.radius = 6
            self.direction = [1, -1]
            self.speed = 12 # add a but in game so we can cbricke the speed depending on the players pref
            item = canvas.create_oval(x-self.radius, y-self.radius,
                                    x+self.radius, y+self.radius,
                                    fill='Pink') #cbricke the color of the ball
            super(Ball, self).__init__(canvas, item)

        def collide(self, game_objects): 
            coords = self.get_coordinates()
            x = (coords[0] + coords[2]) * 0.5
            if len(game_objects) > 1:
                self.direction[1] *= -1
            elif len(game_objects) == 1:
                game_object = game_objects[0]
                coords = game_object.get_coordinates()
                if x > coords[2]:
                    self.direction[0] = 1
                elif x < coords[0]:
                    self.direction[0] = -1
                else:
                    self.direction[1] *= -1

            for game_object in game_objects:
                if isinstance(game_object, Brick):
                    game_object.hit()
                    return True
        
        def update(self):
            coords = self.get_coordinates()
            width = self.canvas.winfo_width()
            if coords[0] <= 0 or coords[2] >= width:
                self.direction[0] *= -1
            if coords[1] <= 0:
                self.direction[1] *= -1
            x = self.direction[0] * self.speed
            y = self.direction[1] * self.speed
            self.move(x, y)


    class Board(Object):
        def __init__(self, canvas, x, y):
            self.width = 150
            self.height = 10
            self.ball = None
            board = canvas.create_rectangle(x - self.width / 2,
                                            y - self.height / 2,
                                            x + self.width / 2,
                                            y + self.height / 2,
                                            fill='#FF6F00')
            super(Board, self).__init__(canvas, board)

        def move(self, offset):
            coords = self.get_coordinates()
            width = self.canvas.winfo_width()
            if coords[0] + offset >= 0 and coords[2] + offset <= width:
                super(Board, self).move(offset, 0)
                if self.ball is not None:
                    self.ball.move(offset, 0)

        def set_ball(self, ball):
            self.ball = ball


    class Brick(Object):
        BLOCKS = {1: '#F3D653', 2: '#1377BA', 3: '#606060'}

        def __init__(self, canvas, x, y, hits):
            self.width = 75
            self.height = 20
            self.hits = hits
            color = Brick.BLOCKS[hits]
            item = canvas.create_rectangle(x - self.width / 2,
                                        y - self.height / 2,
                                        x + self.width / 2,
                                        y + self.height / 2,
                                        fill=color,
                                        tags='brick')
            super(Brick, self).__init__(canvas, item)

        def hit(self):
            self.hits -= 1
            if self.hits == 0:
                self.destroy()
            else:
                self.canvas.itemconfig(self.item,
                                    fill=Brick.BLOCKS[self.hits])

    def update(self):
            coords = self.get_coordinates()
            width = self.canvas.winfo_width()
            if coords[0] <= 0 or coords[2] >= width:
                self.direction[0] *= -1
            if coords[1] <= 0:
                self.direction[1] *= -1
            x = self.direction[0] * self.speed
            y = self.direction[1] * self.speed
            self.move(x, y)


    class Board(Object):
        def __init__(self, canvas, x, y):
            self.width = 150
            self.height = 10
            self.ball = None
            board = canvas.create_rectangle(x - self.width / 2,
                                            y - self.height / 2,
                                            x + self.width / 2,
                                            y + self.height / 2,
                                            fill='#FF6F00')
            super(Board, self).__init__(canvas, board)

        def move(self, offset):
            coords = self.get_coordinates()
            width = self.canvas.winfo_width()
            if coords[0] + offset >= 0 and coords[2] + offset <= width:
                super(Board, self).move(offset, 0)
                if self.ball is not None:
                    self.ball.move(offset, 0)

        def set_ball(self, ball):
            self.ball = ball


    class Brick(Object):
        BLOCKS = {1: '#F3D653', 2: '#1377BA', 3: '#606060'}

        def __init__(self, canvas, x, y, hits):
            self.width = 75
            self.height = 20
            self.hits = hits
            color = Brick.BLOCKS[hits]
            item = canvas.create_rectangle(x - self.width / 2,
                                        y - self.height / 2,
                                        x + self.width / 2,
                                        y + self.height / 2,
                                        fill=color,
                                        tags='brick')
            super(Brick, self).__init__(canvas, item)

        def hit(self):
            self.hits -= 1
            if self.hits == 0:
                self.destroy()
            else:
                self.canvas.itemconfig(self.item,
                                    fill=Brick.BLOCKS[self.hits])
    
    class Game(tk.Frame):
        def __init__(self, master):
            super(Game, self).__init__(master)
            self.lives = 3
            self.score = 0
            self.width = 700
            self.height = 500
            self.canvas = tk.Canvas(self, bg='#000000',
                                    width=self.width,
                                    height=self.height,)
            self.canvas.pack()
            self.pack()

            self.items = {}
            self.ball = None
            self.Board = Board(self.canvas, self.width/2, 426)
            self.items[self.Board.item] = self.Board
            # making random bricks
            for x in range(15, self.width - 50, 75):
                self.add_brick(x + 37.5, 50,  randint(1, 3))
                self.add_brick(x + 37.5, 70, randint(1, 3))
                self.add_brick(x + 37.5, 90, randint(1, 3))

            self.lives_text = None
            self.score_text = None
            self.setup_game()
            self.canvas.focus_set()
            self.canvas.bind('<Left>',
                            lambda _: self.Board.move(-15))
            self.canvas.bind('<Right>',
                            lambda _: self.Board.move(15))
            self.update_score_text()

        def setup_game(self):
            self.add_ball()
            self.update_lives_text()
            self.text = self.draw_text(350, 250,
                                    'Press \'Space\' to Start Game', 25)
            self.canvas.bind('<space>', lambda _: self.start_game())

        def add_ball(self):
            if self.ball is not None:
                self.ball.destroy()
            Board_coords = self.Board.get_coordinates()
            x = (Board_coords[0] + Board_coords[2]) * 0.5
            self.ball = Ball(self.canvas, x, 310)
            self.Board.set_ball(self.ball)

        def add_brick(self, x, y, hits):
            brick = Brick(self.canvas, x, y, hits)
            self.items[brick.item] = brick

        def draw_text(self, x, y, text, size='40', color='white'):
            font = ('Helvetica', size)
            return self.canvas.create_text(x, y, text=text,
                                        font=font, fill=color)

        def update_lives_text(self):
            text = '❤ x % s' % self.lives
            if self.lives_text is None:
                self.lives_text = self.draw_text(665, 20, text, 16)
            else:
                self.canvas.itemconfig(self.lives_text, text=text)

        def update_score_text(self):
            scr = 'Score: % s' % self.score
            if self.score_text is None:
                self.score_text = self.draw_text(58, 20, scr, 16)
            else:
                self.canvas.itemconfig(self.score_text, text=scr)

        def start_game(self):
            self.canvas.unbind('<space>')
            self.canvas.delete(self.text)
            self.Board.ball = None
            self.game_loop()

        def game_loop(self):
            self.check_collisions()
            self.update_score_text()
            num_bricks = len(self.canvas.find_withtag('brick'))
            if num_bricks == 0:
                self.ball.speed = None
                self.draw_text(350, 250, 'Winner :)', color='green')
            elif self.ball.get_coordinates()[3] >= self.height:
                self.ball.speed = None
                self.lives -= 1
                if self.lives < 0:
                    self.draw_text(350, 250, 'Looser :(', color='red')
                else:
                    self.after(1000, self.setup_game)
            else:
                self.ball.update()
                self.after(50, self.game_loop)

        def check_collisions(self):
            ball_coords = self.ball.get_coordinates()
            items = self.canvas.find_overlapping(*ball_coords)
            objects = [self.items[x] for x in items if x in self.items]
            if self.ball.collide(objects):
                self.score += 10


    if __name__ == '__main__':
        game = Game(window1)
        game.mainloop()
    window1.mainloop()



def xoxo():
    window.withdraw()
    global franklin, window2, n, player1_name, player2_name, player1_score, player2_score, n, l 
    n=1
    window.withdraw()
    window2 = Tk()
    player1_score = 0
    player2_score = 0
    player1_name = "Player 1"
    player2_name = "Player 2"
    window2.title('XOXO')
    window2.geometry('600x600')
    window2.config(bg='#d8ccbe')
    canvas = Canvas(window2, width=600, height=350) 
    canvas.grid(row=0, columnspan=6, pady=20)
    franklin = turtle.RawTurtle(canvas)
    btn = Button(window2, text='Leave', width=7,height=2, bd='10', command=window2.destroy)
    btn.place(x=305, y=530)
    btn1 = Button(window2, text='Go Back', width=7,height=2, bd='10', command=lambda:[window2.withdraw(), window.deiconify()])
    btn1.place(x=230, y=530)
   
    scoreboard = Label(window2, text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}", font=("Arial", 16), bg="#d8ccbe", fg="black")
    scoreboard.place(x=195, y=390)
    
    player1 = Label(window2, text = "X :").place(x = 20,y = 575)
    player2 = Label(window2, text = "O :").place(x = 420,y = 575)
    e1 = Entry(window2)
    e1.place(x=70, y=575)
    e2 = Entry(window2)
    e2.place(x=470, y=575)
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    
    def full_reset():
        global window2, player1_name, player2_name, player1_score, player2_score, n, l, cane

        if window2:
            window2.destroy()
        xoxo()
    
    
    def add_full_reset_button():
        full_reset_button = Button(window2, text="Full Reset", width=9, height=1, command=full_reset, font=("Arial", 9), bg="red", fg="white")
        full_reset_button.place(x=268, y=478)  # Adjust placement as needed
    add_full_reset_button()

    def set_names():
        global player1_name, player2_name
        player1_name = e1.get() if e1.get() else "Player 1"
        player2_name = e2.get() if e2.get() else "Player 2"
        print(f"{player1_name} and {player2_name} set.")

    Button(window2, text="Set Names",width=9,height=1, command=set_names).place(x=268, y=505)

    def drawgrid():
        
        franklin.penup()
        franklin.goto(0,0)
        franklin.pendown()
        franklin.pensize(10)
        franklin.penup()
        franklin.goto(-150,-55)
        franklin.pendown()
        franklin.forward(300)
        franklin.penup()
        franklin.goto(-150,55)
        franklin.pendown()
        franklin.forward(300)
        franklin.penup()
        franklin.goto(-50,150)
        franklin.right(90)
        franklin.pendown()
        franklin.forward(300)
        franklin.penup()
        franklin.goto(50,150)
        franklin.pendown()
        franklin.forward(300)
    drawgrid()
    
    def winning_logo1():
        winner_label = Label(window2,text=f"{player1_name} WON THE GAME!", font=("Arial", 20),fg="green",bg="grey")
        winner_label.place(x=150, y=20)
    
    def winning_logo2():
        winner_label = Label(window2,text=f"{player2_name} WON THE GAME!", font=("Arial", 20),fg="green",bg="grey")
        winner_label.place(x=150, y=20)


    def drawx():
        global n
        franklin.pencolor("red")
        franklin.shape('turtle')
        franklin.pendown()
        for i in range(2):
            franklin.left(45)
            franklin.forward(30)
            franklin.backward(60)
            franklin.forward(30)
            franklin.left(45)
        franklin.setheading(-90)
        n=n+1
 
    def drawo():
        global n
        franklin.pencolor('blue')
        franklin.shape('turtle')       
        franklin.pendown()
        franklin.circle(25)
        franklin.setheading(-90)
        n=n+1
    
    def check_game_status():
        """Check the game status after each move."""
        global l, player1_name, player2_name, player1_score, player2_score
        if (
            l[0] == l[1] == l[2] == 1 or
            l[0] == l[3] == l[6] == 1 or
            l[0] == l[4] == l[8] == 1 or
            l[1] == l[4] == l[7] == 1 or
            l[2] == l[5] == l[8] == 1 or
            l[2] == l[4] == l[6] == 1 or
            l[3] == l[4] == l[5] == 1 or
            l[6] == l[7] == l[8] == 1 or
            l[0] == l[1] == l[2] == 2 or
            l[0] == l[3] == l[6] == 2 or
            l[0] == l[4] == l[8] == 2 or
            l[1] == l[4] == l[7] == 2 or
            l[2] == l[5] == l[8] == 2 or
            l[2] == l[4] == l[6] == 2 or
            l[3] == l[4] == l[5] == 2 or
            l[6] == l[7] == l[8] == 2
            ):
        
            return

        elif all(cell != 0 for cell in l):
            draw_label = Label(window2, text="It's a Draw!", font=("Arial", 20), fg="Pink", bg="grey")
            draw_label.place(x=220, y=20)
            print("Draw!")
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=250, y=450)


    window2.mainloop()


window=Tk()
window.geometry('600x600')
window.configure(bg='#d8ccbe')
title = Label(window, text="Home", fg='red',bg="#d8ccbe" , font=("Comic Sans MS", 30, 'bold'))
title.pack()
btn = Button(window, text='Leave', width=7,height=2, bd='10', command=window.destroy)
btn.place(x=270, y=525)
brick = Button(window, text='Brick Breaker', width=9,height=4, bd='5', command=Game)
brick.place(x=100, y=152)
ph1= Canvas(window, width=115, height=115,bd=0.5, highlightthickness=0.5, bg='#d8ccbe')
ph1.place(x=80, y=230)
photo1 = PhotoImage(file ="C:\\Users\\ElieH\\Desktop\\python\\brick.png")
item = ph1.create_image (60,60, image =photo1)

but = Button(window, text='TIc-Tac-Toe', width=9,height=2, bd='5', command=xoxo)
but.place(x=415, y=156)
ph2= Canvas(window, width=110, height=115,bd=0, highlightthickness=0, bg='#d8ccbe')
ph2.place(x=395, y=230)
photo2 = PhotoImage(file ="C:\\Users\\ElieH\\Desktop\\python\\1-0d91dba3.png")
item = ph2.create_image (60,60, image =photo2)
window.mainloop()
