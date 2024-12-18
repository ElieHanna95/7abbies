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
