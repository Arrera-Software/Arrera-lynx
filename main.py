from tkinter import *
from librairy.travailJSON import*
from arreraLynx import*

screen = Tk()
lynxFile = jsonWork("configLynx.json")
userFile = jsonWork("FichierNeuron/configUser.json")
neuronFile = jsonWork("FichierNeuron/configNeuron.json")
lynx = ArreraLynx(screen,lynxFile,userFile,neuronFile)
screen.configure(bg="red")
btnActive = Button(screen,text="Active interface")
def active():
    btnActive.pack_forget()
    lynx.active()
btnActive.configure(command=active)
btnActive.pack()
screen.mainloop()