# Arrera Lynx

Arrera Lynx aims to be the first-start interface for Arrera assistants, which are Arrera SIX, Arrera Ryley, and Arrera Copilote.

## Pages Explanation

The interface is composed of 10 pages that allow configuring the Arrera assistant:

- **Welcome Page**: serves only to show the assistant's logo with a small description of the assistant (configurable from the Arrera Lynx configuration file).
- **User Page**: serves to have the user enter their last name, first name, and choose the gender by which they want the assistant to call them (the only parameter the user is required to enter).
- **Mobility Page**: page whose function is to ask the user for their home and work address for the GPS function, as well as the home and work city for the weather.
- **Environment Page**: page to save internet shortcuts or external software to be saved in the assistant.
- **Search Page**: allows modifying the default search engine used by the assistant.
- **System Page**: this page serves to enable or disable the assistant's history and microphone-related settings (trigger word and sounds upon microphone activation). Microphone settings can be enabled or disabled in the Arrera Lynx configuration file.
- **Work Page**: the Work page has the function of asking the user for download folders and the Arrera Work working folder.
- **Token Page**: this page aims to save the user's GitHub token (the only page that displays depending on the Arrera Lynx configuration file).
- **AI Page**: allows configuring all settings related to the AI mode of the assistants (downloading a model, enabling or disabling AI mode, choosing the model used).
- **END Page**: end page that displays an ending text written in the configuration file.

## Configuration File Explanation

### JSON File
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
### Keys Explanation

- `icon_unix`: Interface icon in .png for UNIX systems (Linux, Mac OS, BSD)
- `icon_win`: Interface icon in .ico for Windows
- `text_presentation`: Presentation text of the assistant found on the welcome page
- `list_genre`: List of genders that will be in the user settings
- `list_engine_search`: List of search engines that will be in the search engine settings
- `text_end`: Text found on the END page to introduce the assistant
- `github_integration`: Keys to enable or disable the TOKEN page to configure the GitHub token (`1`: Enable / `0`: Disable)
- `micro_use`: Keys to enable microphone settings in the system page (`1`: Enable / `0`: Disable)

## Integration

To integrate Arrera Lynx into your project, you must follow these steps:

1. Import the `arrera_lynx` class from `lynx_gui.arrera_lynx`.
2. Create a function that returns a `gestionnaire` object configured with your assistant's parameters.
3. Call the `arrera_lynx` function with the path to the JSON configuration file, the path to the JSON theme file, and the `gestionnaire` object.

Integration example (based on `main.py`):

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

The `create_conf.py` file must return a `gestionnaire` object initialized with a `confNeuron` object.