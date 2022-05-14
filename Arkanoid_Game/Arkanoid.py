from tkinter import *
import time
import random
# Create game window

tk = Tk()
tk.title('Game')
tk.resizable(0,0) # size window
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk,width=500, height=400,highlightthickness=0)
canvas.pack()
tk.update()

# Window is done, right now need create game object end traine my OOP skills =)

class Ball:
    def __init__(self,canvas,paddle,score,color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10,10,25,25, fill=color) # create ball give size and color
        self.canvas.move(self.id,245,100)# give coordinate from ball
        starts = [-2,-1,1,2]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        # create function from hit ball at platform
        def hit_paddle(self,pos):
            paddle_pos = self.canvas.coords(self.paddle.id)
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                    self.score.hit() # Thats is counter points if as ball is hit platform count +1
                    return True
            return False # if not hit - False
        # create function from draw as ball at game windows
        def draw(self):
            self.canvas.move(self.id,self.x,self.y)
            pos = self.canvas.coords(self.id)
            if pos[1] <= 0:
                self.y = 2
            if pos[3] >= self.canvas_height:
                self.hit_bottom = True
                # massage if players lose
                canvas.create_text(250,120,text = 'Game Over =(',font = ('Courier', 30),fill = 'red')
            if self.hit_paddle(pos) == True:
                self.y = -2
            if pos[0] <= 0:
                self.x = 2
            if pos [2] >= self.canvas_width:
                self.x = -2
# create object platform
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill = color)
        start_1 = [40,60,90,120,150,180,200]
        random.shuffle(start_1)
        self.starting_point_x = start_1[0]
        self.canvas.move(self.id,self.starting_point_x,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        # control setings platform
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        #if game is not starting, just wait
        self.started = False
        # if player press star, game will started
        self.canvas.bind_all('<KeyPress-Return>',self.start_game)
    def turn_right(self,event):
        self.x = 2
    def turn_left(self,event):
        self.x = -2
    def start_game(self,event):
        self.started = True
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        # if platforn in end window, we need stop platform
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
# create object Score



