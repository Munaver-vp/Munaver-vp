import pyttsx3
from tkinter import *

def BS():
    Robin = pyttsx3.init()
    voices = Robin.getProperty('voices')
    Robin.setProperty('voice', voices[1].id)
    Robin.say("This Is a Munaver")
    Robin.runAndWait()

    wn = Tk()
    wn.title("Mohammed Munaver Vp")
    wn = Canvas(wn,width=632, height=851)
    wn.pack()
    image = PhotoImage(file = 'kali.JPG')
    wn.create_image(0,0, anchor=NW, image = image)

    wn.mainloop()
BS()





