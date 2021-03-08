from tkinter import*
from PIL import ImageTk,Image
from datetime import datetime
import pytz
import time
root = Tk()
root.title("TitlehateSpyder")
root.geometry("1000x1000")

image1 = ImageTk.PhotoImage(Image.open("1image.jpg"))
image2 = ImageTk.PhotoImage(Image.open("2image.jpg"))

ipia = Label(root,text = "Ipia")
ipia.place(relx = 0.2,rely = 0.05,anchor = CENTER)

ipiaclock = Label(root)
ipiaclock['image'] = image2
ipiaclock.place(relx = 0.2,rely = 0.35,anchor = CENTER)

ipiatime = Label(root)
ipiatime.place(relx = 0.2,rely = 0.65,anchor=CENTER)



us = Label(root,text = "Us")
us.place(relx = 0.7,rely = 0.05,anchor = CENTER)

usclock = Label(root)
usclock['image'] = image1
usclock.place(relx = 0.7,rely = 0.35,anchor = CENTER)

ustime = Label(root)
ustime.place(relx = 0.7,rely = 0.65,anchor=CENTER)




ipia1 = Label(root,text = "Ipia")
ipia1.place(relx = 0.4,rely = 0.05,anchor = CENTER)

ipiaclock1 = Label(root)
ipiaclock1['image'] = image2
ipiaclock1.place(relx = 0.4,rely = 0.35,anchor = CENTER)

ipiatime1 = Label(root)
ipiatime1.place(relx = 0.4,rely = 0.65,anchor=CENTER)



us1 = Label(root,text = "Us")
us1.place(relx = 0.9,rely = 0.05,anchor = CENTER)

usclock1 = Label(root)
usclock1['image'] = image1
usclock1.place(relx = 0.9,rely = 0.35,anchor = CENTER)

ustime1 = Label(root)
ustime1.place(relx = 0.9,rely = 0.65,anchor=CENTER)

class India():
    def times(self):
        home = pytz.timezone('Asia/Kolkata')
        localtime = datetime.now(home)
        ct = localtime.strftime("%H:%M:%S")
        ipiatime['text'] = "Time - " + ct
        ipiatime.after(200,self.times)
        
class Us():
    def times(self):
        home = pytz.timezone('US/Central')
        localtime = datetime.now(home)
        ct = localtime.strftime("%H:%M:%S")
        ustime['text'] = "Time - " + ct
        ustime.after(200,self.times)
        
class India1():
    def times(self):
        home = pytz.timezone('Japan')
        localtime = datetime.now(home)
        ct = localtime.strftime("%H:%M:%S")
        ipiatime1['text'] = "Time - " + ct
        ipiatime1.after(200,self.times)
        
class Us1():
    def times(self):
        home = pytz.timezone('Australia/ACT')
        localtime = datetime.now(home)
        ct = localtime.strftime("%H:%M:%S")
        ustime1['text'] = "Time - " + ct
        ustime1.after(200,self.times)
        

ipiaob = India()
usob = Us()
ipiaob1 = India1()
usob1 = Us1()


indiab = Button(root,text = "qazshowind",command = ipiaob.times)
indiab.place(relx = 0.2,rely = 0.8,anchor = CENTER)

usb = Button(root,text = "qazshowind",command = usob.times)
usb.place(relx = 0.7,rely = 0.8,anchor = CENTER)

indiab1 = Button(root,text = "qazshowind",command = ipiaob1.times)
indiab1.place(relx = 0.4,rely = 0.8,anchor = CENTER)

usb1 = Button(root,text = "qazshowind",command = usob1.times)
usb1.place(relx = 0.5,rely = 0.8,anchor = CENTER)

root.mainloop()









