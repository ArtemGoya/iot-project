import tkinter as tk
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
        pass

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
