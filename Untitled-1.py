from tkinter import *
import turtle
import pygame
import tkinter as tk
from random import randint

pygame.mixer.init()
is_muted = False
def play_sound():
    pygame.mixer.music.load("soundtrack.mp3")  
    pygame.mixer.music.play(-1)

def toggle_mute():
    global is_muted
    if is_muted:
        pygame.mixer.music.set_volume(1.0)  
        mute_button.config(text="Mute")
    else:
        pygame.mixer.music.set_volume(0.0)  
        mute_button.config(text="Unmute")
    is_muted = not is_muted


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

        def destroy(self):  
            self.canvas.delete(self.item)


    class Ball(Object):
        def __init__(self, canvas, x, y):
            self.radius = 6
            self.direction = [1, -1]
            self.speed = 12 
            item = canvas.create_oval(x-self.radius, y-self.radius,
                                    x+self.radius, y+self.radius,
                                    fill='Pink') 
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
        BLOCKS = {1: '#ffff00', 2: '#ff5c33', 3: '#0000ff'}

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
        full_reset_button.place(x=268, y=478) 
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
            continue_button.place(x=268, y=450)

    def win1(): 
        global player1_score, player2_score, player1_name, player1_score, franklin, continue_button, l, n
        if l[0]==l[1]==l[2]==1:
            player1_score += 1  
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(-150,100)
            franklin.left(90)
            franklin.pendown()
            franklin.forward(300)
            winning_logo1()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9
        elif l[0]==l[1]==l[2]==2:
            player2_score += 1  
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(-150,100)
            franklin.left(90)
            franklin.pendown()
            franklin.forward(300)
            winning_logo2()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9
    def win2(): 
        global player1_score, player2_score, player1_name, player1_score, franklin, continue_button, l, n
        if l[1]== l[4]==l[7]==1:
            player1_score += 1  
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(0,150)
            franklin.pendown()
            franklin.forward(300)
            winning_logo1()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9
        elif l[1]== l[4]==l[7]==2:
            player2_score += 1  
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(0,150)
            franklin.pendown()
            franklin.forward(300)
            winning_logo2()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9
    def win3(): 
        global player1_score, player2_score, player1_name, player1_score, franklin, continue_button, l, n
        if l[0]== l[3]==l[6]==1:
            player1_score += 1  
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(-100,150)
            franklin.pendown()
            franklin.forward(300)
            winning_logo1()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9

        elif l[0]== l[3]==l[6]==2:
            player2_score += 1 
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(-100,150)
            franklin.pendown()
            franklin.forward(300)
            winning_logo2()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9
    def win4(): 
        global player1_score, player2_score, player1_name, player1_score, franklin, continue_button, l, n
        if l[0]== l[4]==l[8]==1:
            player1_score += 1 
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(-150,150)
            franklin.left(45)
            franklin.pendown()
            franklin.forward(425)
            winning_logo1()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9

        elif l[0]== l[4]==l[8]==2:
            player2_score += 1  
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(-150,150)
            franklin.left(45)
            franklin.pendown()
            franklin.forward(425)
            winning_logo2()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9
    def win5(): 
        global player1_score, player2_score, player1_name, player1_score, franklin, continue_button, l, n
        if l[2]== l[5]==l[8]==1:
            player1_score += 1  
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(100,150)
            franklin.pendown()
            franklin.forward(300)
            winning_logo1()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9

        elif l[2]== l[5]==l[8]==2:
            player2_score += 1 
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(100,150)
            franklin.pendown()
            franklin.forward(300)
            winning_logo2()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9
    def win6(): 
        global player1_score, player2_score, player1_name, player1_score, franklin, continue_button, l, n
        if l[2]== l[4]==l[6]==1:
            player1_score += 1  
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(150,150)
            franklin.right(45)
            franklin.pendown()
            franklin.forward(425)
            winning_logo1()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9

        elif l[2]== l[4]==l[6]==2:
            player2_score += 1  
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(150,150)
            franklin.right(45)
            franklin.pendown()
            franklin.forward(425)
            winning_logo2()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9
    def win7(): 
        global player1_score, player2_score, player1_name, player1_score, franklin, continue_button, l, n
        if l[3]== l[4]==l[5]==1:
            player1_score += 1  
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(-150,0)
            franklin.left(90)
            franklin.pendown()
            franklin.forward(300)
            winning_logo1()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9

        elif l[3]== l[4]==l[5]==2:
            player2_score += 1  
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(-150,0)
            franklin.left(90)
            franklin.pendown()
            franklin.forward(300)
            winning_logo2()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9
    def win8(): 
        global player1_score, player2_score, player1_name, player1_score, franklin, continue_button, l, n
        if l[6]== l[7]==l[8]==1:
            player1_score += 1  
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(-150,-100)
            franklin.left(90)
            franklin.pendown()
            franklin.forward(300)
            winning_logo1()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9

        elif l[6]== l[7]==l[8]==2:
            player2_score += 1  
            scoreboard.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")
            franklin.pencolor('black')
            franklin.pensize(5)
            franklin.penup()
            franklin.goto(-150,-100)
            franklin.left(90)
            franklin.pendown()
            franklin.forward(300)
            winning_logo2()
            continue_button = Button(window2, text="Continue Game",width=12,height=1, command=reset_game, font=("Arial", 9))
            continue_button.place(x=268, y=450)
            l = [0] * 9
    def x1():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(-100, 100)
        drawx()
        l[0]=1
        caneplace()
        if n>=5:
            win1()
            win3()
            win4()         
    def x2():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(0, 100)
        drawx()
        l[1]=1
        caneplace()
        if n>=5:
            win1()
            win2()        
    def x3():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(100, 100)
        drawx()
        l[2]=1
        caneplace()
        if n>=5:
            win1()   
            win5()
            win6()    
    def x4():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(-100, 0)
        drawx()
        l[3]=1
        caneplace()
        if n>=5:
            win7()    
            win3()
    def x5():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l  
        franklin.penup()
        franklin.goto(0, 0)
        drawx()
        l[4]=1
        caneplace()
        if n>=5:
            win7()
            win2()
            win4()
            win6()              
    def x6():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(100, 0)
        drawx()
        l[5]=1
        caneplace()
        if n>=5:
            win7()           
            win5()
    def x7():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(-100, -100)
        drawx()
        l[6]=1
        caneplace()
        if n>=5:
            win8()    
            win3()  
            win6()
    def x8():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(0, -100)
        drawx()
        l[7]=1
        caneplace()
        if n>=5:
            win8()            
            win2()
    def x9():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(100, -100)
        drawx()
        l[8]=1
        caneplace()
        if n>=5:
            win8()    
            win5()
            win4()
                              
    def o1():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(-120,100)
        drawo()
        caneplace()
        l[0]=2
        
        if n>=5:
            win1()
            win3()
            win4()
    def o2():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(-20,100)
        drawo()
        caneplace()
        l[1]=2
        if n>=5:
            win1()
            win2()
    def o3():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(80,100)
        drawo()
        caneplace()
        l[2]=2
        if n>=5:
            win1()
            win5()
            win6()
    def o4():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(-120,0)
        drawo()
        caneplace()
        l[3]=2
        if n>=5:
            win7()
            win3()
    def o5():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(-20,0)
        drawo()
        caneplace()
        l[4]=2
        if n>=5:
            win7()
            win5()
            win4()
            win6()
    def o6():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(80,0)
        drawo()
        caneplace()
        l[5]=2

        if n>=5:
            win7()
            win5()
    def o7():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(-120,-100)
        drawo()
        caneplace()
        l[6]=2
        if n>=5:
            win8()
            win3()
            win6()
    def o8():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(-20,-100)
        drawo()
        caneplace()
        l[7]=2
        if n>=5:
            win8()
            win2()
    def o9():
        global window2, n, player1_name, player2_name, player1_score, player2_score, continue_button, l
        franklin.penup()
        franklin.goto(80,-100)
        drawo()
        caneplace()
        l[8]=2
        if n>=5:
            win8()
            win5()
            win4()

    def setupbuttons():
        butx1 = Button(window2, text='x', width=6,height=3, bd='2',  command=lambda:[x1(),butx1.destroy(),buto1.destroy(), check_game_status()])
        butx1.place(x=30, y=400)
        butx2 = Button(window2, text='x', width=6,height=3, bd='2', command=lambda:[x2(),butx2.destroy(),buto2.destroy(), check_game_status()])
        butx2.place(x=80, y=400)
        butx3 = Button(window2, text='x', width=6,height=3, bd='2', command=lambda:[x3(),butx3.destroy(),buto3.destroy(), check_game_status()])
        butx3.place(x=128, y=400)

        butx4 = Button(window2, text='x', width=6,height=3, bd='2', command=lambda:[x4(),butx4.destroy(),buto4.destroy(), check_game_status()])
        butx4.place(x=30, y=450)
        butx5 = Button(window2, text='x', width=6,height=3, bd='2', command=lambda:[x5(),butx5.destroy(),buto5.destroy(), check_game_status()])
        butx5.place(x=80, y=450)
        butx6 = Button(window2, text='x', width=6,height=3, bd='2', command=lambda:[x6(),butx6.destroy(),buto6.destroy(), check_game_status()])
        butx6.place(x=128, y=450)

        butx7 = Button(window2, text='x', width=6,height=3, bd='2', command=lambda:[x7(),butx7.destroy(),buto7.destroy(), check_game_status()])
        butx7.place(x=30, y=500)
        butx8 = Button(window2, text='x', width=6,height=3, bd='2', command=lambda:[x8(),butx8.destroy(),buto8.destroy(), check_game_status()])
        butx8.place(x=80, y=500)
        butx9 = Button(window2, text='x', width=6,height=3, bd='2', command=lambda:[x9(),butx9.destroy(),buto9.destroy(), check_game_status()])
        butx9.place(x=128, y=500)

        buto1 = Button(window2, text='o', width=6,height=3, bd='2', command= lambda:[o1(), buto1.destroy(),butx1.destroy(), check_game_status()])
        buto1.place(x=430, y=400)
        buto2 = Button(window2, text='o', width=6,height=3, bd='2', command= lambda:[o2(), buto2.destroy(),butx2.destroy(), check_game_status()])
        buto2.place(x=480, y=400)
        buto3 = Button(window2, text='o', width=6,height=3, bd='2', command= lambda:[o3(), buto3.destroy(),butx3.destroy(), check_game_status()])
        buto3.place(x=530, y=400)

        buto4 = Button(window2, text='o', width=6,height=3, bd='2', command= lambda:[o4(), buto4.destroy(),butx4.destroy(), check_game_status()])
        buto4.place(x=430, y=450)
        buto5 = Button(window2, text='o', width=6,height=3, bd='2', command= lambda:[o5(), buto5.destroy(),butx5.destroy(), check_game_status()])
        buto5.place(x=480, y=450)
        buto6 = Button(window2, text='o', width=6,height=3, bd='2', command= lambda:[o6(), buto6.destroy(),butx6.destroy(), check_game_status()])
        buto6.place(x=530, y=450)

        buto7 = Button(window2, text='o', width=6,height=3, bd='2', command= lambda:[o7(), buto7.destroy(),butx7.destroy(), check_game_status()])
        buto7.place(x=430, y=500)
        buto8 = Button(window2, text='o', width=6,height=3, bd='2', command= lambda:[o8(), buto8.destroy(),butx8.destroy(), check_game_status()])
        buto8.place(x=480, y=500)
        buto9 = Button(window2, text='o', width=6,height=3, bd='2', command= lambda:[o9(), buto9.destroy(),butx9.destroy(), check_game_status()])
        buto9.place(x=530, y=500)

    setupbuttons()
    
    def caneplace():
        global n
        if n%2==0:
            cane.place(x=30, y=400)
        else:
            cane.place(x=430, y=400)

    cane= Canvas(window2, width=150, height=160, bg='#d8ccbe', highlightthickness=5, highlightbackground='#d8ccbe', highlightcolor='#d8ccbe')
    caneplace()
          


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
sound = Button(window, text='Play Sound', width=9,height=2, bd='5', command=lambda:[sound.destroy(),play_sound()])
sound.place(x=268, y=477)
mute_button = Button(window,text="Mute", command=toggle_mute)
mute_button.place(x=550, y=10)
ph1= Canvas(window, width=115, height=115,bd=0.5, highlightthickness=0.5, bg='#d8ccbe')
ph1.place(x=80, y=230)
photo1 = PhotoImage(file ="brick.png")
item = ph1.create_image (60,60, image =photo1)

but = Button(window, text='TIc-Tac-Toe', width=9,height=2, bd='5', command=xoxo)
but.place(x=415, y=156)
ph2= Canvas(window, width=110, height=115,bd=0, highlightthickness=0, bg='#d8ccbe')
ph2.place(x=395, y=230)
photo2 = PhotoImage(file ="xoxo.png")
item = ph2.create_image (60,60, image =photo2)
window.mainloop()
