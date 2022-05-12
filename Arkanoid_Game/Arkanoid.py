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


