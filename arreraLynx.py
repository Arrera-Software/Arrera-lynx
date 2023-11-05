from tkinter import *
from tkinter import messagebox
from librairy.travailJSON import*

class ArreraLynx :
    def __init__(self,windows:Tk,fichierLynx:jsonWork,fichierNeuron:jsonWork):
        #fichier JSON
        self.fichierLynx = fichierLynx
        self.fileNeuron = fichierNeuron
        #Variable 
        self.varGenre = StringVar(windows)
        color = self.fichierLynx.lectureJSON("color")
        textColor = self.fichierLynx.lectureJSON("textColor")
        nomSoft = self.fichierLynx.lectureJSON("nameSoft")
        iconLogiciel = PhotoImage(file=str(self.fichierLynx.lectureJSON("iconSoft")))
        listGenre = self.fichierLynx.lectureJSONList("listGenre")
        #modification de la fenetre
        windows.title(nomSoft+": Premier demarage")
        windows.maxsize(700,500)
        windows.iconphoto(False,iconLogiciel)
        #cadre tkinter
        self.frameAcceuil = Frame(windows,width=700,height=500,bg=color)
        self.frameUserName = Frame(windows,width=700,height=500,bg=color)
        self.frameUserGenre = Frame(windows,width=700,height=500,bg=color)
        self.frameWeather = Frame(windows,width=700,height=500,bg=color)
        self.frameGPS = Frame(windows,width=700,height=500,bg=color)
        self.frameSoft =  Frame(windows,width=700,height=500,bg=color)
        self.frameEnd =  Frame(windows,width=700,height=500,bg=color)
        #widget 
        labelTitre = [
            Label(self.frameAcceuil,bg=color,fg=textColor,font=("arial","20"),text="Programme de premier demarage de"+nomSoft),
            Label(self.frameUserName,bg=color,fg=textColor,font=("arial","20"),text="Nom d'utilisateur"),
            Label(self.frameUserGenre,bg=color,fg=textColor,font=("arial","20"),text="Genre d'utilisateur"),
            Label(self.frameWeather,bg=color,fg=textColor,font=("arial","20"),text="Meteo"),
            Label(self.frameGPS,bg=color,fg=textColor,font=("arial","20"),text="GPS"),
            Label(self.frameSoft,bg=color,fg=textColor,font=("arial","20"),text="Logiciel"),
            Label(self.frameEnd,bg=color,fg=textColor,font=("arial","20"),text="Configuration terminer")
        ]
        btnSuivant = [
            Button(self.frameAcceuil,bg=color,fg=textColor,font=("arial","15"),text="Commencer",command=self._passUserName),
            Button(self.frameUserName,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self._passUserGenre),
            Button(self.frameUserGenre,bg=color,fg=textColor,font=("arial","15"),text="Suivant"),
            Button(self.frameWeather,bg=color,fg=textColor,font=("arial","15"),text="Suivant"),
            Button(self.frameGPS,bg=color,fg=textColor,font=("arial","15"),text="Suivant"),
            Button(self.frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Suivant"),
            Button(self.frameEnd,bg=color,fg=textColor,font=("arial","15"),text="Commencer à utiliser "+nomSoft)
        ]
        #frameUserName & frameUserGenre
        frameNameUser = Frame(self.frameUserName,bg=color)
        frameGenreUser = Frame(self.frameUserGenre,bg=color)
        labelIndicationUser = [
            Label(frameNameUser,bg=color,fg=textColor,font=("arial","15"),text="Nom :"),
            Label(frameGenreUser,bg=color,fg=textColor,font=("arial","15"),text="Genre :")
            ]
        self.entryName = Entry(frameNameUser,font=("arial","15"),borderwidth=2,relief="solid")
        menuGenre = OptionMenu(frameGenreUser,self.varGenre,*listGenre)
        #calcule affichage
        largeurFrame = self.frameAcceuil.winfo_reqwidth()
        hauteurFrame = self.frameAcceuil.winfo_reqheight()
        #affichage
        #frameAcceuil
        labelTitre[0].place(x=((largeurFrame-labelTitre[0].winfo_reqwidth())//2),y=0)
        btnSuivant[0].place(relx=0.5,rely=0.5,anchor="center")
        #frameUserName
        labelTitre[1].place(x=((largeurFrame-labelTitre[1].winfo_reqwidth())//2),y=0)
        btnSuivant[1].place(x=((largeurFrame-btnSuivant[1].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[1].winfo_reqheight()))
        labelIndicationUser[0].pack(side="left")
        self.entryName.pack(side="left")
        frameNameUser.place(relx=0.5,rely=0.5,anchor="center")
        #frameUserGenre
        labelTitre[2].place(x=((largeurFrame-labelTitre[2].winfo_reqwidth())//2),y=0)
        labelIndicationUser[1].pack(side="left")
        menuGenre.pack(side="left")
        btnSuivant[2].place(x=((largeurFrame-btnSuivant[2].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[1].winfo_reqheight()))
        frameGenreUser.place(relx=0.5,rely=0.5,anchor="center")

    def _clearView(self):
        self.frameAcceuil.pack_forget()
        self.frameUserName.pack_forget()
        self.frameUserGenre.pack_forget()
        self.frameWeather.pack_forget()
        self.frameGPS.pack_forget()
        self.frameSoft.pack_forget()
        self.frameEnd.pack_forget()

    def active(self):
        self.frameAcceuil.pack()

    def _passUserName(self):
        self._clearView()
        self.frameUserName.pack()
        
    def _passUserGenre(self):
        if self.entryName.get():
            self._clearView()
            self.frameUserGenre.pack()
            self.fileNeuron.EcritureJSON("user",self.entryName.get())
        else :
            messagebox.showerror("Erreur","Veuillez entrer un nom d'utilisateur avant de continuer")
    