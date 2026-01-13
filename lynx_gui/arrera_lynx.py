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

        super().__init__(title=f"{self.__json_file.getContentJsonFlag("name_assistant")} : Configuration",
                         width=800,height=500,resizable=False,
                         theme_file=theme_file,
                         icon=icon)

        self.mainloop()

    def __welcome_frame(self):
        pass

    def __user_frame(self):
        pass

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