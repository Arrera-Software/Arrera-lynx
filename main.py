from lynx_gui.arrera_lynx import*
from src.create_conf import create_conf

def main():
   arrera_lynx(conf_file="json_file/configLynx.json",
               theme_file="asset/theme/theme_bleu_blanc.json",
               gest=create_conf())

if __name__ == '__main__':
    main()
