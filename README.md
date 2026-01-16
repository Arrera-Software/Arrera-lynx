# Arrera Lynx

[Read in English](README_en.md)

Arrera Lynx a pour but d'être l'interface de premier démarrage des assistants d'Arrera, qui sont Arrera SIX, Arrera Ryley et Arrera Copilote.

## Explication des pages

L'interface est composée de 10 pages qui permettent de paramétrer l'assistant Arrera :

- **Page de bienvenue** : sert juste à montrer le logo de l'assistant avec une petite description de l'assistant (paramétrable depuis le fichier de configuration d'Arrera Lynx)
- **Page utilisateur** : sert à faire entrer à l'utilisateur son nom de famille, son prénom et à choisir le genre par lequel il veut que l'assistant l'appelle (seul paramètre où l'utilisateur est obligé de rentrer).
- **Page Mobilité** : page qui a pour fonction de demander à l'utilisateur son adresse de domicile et de travail pour la fonction GPS, ainsi que la ville de domicile et de travail pour la météo.
- **Page Environnement** : page pour enregistrer des raccourcis internet ou des logiciels externes à enregistrer dans l'assistant.
- **Page recherche** : permet de modifier le moteur de recherche par défaut utilisé par l'assistant.
- **Page Système** : cette page sert à activer ou non l'historique de l'assistant et les paramètres liés au micro (trigger word et sons au déclenchement du micro). Les paramètres du micro sont activables ou non dans le fichier de configuration d'Arrera Lynx.
- **Page Work** : la page Work a pour fonction de demander à l'utilisateur les dossiers de téléchargement et le dossier de travail Arrera Work.
- **Page Token** : cette page a pour but d'enregistrer le token GitHub de l'utilisateur (seule page qui s'affiche en fonction du fichier de configuration d'Arrera Lynx).
- **Page IA** : permet de paramétrer tous les paramètres liés au mode IA des assistants (téléchargement d'un modèle, activer ou non le mode IA, choix du modèle utilisé).
- **Page FIN** : page de fin qui affiche un texte de fin écrit dans le fichier de configuration.

## Explication du fichier de configuration

### Fichier JSON
```json
{
    "icon_unix": "",
    "icon_win": "",
    "text_presentation": "",
    "list_genre": [],
    "list_engine_search": [],
    "text_end": "",
    "github_integration": "1",
    "micro_use": "1"
}
```
### Explication des keys 

- `icon_unix` : Icône de l'interface en .png pour les systèmes UNIX (Linux, Mac OS, BSD)
- `icon_win` : Icône de l'interface en .ico pour Windows
- `text_presentation` : Texte de présentation de l'assistant qui se trouve sur la page bienvenue
- `list_genre` : Liste des genres qui seront dans le paramétrage des utilisateurs
- `list_engine_search` : Liste des moteurs de recherche qui seront dans le paramétrage du moteur de recherche
- `text_end` : Texte qui se trouve sur la page FIN pour introduire l'assistant
- `github_integration` : Clés pour activer ou non la page TOKEN pour paramétrer le token GitHub (`1` : Activer / `0` : Désactiver)
- `micro_use` : Clés pour activer les paramétrages du micro dans la page système (`1` : Activer / `0` : Désactiver)

## Integration 

Pour intégrer Arrera Lynx dans votre projet, vous devez suivre les étapes suivantes :

1. Importer la classe `arrera_lynx` depuis `lynx_gui.arrera_lynx`.
2. Créer une fonction qui retourne un objet `gestionnaire` configuré avec les paramètres de votre assistant.
3. Appeler la fonction `arrera_lynx` avec le chemin vers le fichier de configuration JSON, le chemin vers le fichier de thème JSON et l'objet `gestionnaire`.

Exemple d'intégration (basé sur `main.py`) :

```python
from lynx_gui.arrera_lynx import *
from src.create_conf import create_conf

def main():
   arrera_lynx(conf_file="json_file/configLynx.json",
               theme_file="asset/theme/theme_bleu_blanc.json",
               gest=create_conf())

if __name__ == '__main__':
    main()
```

Le fichier `create_conf.py` doit retourner un objet `gestionnaire` initialisé avec un objet `confNeuron`.
