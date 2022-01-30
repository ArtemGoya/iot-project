import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter.constants import NSEW
import configparser
from Controllers.MainController import MainController
from Views.MainView import MainView
from Services.GalleryManagerService import GelleryManagerService

LOOP_INTERVAL = 1_000
# CONFIG = "m_config.txt"

class BasicGui(tk.Frame):
    def __init__(self, master=None):
        # self.konfig = configparser.ConfigParser()
        # self.konfig.read(CONFIG, "UTF8")
        tk.Frame.__init__(self, master)
        self.parent = master
        self.parent.protocol("WM_DELETE_WINDOW", self.file_quit)
        self.parent.resizable(width=False, height=False)
        # self.domyslne = self.konfig["DEFAULT"]
        self.geometria_baza = "840x775+204+118"
        self.parent.geometry(self.geometria_baza)
        self.utworz_bazowe_menu()
        self.utworz_status()
        self.utworz_okno_robocze()
        self.gallery()
        self.parent.columnconfigure(0, weight=999)
        self.parent.columnconfigure(1, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.parent.rowconfigure(1, weight=9999)
        self.parent.rowconfigure(2, weight=1)

    def gallery(self):
        self.color = "SystemButtonFace"
        
        self.createLayout()
        
        
    def createLayout(self):
        title=Frame(self.robocze, height=90, background="#fff")
        title.grid(column=0, row=0, rowspan=1, columnspan=4)
        self.titleVal = Label(title, height=4, text="Galeria handlowa Amber", font =("Helvetica", 25), bg="#fff")
        self.titleVal.grid(row=3, column=0, columnspan=1)
        Frame(self.robocze, height=20, width=55, background="#fff").grid(column=0, row=1, rowspan=1)
        self.createLeftFrame()
        Frame(self.robocze, height=50, width=55, background="#fff").grid(column=2, row=1, rowspan=1)
        self.createRightFrame()
        
    
    def createLeftFrame(self):
        detectorsData = Frame(self.robocze, height=600, width=400, background=self.color, highlightbackground="black", highlightthickness=2)
        detectorsData.grid(column=1, row=1, rowspan=1)
        detectorsLabel = Label(detectorsData, width=15, height=3, text="Dane z czujników", font =("Helvetica", 15), bg=self.color)
        detectorsLabel.grid(row=0, column=0, columnspan=2)
        outDetectorsLabel = Label(detectorsData, width=20, height=2, text="Zewnątrz:", font =("Helvetica", 20), bg=self.color)
        outDetectorsLabel.grid(row=1, column=0, columnspan=2)
        outTempLabel = Label(detectorsData, width=15, height=2, text="Temperatura:", font =("Helvetica", 12), bg=self.color)
        outTempLabel.grid(row=2, column=0, columnspan=1)
        self.outTempValLabel = Label(detectorsData, width=15, height=2, text="0*C", font =("Helvetica", 12), bg=self.color)
        self.outTempValLabel.grid(row=2, column=1, columnspan=1)
        outHumLabel = Label(detectorsData, width=15, height=2, text="Wilgotność:", font =("Helvetica", 12), bg=self.color)
        outHumLabel.grid(row=3, column=0, columnspan=1)
        self.outHumValLabel = Label(detectorsData, width=15, height=2, text="32%", font =("Helvetica", 12), bg=self.color)
        self.outHumValLabel.grid(row=3, column=1, columnspan=1)
        outLightLabel = Label(detectorsData, width=15, height=2, text="Oświetlenie:", font =("Helvetica", 12), bg=self.color)
        outLightLabel.grid(row=4, column=0, columnspan=1)
        self.outLightValLabel = Label(detectorsData, width=15, height=2, text="250 lux", font =("Helvetica", 12), bg=self.color)
        self.outLightValLabel.grid(row=4, column=1, columnspan=1)
        outWindLabel = Label(detectorsData, width=15, height=2, text="Temperatura:", font =("Helvetica", 12), bg=self.color)
        outWindLabel.grid(row=5, column=0, columnspan=1)
        self.outWindValLabel = Label(detectorsData, width=15, height=2, text="0*C", font =("Helvetica", 12), bg=self.color)
        self.outWindValLabel.grid(row=5, column=1, columnspan=1)
        
        inDetectorsLabel = Label(detectorsData, width=20, height=2, text="Wewnątrz:", font =("Helvetica", 20), bg=self.color)
        inDetectorsLabel.grid(row=6, column=0, columnspan=2)
        inTempLabel = Label(detectorsData, width=15, height=2, text="Temperatura:", font =("Helvetica", 12), bg=self.color)
        inTempLabel.grid(row=7, column=0, columnspan=1)
        self.inTempValLabel = Label(detectorsData, width=15, height=2, text="23*C", font =("Helvetica", 12), bg=self.color)
        self.inTempValLabel.grid(row=7, column=1, columnspan=1)
        inHumLabel = Label(detectorsData, width=15, height=2, text="Wilgotność:", font =("Helvetica", 12), bg=self.color)
        inHumLabel.grid(row=8, column=0, columnspan=1)
        self.inHumValLabel = Label(detectorsData, width=15, height=2, text="20%", font =("Helvetica", 12), bg=self.color)
        self.inHumValLabel.grid(row=8, column=1, columnspan=1)
        inLightLabel = Label(detectorsData, width=15, height=2, text="Oświetlenie:", font =("Helvetica", 12), bg=self.color)
        inLightLabel.grid(row=9, column=0, columnspan=1)
        self.inLightValLabel = Label(detectorsData, width=15, height=2, text="500 lux", font =("Helvetica", 12), bg=self.color)
        self.inLightValLabel.grid(row=9, column=1, columnspan=1)
        
        Label(detectorsData, width=15, height=2, text="", font =("Helvetica", 12), bg=self.color).grid(row=10, column=1, columnspan=1)
        
        
        

    def createRightFrame(self):
        peripheralsData = Frame(self.robocze, height=600, width=400, background=self.color, highlightbackground="black", highlightthickness=2)
        peripheralsData.grid(column=3, row=1, rowspan=1)
        periphealsLabel = Label(peripheralsData, width=15, height=3, text="Kontrola", font =("Helvetica", 15), bg=self.color)
        periphealsLabel.grid(row=0, column=0, columnspan=2)
        lightingLabel = Label(peripheralsData, width=20, height=2, text="Oświetlenie:", font =("Helvetica", 20), bg=self.color)
        lightingLabel.grid(row=1, column=0, columnspan=2)
        lightingStateLabel = Label(peripheralsData, width=15, height=2, text="Stan:", font =("Helvetica", 12), bg=self.color)
        lightingStateLabel.grid(row=2, column=0, columnspan=1)
        self.lightingStateValLabel = Label(peripheralsData, width=15, height=2, text="Włączone", font =("Helvetica", 12), bg=self.color)
        self.lightingStateValLabel.grid(row=2, column=1, columnspan=1)
        lightingModeLabel = Label(peripheralsData, width=15, height=2, text="Tryb:", font =("Helvetica", 12), bg=self.color)
        lightingModeLabel.grid(row=3, column=0, columnspan=1)
        
        self.lightingModeVal = StringVar(peripheralsData)
        self.lightingModeVal.set("Automatyczny") # default value

        lightningOptionMenu = OptionMenu(peripheralsData, self.lightingModeVal, "Automatyczny", "Włączone", "Wyłączone")
        lightningOptionMenu.grid(row=3, column=1, columnspan=1)
        
        windowsLabel = Label(peripheralsData, width=20, height=2, text="Okiennice:", font =("Helvetica", 20), bg=self.color)
        windowsLabel.grid(row=4, column=0, columnspan=2)
        windowsStateLabel = Label(peripheralsData, width=15, height=2, text="Stan:", font =("Helvetica", 12), bg=self.color)
        windowsStateLabel.grid(row=5, column=0, columnspan=1)
        self.windowsStateValLabel = Label(peripheralsData, width=15, height=2, text="Otwarte", font =("Helvetica", 12), bg=self.color)
        self.windowsStateValLabel.grid(row=5, column=1, columnspan=1)
        windowsModeLabel = Label(peripheralsData, width=15, height=2, text="Tryb:", font =("Helvetica", 12), bg=self.color)
        windowsModeLabel.grid(row=6, column=0, columnspan=1)
        
        self.windowsModeVal = StringVar(peripheralsData)
        self.windowsModeVal.set("Automatyczny") # default value

        windowsOptionMenu = OptionMenu(peripheralsData, self.windowsModeVal, "Automatyczny", "Otwarte", "Zamknięte")
        windowsOptionMenu.grid(row=6, column=1, columnspan=1)
        
        Label(peripheralsData, width=15, height=9, text="", font =("Helvetica", 12), bg=self.color).grid(row=7, column=1, columnspan=1)


    # Creates status bar
    def utworz_status(self):
        self.statusbar = tk.Label(self.parent, text="Linia statusu...",
                                    anchor=tkinter.W)
        self.statusbar.after(5000, self.clearStatusBar)
        self.statusbar.grid(row=2, column=0, columnspan=2,
                            sticky=tkinter.EW)

    # Sets status bar with given message
    def ustawStatusBar(self, txt):
        self.statusbar["text"] = txt

    # Clears message in status bar
    def clearStatusBar(self):
        self.statusbar["text"] = ""

    # Creates basic menu "File" in menu bar
    def utworz_bazowe_menu(self):
        self.menubar = tk.Menu(self.parent)
        self.parent["menu"] = self.menubar
        fileMenu = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
                ("Save", self.file_save, "Ctrl+S", "<Control-s>"),
                ("Quit", self.file_quit, "Ctrl+Q", "<Control-q>")):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0,
                                        command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="File", menu=fileMenu, underline=0)
        pass

    # Creates basic menu "Help" in menu bar
    def dodaj_menu_help(self):
        pass

    # Creates basic menu "Edit" in menu bar
    def dodaj_menu_edit(self):
        pass

    # Ends program
    def file_quit(self, event=None):
        reply = tkinter.messagebox.askyesno(
            "koniec pracy",
            "naprawdę kończysz?", parent=self.parent)
        event = event
        if reply:
            # with open(CONFIG, 'w') as config_plik:
            #     self.konfig.write(config_plik)
            self.parent.destroy()
        pass

    # Saves configuration in config file
    def file_save(self, event=None):
        event = event
        pass

    # Creates basic graphic workspace for game gui
    def utworz_okno_robocze(self):
        self.robocze = tk.Frame(self.parent, background='#ffffff')
        self.robocze.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)
        pass    

if __name__ == '__main__':
    root = tk.Tk()
    app = BasicGui(master=root)
    galery_manager = GelleryManagerService()
    view = MainView(app)
    controller = MainController(view, galery_manager)
    view.set_controller(controller)


    def loop():
        galery_manager.loop()
        print("test")

    def runLoop():
        loop()
        app.after(LOOP_INTERVAL, runLoop)

    app.after(LOOP_INTERVAL, runLoop)
    app.mainloop()
