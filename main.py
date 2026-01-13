from arreraLynx import*

def main():
    lynx = ArreraLynx("configLynx.json",
                      "json_file/configUser.json",
                      "json_file/configNeuron.json")
    lynx.active()

if __name__ == '__main__':
    main()
