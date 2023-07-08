from tkinter import *
from time import strftime

myWindow = Tk()
myWindow.title('Clock')

def time():
    myTime = strftime('%H:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1000, time)

clock = Label(myWindow, font = ('arial', 45, 'bold'), background = 'light blue', foreground = 'black')
clock.pack(anchor = 'center')

time()

mainloop()