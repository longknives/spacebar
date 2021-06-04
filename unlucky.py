import tkinter
from tkinter import *
import datetime
from threading import Time
import time
from tkinter import *
import tkinter

import keyboard
import pyautogui  


ws = Tk()
ws.title('Hotkey')
ws.geometry('1000x1000') 
key1 = 0.0
start = False
startkey = ''
altstart = False
writing = False

var = DoubleVar()

f = open("configseconds.txt", 'r+')
w = open("configkey.txt", 'r+')


def gui(key1, start, startkey, altstart, writing):

 if(writing == True):
       f = open("configseconds.txt", 'r+')
       w = open("configkey.txt", 'r+')
       f.truncate(0)
       w.truncate(0)
       f.write(str(cal.get()))
       w.write(str(e.get()))

  
 if start == True:
   startkey = e.get()
   seconds = cal.get() 
   


     
   while True: 
     try: 
        if keyboard.is_pressed(startkey):
          
           pyautogui.keyDown('space')  
           time.sleep(key1/1000)
 



           
     except:
        break 


cal=Entry(ws,  borderwidth=0)

cal.place(x=100,y=400)

       
      






dwnd = PhotoImage(file='timer1.png')
Button(ws, image=dwnd,  borderwidth=0,  command=lambda key1 = cal.get():gui(key1,start,startkey, altstart, writing)).place(x = 0, y = 0)




dwnd1 = PhotoImage(file='CORRECT.png')
button1 = Button(ws, image=dwnd1,   borderwidth=0, command=lambda start = True:gui(key1,start,startkey, altstart, writing)).place(x = 1290, y = 0)

e=Entry(ws,  borderwidth=0)

e.place(x=645,y=400)

dwnd2 = PhotoImage(file='loaf.png')
button1 = Button(ws, image=dwnd2,  borderwidth=0, command=lambda startkey = e.get():gui(key1,start,startkey, altstart, writing)).place(x = 600, y = 0)

text = Label(ws, text="ms")

text.place(x=225,y=400)




dwnd4 = PhotoImage(file='configawesome.png')
button5 = Button(ws, image=dwnd4,  borderwidth=0, command=lambda altstart = True:gui(key1,start,startkey, altstart, writing)).place(x = 1250, y = 500)

dwnd5 = PhotoImage(file='write.png')
button5 = Button(ws, image=dwnd5,  borderwidth=0, command=lambda writing = True:gui(key1,start,startkey, altstart, writing)).place(x = 800, y = 600)


   
def altok(altstart):
   if altstart == True:
            
   


     
    while True: 
     try: 
        if keyboard.is_pressed(w.readline()):
          
           pyautogui.keyDown('space')  
           time.sleep(f.readline()/1000)
 



           
     except:
        break 


ws.mainloop()
