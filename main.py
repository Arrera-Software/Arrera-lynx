from arreraLynx import*

def main():
    lynx = ArreraLynx("configLynx.json",
                      "FichierNeuron/configUser.json",
                      "FichierNeuron/configNeuron.json")
    lynx.active()

if __name__ == '__main__':
    main()
