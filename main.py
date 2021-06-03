import pyttsx3
from tkinter import *

def BS():
    Robin = pyttsx3.init()
    voices = Robin.getProperty('voices')
    Robin.setProperty('voice', voices[1].id)
    Robin.say("<Your Text>")
    Robin.runAndWait()

    wn = Tk()
    wn.title("<Your Text>")
    wn = Canvas(wn,width=632, height=851)
    wn.pack()
    image = PhotoImage(file = 'yourimage.jpg')
    wn.create_image(0,0, anchor=NW, image = image)

    wn.mainloop()
BS()





