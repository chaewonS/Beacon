
# -*- coding: utf-8 -*-
import Tkinter

global x
global y
x=1
y=1
global a
def showposition():
    global a
    canvas.delete(a)
    global x
    global y
    x=x+1
    y=y+1
    a = canvas.create_rectangle(SP_w +(x-1)*column, SP_h+(y-1)*row, SP_w+x*column,SP_h+y*row,fill="yellow")
    canvas.after(1000,showposition)
    
master = Tkinter.Tk()
width = 1080
height = 650
#label = Label(master, text="placeholder").pack()
canvas = Tkinter.Canvas(master, width=width, height=height)

rectanglesize = 8
SP_w = 215 #1080-650/2
SP_h = 10 #StartPoint
polygon = canvas.create_rectangle(SP_w,SP_h, width-SP_w,height-SP_h)

row = int((height-SP_h -SP_h)/rectanglesize) # 행 간격
x1 = canvas.create_line(SP_w, SP_h+row*1, width-SP_w, SP_h+row*1, fill="red")
x2 = canvas.create_line(SP_w, SP_h+row*2, width-SP_w, SP_h+row*2)
x3 = canvas.create_line(SP_w, SP_h+row*3, width-SP_w, SP_h+row*3)
x4 = canvas.create_line(SP_w, SP_h+row*4, width-SP_w, SP_h+row*4)
x5 = canvas.create_line(SP_w, SP_h+row*5, width-SP_w, SP_h+row*5)
x6 = canvas.create_line(SP_w, SP_h+row*6, width-SP_w, SP_h+row*6)
x7 = canvas.create_line(SP_w, SP_h+row*7, width-SP_w, SP_h+row*7)

column = int((width-SP_w-SP_w)/rectanglesize) #열 간격
y1 = canvas.create_line(SP_w+column, SP_h, SP_w +column, height-SP_h, fill="red")
y2 = canvas.create_line(SP_w+column*2, SP_h, SP_w +column*2, height-SP_h)
y3 = canvas.create_line(SP_w+column*3, SP_h, SP_w +column*3, height-SP_h)
y4 = canvas.create_line(SP_w+column*4, SP_h, SP_w +column*4, height-SP_h)
y5 = canvas.create_line(SP_w+column*5, SP_h, SP_w +column*5, height-SP_h)
y6 = canvas.create_line(SP_w+column*6, SP_h, SP_w +column*6, height-SP_h)
y7 = canvas.create_line(SP_w+column*7, SP_h, SP_w +column*7, height-SP_h)
a=canvas.create_rectangle(1,1,2,2)
showposition()
canvas.pack()
canvas.mainloop()
