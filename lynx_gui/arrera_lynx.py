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

        #self.__welcome.placeCenter()
        self.__user.placeCenter()

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
        pass

    def __environment_frame(self):
        pass

    def __system_frame(self):
        pass

    def __work_frame(self):
        pass

    def __ia_frame(self):
        pass