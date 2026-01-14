from lib.arrera_tk import *
from librairy.travailJSON import *
from librairy.dectectionOS import OS
"""
Todo :
- Page Acceuil (Icon de l'assistant + petit texte qui presente l'assistant+ bouton configurer)
- Page USER (Un zone pour nom, une zone pour prenom et Menu pour choisir le genre)
- Partie mobiliter (Domicile Meteo / Travail meteo, adresse travaille , adresse domicile et un bouton pour ajouter un ville supplementaire pour la meteo)
- Environement numerique (Ajout de logiciel, ajout de racourcie web et config moteur de recherche)
- Systeme et Micro (Activer l'historique, Gerer trigerword et ajouter sons micro(activer ou non par le fichier de conf))
- Travail (Dossier travail Arrera Work, dossier download et token github(activer ou non par le fichier de conf))
- IA (Activer le mode IA, choisir et download model)
"""

class arrera_lynx(aTk):
    def __init__(self,conf_file:str,theme_file:str):
        self.__json_file = jsonWork(conf_file)
        os = OS()
        if os.osLinux() or os.osMac():
            icon = self.__json_file.getContentJsonFlag("icon_unix")
        else :
            icon = self.__json_file.getContentJsonFlag("icon_win")

        self.__assistant_name = self.__json_file.getContentJsonFlag("name_assistant")

        super().__init__(title=f"{self.__assistant_name} : Configuration",
                         width=800,height=500,resizable=False,
                         theme_file=theme_file,
                         icon=icon)

        self.__welcome = self.__welcome_frame()
        self.__user = self.__user_frame()
        self.__mobility = self.__mobility_frame()
        self.__environement = self.__environment_frame()
        self.__system = self.__system_frame()


        #self.__welcome.placeCenter()
        self.__system.placeCenter()

        self.mainloop()

    def __welcome_frame(self):
        m = aFrame(self,width=775,height=475)

        icon = aImage(250,250,self.__json_file.getContentJsonFlag("icon_unix"))
        licon = aLabel(m,text="",image=icon)

        lText = aLabel(m,text=self.__json_file.getContentJsonFlag("text_presentation"),police_size=25,
                       wraplength=400,justify="left")

        btn = aButton(m,text=f"Configurer {self.__assistant_name}",size=20)

        licon.placeTopLeft()
        lText.placeTopRight()
        btn.placeBottomRight()

        return m

    def __user_frame(self):

        listGenre = self.__json_file.getFlagListJson("list_genre")

        m = aFrame(self,width=775,height=475)
        info = aFrame(m,width=350,height=200)
        lTitle = aLabel(m,text="Information de l'utilisateur",police_size=25)
        lDesc = aLabel(m,police_size=20,
                       text="Pour apprendre a vous connectre l'assistant a besoin de savoir votre nom, prenom et le pronom que vous voulez qui vous appelle",
                       wraplength=250,justify="left")

        self.__eFirstName = aEntryLengend(info,text="Prénom",police_size=15)
        self.__eLastName = aEntryLengend(info,text="Nom",police_size=15)
        self.__mGenre = aOptionMenuLengend(info,text="Genre",values=listGenre,police_size=15)

        btn = aButton(m,text="Continuer",size=20)

        lTitle.placeTopCenter()
        info.placeRightCenter()
        lDesc.placeCenterLeft()
        self.__eFirstName.placeTopLeft()
        self.__eLastName.placeCenterLeft()
        self.__mGenre.placeBottomLeft()
        btn.placeBottomRight()

        return m

    def __mobility_frame(self):
        m = aFrame(self,width=775,height=475)

        lTitle = aLabel(m,text="Parametre de mobiliter",police_size=25)
        btn = aButton(m,text="Continuer",size=20)

        fMeteo = aFrame(m,width=365 ,height=300)
        ltMeteo = aLabel(fMeteo,text="Meteo",police_size=20)
        self.__eMDomicile = aEntryLengend(fMeteo,text="Ville de domicile",
                                          police_size=15)
        self.__eMWork = aEntryLengend(fMeteo, text="Ville de travail",
                                      police_size=15)
        btnATown = aButton(fMeteo, text="Ajouter une ville", size=20)

        fGPS = aFrame(m,width=365,height=300)
        ltGPS = aLabel(fGPS, text="GPS", police_size=20)
        self.__eGDomicile = aEntryLengend(fGPS, text="Adressse de domicile",
                                          police_size=15,width=175)
        self.__eGWork = aEntryLengend(fGPS, text="Adresse de travail",
                                      police_size=15)

        lTitle.placeTopCenter()

        fMeteo.placeRightCenter()
        fGPS.placeLeftCenter()
        btn.placeBottomRight()

        ltMeteo.placeTopCenter()
        self.__eMDomicile.placeCenterOnWidth(y=75)
        self.__eMWork.placeCenterOnWidth(y=125)
        btnATown.placeCenterOnWidth(y=175)

        ltGPS.placeTopCenter()
        self.__eGDomicile.placeCenterOnWidth(y=75)
        self.__eGWork.placeCenterOnWidth(y=125)

        return  m

    def __environment_frame(self):
        m = aFrame(self,width=775,height=475)

        lTitle = aLabel(m,text="Parametre d'environnement numerique",police_size=25)

        fWeb = aFrame(m,width=258,height=200)
        lTWeb = aLabel(fWeb,police_size=20,text="Racourcie interface")
        self.__eWebName = aEntryLengend(fWeb,text="Nom",police_size=15)
        self.__eWebLink = aEntryLengend(fWeb,text="Lien",police_size=15)

        listEngine = self.__json_file.getFlagListJson("list_engine_search")
        fSearch = aFrame(m,width=258,height=200)
        lTSearch = aLabel(fSearch,police_size=20,text="Moteur de recherche\npar default")
        self.__mSearchEngine = aOptionMenu(fSearch,value=listEngine)

        fSoft = aFrame(m,width=258,height=200)
        lTSoft = aLabel(fSoft,police_size=20,text="Logiciel externe")
        self.__eSoftName = aEntryLengend(fSoft,text="Nom",police_size=15)
        btnSoft = aButton(fSoft,text="Ajouter",size=20)

        btn = aButton(m,text="Continuer",size=20)

        fWeb.placeLeftCenter()
        fSearch.placeCenter()
        fSoft.placeRightCenter()

        lTWeb.placeTopCenter()
        self.__eWebName.placeCenterOnWidth(y=75)
        self.__eWebLink.placeCenterOnWidth(y=125)

        lTSearch.placeTopCenter()
        self.__mSearchEngine.placeCenterOnWidth(y=75)

        lTSoft.placeTopCenter()
        self.__eSoftName.placeCenterOnWidth(y=75)
        btnSoft.placeCenterOnWidth(y=125)

        lTitle.placeTopCenter()

        btn.placeBottomRight()
        return m

    def __system_frame(self):
        m = aFrame(self,width=775,height=475)

        lTitle = aLabel(m,text="Parametre general de l'assistant",police_size=25)

        fMicro = aFrame(m,width=350,height=200)
        lTMicro = aLabel(fMicro,police_size=20,text="Microphone")
        self.__enableSound = aSwicht(fMicro,text="Sons au demarage de l'ecoute",default_value=True)
        btnTriger = aButton(fMicro,text="Ajouter un mots declencheur",size=20)

        fSystem = aFrame(m,width=350,height=200)
        lTSysteme = aLabel(fSystem,police_size=20,text="Parametrage de l'assistant")
        self.__enableHist = aSwicht(fSystem,text="Activer l'historique",default_value=True)

        btn = aButton(m,text="Continuer",size=20)

        lTitle.placeTopCenter()

        fMicro.placeLeftCenter()
        fSystem.placeRightCenter()

        lTMicro.placeTopCenter()
        self.__enableSound.placeCenterOnWidth(y=75)
        btnTriger.placeCenterOnWidth(y=125)

        lTSysteme.placeTopCenter()
        self.__enableHist.placeCenter()

        btn.placeBottomRight()

        return m

    def __work_frame(self):
        pass

    def __ia_frame(self):
        pass