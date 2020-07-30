from tkinter import *
import time

WIDTH = 1300
HEIGHT = 700
SIZE = 100
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="grey")
canvas.pack()
color = 'yellow'


class Ball:
    def __init__(self, x, y):
        self.shape = canvas.create_oval(0, 0, SIZE, SIZE, fill=color)
        self.speedx = x # changed from 3 to 9
        self.speedy = y # changed from 3 to 9
        self.active = True
        self.move_active()

    def ball_update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

    def move_active(self):
        if self.active:
            self.ball_update()
            tk.after(40, self.move_active) # changed from 10ms to 30ms

w, h = tk.winfo_screenwidth(), tk.winfo_screenheight()
tk.overrideredirect(1)
tk.geometry("%dx%d+0+0" % (w, h))
ball = Ball(5,8)
ball2 = Ball(7,6)
tk.mainloop()
