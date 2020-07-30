from tkinter import *
from pytube import YouTube

def download():
    YouTube(user_input.get()).streams.first().download()
    user_input.delete(0, END)

root = Tk()
user_input = Entry()
user_input.pack()
user_input.bind('<Return>', (lambda event: download())) 
user_input.focus()
root.mainloop()


