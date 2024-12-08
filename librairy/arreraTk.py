import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import webbrowser as wb

VERSIONARRERATK = "1.0.0"

class CArreraTK :
    def __init__(self):
        self.__mode = 0
        self.__windowsColor = ""
        self.__textColor = ""
        self.__images = []

    def aTK(self, mode: int = 0, width: int = 800, height: int = 600,title: str = "ArreraTK", resizable: bool = False, bg: str = "", fg: str = "", icon: str = ""):
        """
        :param mode: 1 for Tkinter, 0 for customtkinter
        :param mainWindow: True for main window, False for Toplevel
        :param width: width of the window
        :param height: height of the window
        :param title: title of the window
        :param resizable: True for resizable, False for not resizable
        :param bg:  background color
        :param fg:  text color
        :param icon: icon of the window (ico file)
        """
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        ctheme = ctk.get_appearance_mode()
        if ctheme == "Dark":
            defaultColor = ctk.ThemeManager.theme["CTk"]["fg_color"][1]
            defaultTextColor = ctk.ThemeManager.theme["CTk"]["fg_color"][0]
        else:
            defaultColor = ctk.ThemeManager.theme["CTk"]["fg_color"][0]
            defaultTextColor = ctk.ThemeManager.theme["CTk"]["fg_color"][1]
        self.__mode = mode
        if mode == 0:
            self.__root = ctk.CTk()
            self.__root.configure(bg_color=defaultColor)
        else:
            self.__root = Tk()
        if icon != "":
            self.__root.iconbitmap(icon)
        self.__root.geometry(f"{width}x{height}")
        self.__root.title(title)
        self.__root.resizable(resizable, resizable)
        if bg == "":
            self.__root.configure(bg=defaultColor)
            self.__windowsColor = defaultColor
            self.__textColor = defaultTextColor
        else:
            self.__root.configure(bg=bg)
            self.__windowsColor = bg
            self.__textColor = fg

        return self.__root

    def aTopLevel(self, mode: int = 0, width: int = 800, height: int = 600,title: str = "ArreraTK", resizable: bool = False, bg: str = "", fg: str = "", icon: str = ""):
        """
        :param mode: 1 for Tkinter, 0 for customtkinter
        :param mainWindow: True for main window, False for Toplevel
        :param width: width of the window
        :param height: height of the window
        :param title: title of the window
        :param resizable: True for resizable, False for not resizable
        :param bg:  background color
        :param fg:  text color
        :param icon: icon of the window (ico file)
        """
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        ctheme = ctk.get_appearance_mode()
        if ctheme == "Dark":
            defaultColor = ctk.ThemeManager.theme["CTk"]["fg_color"][1]
            defaultTextColor = ctk.ThemeManager.theme["CTk"]["fg_color"][0]
        else:
            defaultColor = ctk.ThemeManager.theme["CTk"]["fg_color"][0]
            defaultTextColor = ctk.ThemeManager.theme["CTk"]["fg_color"][1]
        self.__mode = mode
        if mode == 0:
            self.__root = ctk.CTkToplevel()
        else:
            self.__root = Toplevel()
        if icon != "":
            self.__root.iconbitmap(icon)
        self.__root.geometry(f"{width}x{height}")
        self.__root.title(title)
        self.__root.resizable(resizable, resizable)
        if bg == "":
            self.__root.configure(bg=defaultColor)
            self.__windowsColor = defaultColor
            self.__textColor = defaultTextColor
        else:
            self.__root.configure(bg=bg)
            self.__windowsColor = bg
            self.__textColor = fg

        return self.__root

    def view(self):
        self.__root.mainloop()

    def title(self, title: str):
        self.__root.title(title)

    def setGeometry(self, width: int, height: int):
        self.__root.geometry(f"{width}x{height}")

    def setResizable(self, resizable: bool):
        self.__root.resizable(resizable, resizable)

    def setColor(self, bg: str, fg: str):
        self.__root.configure(bg=bg)
        self.__windowsColor = bg
        self.__textColor = fg


    def createImage(self, pathLight: str, pathDark: str = "none", tailleX: int = 250, tailleY: int = 250):
        if (self.__mode == 0):
            if (pathDark != "none"):
                image = ctk.CTkImage(
                    light_image=Image.open(pathLight),
                    dark_image=Image.open(pathDark),
                    size=(tailleX, tailleY))
                return image
            else :
                image = ctk.CTkImage(
                    light_image=Image.open(pathLight),
                    size=(tailleX, tailleY))
                return image
        else :
            if (pathDark != "none"):
                imageLight = PhotoImage(file=pathLight)
                imageDark = PhotoImage(file=pathDark)
                return [imageLight, imageDark]
            else :
                imageLight = PhotoImage(file=pathLight)
                return imageLight

    def createLabel(self, screen, text: str = "", image = None, bg : str = "", fg : str = "",police : str = "Arial", taille : int = 12):
        if (self.__mode == 0):
            label = ctk.CTkLabel(screen)
            if (text != ""):
                label.configure(text=text)
            if (image != None):
                label.configure(image=image)
            if (bg != ""):
                label.configure(bg_color=bg)
            if (fg != ""):
                label.configure(fg_color=fg)
            if (police != "Arial" or taille != 12):
                label.configure(font=(police,taille,"normal"))
        else :
            label = Label(screen)
            if (text != ""):
                label.configure(text=text)
            if (image != None):
                label.configure(image=image)
            if (bg != ""):
                label.configure(bg=bg)
            if (fg != ""):
                label.configure(fg=fg)
            if (police != "Arial" or taille != 12):
                label.configure(font=(police, taille))
        return label

    def createButton(self, screen, text: str = "", image = None, bg : str = "", fg : str = "", command = None,police : str = "Arial", taille : int = 12):
        if (self.__mode == 0):
            btn = (ctk.CTkButton(screen))
            if (text != ""):
                btn.configure(text=text)
            if (image != None):
                btn.configure(image=image)
            if (bg != ""):
                btn.configure(bg_color=bg)
            if (fg != ""):
                btn.configure(fg_color=fg)
            if (command != None):
                btn.configure(command=command)
            if (police != "Arial" or taille != 12):
                btn.configure(font=(police,taille,"normal"))
        else :
            btn = Button(screen)
            if (text != ""):
                btn.configure(text=text)
            if (image != None):
                btn.configure(image=image)
            if (bg != ""):
                btn.configure(bg=bg)
            if (fg != ""):
                btn.configure(fg=fg)
            if (command != None):
                btn.configure(command=command)
            if (police != "Arial" or taille != 12):
                btn.configure(font=(police, taille))
        return btn

    def createEntry(self, screen, bg : str = "", fg : str = "",placeholderText :str = "",police : str = "Arial", taille : int = 12,width : int = 20):
        if (self.__mode == 0):
            entry = ctk.CTkEntry(screen)
            if (bg != ""):
                entry.configure(bg_color=bg)
            if (fg != ""):
                entry.configure(fg_color=fg)
            if (placeholderText != ""):
                entry.configure(placeholder_text=placeholderText)
            if (police != "Arial" or taille != 12):
                entry.configure(font=(police, taille,"normal"))
            if (width != 20):
                entry.configure(width=width)
        else :
            entry = Entry(screen)
            if (bg != ""):
                entry.configure(bg=bg)
            if (fg != ""):
                entry.configure(fg=fg)
            if (police != "Arial" or taille != 12):
                entry.configure(font=(police, taille))
        return entry

    def createText(self, screen, bg : str = "", fg : str = ""):
        text = Text(screen)
        if (bg != ""):
            text.configure(bg=bg)
        if (fg != ""):
            text.configure(fg=fg)

        return text

    def createCheckbox(self, screen, text: str = "", bg : str = "", fg : str = ""):
        checkbox = Checkbutton(screen,text=text)
        if (bg != ""):
            checkbox.configure(bg=bg)
        if (fg != ""):
            checkbox.configure(fg=fg)
        return checkbox

    def createRadioButton(self, screen, text: str = "", bg : str = "", fg : str = ""):
        if (self.__mode == 0):
            radio = ctk.CTkRadioButton(screen)
            if (text != ""):
                radio.configure(text=text)
            if (bg != ""):
                radio.configure(bg_color=bg)
            if (fg != ""):
                radio.configure(fg_color=fg)
        else :
            radio = Radiobutton(screen,text=text)
            if (bg != ""):
                radio.configure(bg=bg)
            if (fg != ""):
                radio.configure(fg=fg)
        return radio

    def createCanvas(self, screen, width: int, height: int, bg : str = "",imageFile : str = ""):
        canvas = Canvas(screen, width=width, height=height)
        if (bg != ""):
            canvas.configure(bg=bg)
        if (imageFile != ""):
            photo = PhotoImage(file=imageFile,master=canvas)
            canvas.image_names = photo
            canvas.create_image(0, 0, image=photo, anchor="nw")
        return canvas

    def createFrame(self, screen,width : int = 0 ,height : int = 0,  bg : str = ""):
        if (self.__mode == 0):
            frame = ctk.CTkFrame(screen)
            if (width != 0):
                frame.configure(width=width)
            if (height != 0):
                frame.configure(height=height)
            if (bg != ""):
                frame.configure(bg_color=bg)
            else:
                frame.configure(bg_color=self.__windowsColor)
            frame.update()
        else :
            frame = Frame(screen)
            if (width != 0):
                frame.configure(width=width)
            if (height != 0):
                frame.configure(height=height)
            if (bg != ""):
                frame.configure(bg=bg)
        return frame

    def createOptionMenu(self,screen,value: list, var:StringVar,taille : int = 0, police :str = "" ):
        if (self.__mode == 0):
            option = ctk.CTkOptionMenu(screen,variable=var,values=value)
        else:
            option = OptionMenu(screen,var,*value)
        if (police != "" and taille != 0):
            option.configure(font=(police,taille,"normal"))
        var.set(value[0])
        return option

    def placeLeftTop(self, widget):
        widget.place(relx=0, rely=0, anchor='nw')

    def placeRightTop(self, widget):
        widget.place(relx=1, rely=0, anchor='ne')

    def placeLeftBottom(self, widget):
        widget.place(relx=0, rely=1, anchor='sw')

    def placeRightBottom(self, widget):
        widget.place(relx=1, rely=1, anchor='se')

    def placeCenter(self, widget):
        widget.place(relx=0.5, rely=0.5, anchor='center')

    def placeLeftCenter(self, widget):
        widget.place(relx=0, rely=0.5, anchor='w')

    def placeRightCenter(self, widget):
        widget.place(relx=1, rely=0.5, anchor='e')

    def placeTopCenter(self, widget):
        widget.place(relx=0.5, rely=0, anchor='n')

    def placeBottomCenter(self, widget):
        widget.place(relx=0.5, rely=1, anchor='s')

    def pack(self, widget,xExpand : bool = False , yExpand : bool = False):
        if (xExpand and yExpand):
            widget.pack(expand="both")
        else:
            if (xExpand):
                widget.pack(expand="x")
            else:
                if (yExpand):
                    widget.pack(expand="y")
                else:
                    widget.pack()

    def packLeft(self, widget,xExpand : bool = False , yExpand : bool = False):
        if (xExpand and yExpand):
            widget.pack(expand="both",side="left")
        else:
            if (xExpand):
                widget.pack(expand="x",side="left")
            else:
                if (yExpand):
                    widget.pack(expand="y",side="left")
                else:
                    widget.pack(side="left")

    def packRight(self, widget,xExpand : bool = False , yExpand : bool = False):
        if (xExpand and yExpand):
            widget.pack(expand="both",side="right")
        else:
            if (xExpand):
                widget.pack(expand="x",side="right")
            else:
                if (yExpand):
                    widget.pack(expand="y",side="right")
                else:
                    widget.pack(side="right")

    def packTop(self, widget,xExpand : bool = False , yExpand : bool = False):
        if (xExpand and yExpand):
            widget.pack(expand="both",side="top")
        else:
            if (xExpand):
                widget.pack(expand="x",side="top")
            else:
                if (yExpand):
                    widget.pack(expand="y",side="top")
                else:
                    widget.pack(side="top")

    def packBottom(self, widget,xExpand : bool = False , yExpand : bool = False):
        if (xExpand and yExpand):
            widget.pack(expand="both",side="bottom")
        else:
            if (xExpand):
                widget.pack(expand="x",side="bottom")
            else:
                if (yExpand):
                    widget.pack(expand="y",side="bottom")
                else:
                    widget.pack(side="bottom")

    def aproposWindows(self,nameSoft:str,iconFile:str,version:str,copyright:str,linkSource:str,linkWeb:str):
        if (self.__mode == 0):
            apropos = ctk.CTkToplevel()
            apropos.configure(bg=self.__windowsColor)
            apropos.title("A propos : "+nameSoft)
            apropos.maxsize(400,300)
            apropos.minsize(400,300)
            icon = ctk.CTkImage(light_image=Image.open(iconFile),size=(100,100))
            mainFrame = ctk.CTkFrame(apropos,width=400,height=250,border_width=0)
            frameBTN = ctk.CTkFrame(apropos,width=400,height=50,border_width=0)
            frameLabel = ctk.CTkFrame(apropos,border_width=0)

            labelIcon = ctk.CTkLabel(mainFrame,image=icon,text="")
            labelSoft = ctk.CTkLabel(frameLabel,text=nameSoft+" version "+version,font=("Arial",20))
            labelVersion = ctk.CTkLabel(frameLabel,text="Arrera TK version "+VERSIONARRERATK,font=("Arial",13))
            labelCopy = ctk.CTkLabel(mainFrame,text=copyright,font=("Arial",13))

            btnLinkSource = ctk.CTkButton(frameBTN,text="Source code",command= lambda :  wb.open(linkSource))
            btnLinkWeb = ctk.CTkButton(frameBTN,text="Web site",command= lambda :  wb.open(linkWeb))

            labelIcon.place(relx=0.5, rely=0.0, anchor="n")
            labelSoft.pack()
            labelVersion.pack()
            labelCopy.place(relx=0.5, rely=1.0, anchor="s")

            frameLabel.place(relx=0.5, rely=0.5, anchor="center")
            mainFrame.pack(side="top")
            frameBTN.pack(side ="bottom")


            btnLinkSource.place(relx=1, rely=1, anchor='se')
            btnLinkWeb.place(relx=0, rely=1, anchor='sw')
        else :
            apropos = Toplevel()
            apropos.title("A propos : " + nameSoft)
            apropos.configure(bg=self.__windowsColor)
            apropos.maxsize(400, 300)
            apropos.minsize(400, 300)
            icon = ctk.CTkImage(light_image=Image.open(iconFile), size=(100, 100))
            mainFrame = Frame(apropos, width=400, height=250,bg=self.__windowsColor)
            frameBTN = Frame(apropos, width=400, height=50,bg=self.__windowsColor)
            frameLabel = Frame(apropos,bg=self.__windowsColor)

            # Traitement Image
            labelIcon = Label(mainFrame, bg=self.__windowsColor)
            imageOrigine = Image.open(iconFile)
            imageRedim = imageOrigine.resize((100,100))
            icon = ImageTk.PhotoImage(imageRedim, master=labelIcon)
            labelIcon.image_names = icon
            labelIcon.configure(image=icon)

            labelSoft = Label(frameLabel, text=nameSoft + " version " + version, font=("Arial", 20),bg=self.__windowsColor,fg=self.__textColor)
            labelVersion = Label(frameLabel, text="Arrera TK version " + VERSIONARRERATK, font=("Arial", 13),bg=self.__windowsColor,fg=self.__textColor)
            labelCopy = Label(mainFrame, text=copyright, font=("Arial", 13),bg=self.__windowsColor,fg=self.__textColor)

            btnLinkSource = Button(frameBTN, text="Source code", command=lambda: wb.open(linkSource),bg=self.__windowsColor,fg=self.__textColor)
            btnLinkWeb = Button(frameBTN, text="Web site", command=lambda: wb.open(linkWeb),bg=self.__windowsColor,fg=self.__textColor)

            labelIcon.place(relx=0.5, rely=0.0, anchor="n")
            labelSoft.pack()
            labelVersion.pack()
            labelCopy.place(relx=0.5, rely=1.0, anchor="s")

            frameLabel.place(relx=0.5, rely=0.5, anchor="center")
            mainFrame.pack(side="top")
            frameBTN.pack(side="bottom")

            btnLinkSource.place(relx=1, rely=1, anchor='se')
            btnLinkWeb.place(relx=0, rely=1, anchor='sw')