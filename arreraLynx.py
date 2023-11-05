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
        self.frameAddWeather = Frame(windows,width=700,height=500,bg=color)
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
            Button(self.frameUserGenre,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self._passMeteo),
            Button(self.frameWeather,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self._passGPS),
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
        #frameWeather
        btnDomicile = Button(self.frameWeather,bg=color,fg=textColor,font=("arial","15"),text="Domicile",command=lambda : self._viewAddMeteo("domicile"))
        btnTravail = Button(self.frameWeather,bg=color,fg=textColor,font=("arial","15"),text="Lien de travail",command=lambda : self._viewAddMeteo("travail"))
        btnVille = Button(self.frameWeather,bg=color,fg=textColor,font=("arial","15"),text="Ajouter une ville",command=lambda : self._viewAddMeteo("ville"))
        #frameAddWeather
        self.labelTitreAdd = [Label(self.frameAddWeather,bg=color,fg=textColor,font=("arial","15"),text="Domicile"),
                          Label(self.frameAddWeather,bg=color,fg=textColor,font=("arial","15"),text="Ville"),
                          Label(self.frameAddWeather,bg=color,fg=textColor,font=("arial","15"),text="Travail")]
        self.entryVille = Entry(self.frameAddWeather,font=("arial","15"),borderwidth=2,relief="solid")
        self.btnAdd = Button(self.frameAddWeather,bg=color,fg=textColor,font=("arial","15"),text="Ajouter")
        #frameGPS
        btnAdresseDomicile = Button(self.frameGPS,bg=color,fg=textColor,font=("arial","15"),text="Adresse de domicile")
        btnAdresseTravail = Button(self.frameGPS,bg=color,fg=textColor,font=("arial","15"),text="Adresse de Travail")

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
        btnSuivant[2].place(x=((largeurFrame-btnSuivant[2].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[2].winfo_reqheight()))
        frameGenreUser.place(relx=0.5,rely=0.5,anchor="center")
        #frameWeather
        labelTitre[3].place(x=((largeurFrame-labelTitre[3].winfo_reqwidth())//2),y=0)
        btnDomicile.place(x=15,y=((hauteurFrame-btnDomicile.winfo_reqheight())//2))
        btnVille.place(relx=0.5,rely=0.5,anchor="center")
        btnTravail.place(x=((largeurFrame-btnTravail.winfo_reqwidth())-15),y=((hauteurFrame-btnTravail.winfo_reqheight())//2))
        btnSuivant[3].place(x=((largeurFrame-btnSuivant[3].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[3].winfo_reqheight()))
        #frameAddWeather
        self.entryVille.place(relx=0.5,rely=0.5,anchor="center")
        self.btnAdd.place(x=((largeurFrame-self.btnAdd.winfo_reqwidth())//2),y=(hauteurFrame-self.btnAdd.winfo_reqheight()))
        #frameGPS
        labelTitre[4].place(x=((largeurFrame-labelTitre[4].winfo_reqwidth())//2),y=0)
        btnAdresseDomicile.place(x=15,y=((hauteurFrame-btnAdresseDomicile.winfo_reqheight())//2))
        btnAdresseTravail.place(x=(largeurFrame-btnAdresseTravail.winfo_reqwidth())-15,y=((hauteurFrame-btnAdresseTravail.winfo_reqheight())//2))
        btnSuivant[4].place(x=((largeurFrame-btnSuivant[4].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[4].winfo_reqheight()))

    def _clearView(self):
        self.frameAcceuil.pack_forget()
        self.frameUserName.pack_forget()
        self.frameUserGenre.pack_forget()
        self.frameWeather.pack_forget()
        self.frameAddWeather.pack_forget()
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
    
    def _activeFrameWeather(self):
        self._clearView()
        self.frameWeather.pack()

    def _passMeteo(self):
        if self.varGenre.get():
            self._activeFrameWeather()
            self.fileNeuron.EcritureJSON("genre",self.varGenre.get())
        else :
           messagebox.showerror("Erreur","Veuillez entrer selectionner un genre avant de continuer") 
    
    def _viewAddMeteo(self,mode):
        self._clearView()
        self.entryVille.delete("0",END)
        self.frameAddWeather.pack()
        if mode == "domicile" :
            self.labelTitreAdd[0].place(x=((self.frameAcceuil.winfo_reqwidth()-self.labelTitreAdd[0].winfo_reqwidth())//2),y=0)
            self.btnAdd.configure(command=lambda : self._addMeteo(mode))
        else :
            if mode == "travail" :
                self.labelTitreAdd[2].place(x=((self.frameAcceuil.winfo_reqwidth()-self.labelTitreAdd[2].winfo_reqwidth())//2),y=0)
                self.btnAdd.configure(command=lambda : self._addMeteo(mode))
            else :
                if mode == "ville" :
                    self.labelTitreAdd[1].place(x=((self.frameAcceuil.winfo_reqwidth()-self.labelTitreAdd[1].winfo_reqwidth())//2),y=0)
                    self.btnAdd.configure(command=lambda : self._addMeteo(mode))
        
    
    def _addMeteo(self,mode):
        valeur = self.entryVille.get()
        if valeur:
            if mode == "domicile" :
                self.fileNeuron.EcritureJSON("lieuDomicile",valeur)
            else :
                if mode == "travail" :
                    self.fileNeuron.EcritureJSON("lieuTravail",valeur)  
                else :
                    if mode == "ville" :
                        self.fileNeuron.EcritureJSONList("listVille",valeur) 
            self._activeFrameWeather()
        else :
            self._activeFrameWeather()
            messagebox.showerror("Erreur","Aucun ville n'a été marquer dans la zone de texte")
    
    def _passGPS(self):
        self._clearView()
        self.frameGPS.pack()