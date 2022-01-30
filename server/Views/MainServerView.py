

from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter.messagebox
from tkinter.constants import NSEW
import configparser
from turtle import bgcolor

import database as db

LOOP_INTERVAL = 1_000

# CONFIG = "m_config.txt"


class MainServerView(Frame):

    def __init__(self, parent):
        # self.konfig = configparser.ConfigParser()
        # self.konfig.read(CONFIG, "UTF8")
        super().__init__(parent)
        self.parent = parent
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
        title = Frame(self.robocze, height=100, width=800, background="#fff")
        title.pack(fill=None, expand=False)
        title.pack_propagate(0)
        self.titleVal = Label(title, height=4, text="Podłączeni klienci", font=(
            "Helvetica", 25), bg="#fff")
        self.titleVal.pack(fill=None, expand=False)
        self.createLeftFrame()

    def createLeftFrame(self):
        temp = Frame(self.robocze, height=700, width=800,
                     background=self.color, highlightbackground="black", highlightthickness=2)
        temp.pack()
        temp.pack_propagate(0)
        s = Scrollbar(temp)
        s.pack(side=RIGHT, fill=Y)

        detectorsData2 = Canvas(temp, height=700, width=800,
                                background=self.color, yscrollcommand=s.set)
        detectorsData2.pack()
        detectorsData2.pack_propagate(0)
        s.config(command=detectorsData2.yview)

        detectorsData = ttk.Frame(detectorsData2)

        detectorsData.bind(
            "<Configure>",
            lambda e: detectorsData2.configure(
                scrollregion=detectorsData2.bbox("all")
            )
        )
        detectorsData2.create_window(
            (0, 0), width=800, window=detectorsData, anchor="nw")

        gallery_data = db.get_galleries()

        for (id, name) in gallery_data:
            self.add_client_frame(detectorsData, id, name)

    def add_client_frame(self, frame, id, name):
        clientFrame = Frame(frame, height=120, width=800,
                            background="#fff", highlightbackground="black", highlightthickness=1)
        clientFrame.pack()
        clientFrame.pack_propagate(0)
        idLabel = Label(clientFrame, height=2,
                        text="Id:", font=("Helvetica", 19), bg="#fff")
        idLabel.pack(side=LEFT)
        idValLabel = Label(clientFrame,  height=2,
                           text=str(id), font=("Helvetica", 19), bg="#fff")
        idValLabel.pack(side=LEFT)
        nameLabel = Label(clientFrame,  height=2,
                          text=", Nazwa:", font=("Helvetica", 19), bg="#fff")
        nameLabel.pack(side=LEFT)
        nameValLabel = Label(clientFrame,  height=2,
                             text=str(name), font=("Helvetica", 19), bg="#fff")
        nameValLabel.pack(side=LEFT)
        detailsButton = Button(clientFrame, text="Szczegóły", font=("Helvetica", 20), height=1, width=12,
                               bg=self.color, command=(lambda: self.show_details(id)))
        detailsButton.pack(side=RIGHT, padx=30)
    # Creates status bar

    def utworz_status(self):
        self.statusbar = Label(self.parent, text="Linia statusu...",
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
        self.menubar = Menu(self.parent)
        self.parent["menu"] = self.menubar
        fileMenu = Menu(self.menubar)
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
        self.robocze = Frame(self.parent, background='#ffffff')
        self.robocze.grid(row=1, column=0, columnspan=1,
                          rowspan=1, sticky=NSEW)
        pass

    # szczegóły wybranej galerii
    def show_details(self, galery_id):

        rank_list = []
        top = Toplevel()

        top.geometry("1400x1000+204+118")
        top.resizable(width=False, height=False)
        title = Frame(top, height=100, background="#fff")
        title.pack(fill=X, expand=False)
        title.pack_propagate(0)
        titleVal = Label(title, height=4, text="Galeria handlowa Amber", font=(
            "Helvetica", 25), bg="#fff")
        titleVal.pack(fill=None, expand=False)

        detail_frame = Frame(top, height=800, width=1330,
                             background=self.color)
        detail_frame.pack(fill=None, expand=False)
        detail_frame.pack_propagate(0)

        detail_scroll = Scrollbar(detail_frame)
        detail_scroll.pack(side=RIGHT, fill=Y)

        details_table = ttk.Treeview(
            detail_frame, yscrollcommand=detail_scroll.set, height=800)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", font=("Helvetica", 12))
        style.configure("Treeview.Heading", background="#C0C0C0",
                        font=("Helvetica", 12,))

        details_table.pack()
        details_table.pack_propagate(0)
        detail_scroll.config(command=details_table.yview)

        details_table['columns'] = ('tmp_in', 'hum_in', 'light_in', 'tmp_out',
                                    'hum_out', "light_out", "wind", "windows", "lighting", "time")

        details_table.column("#0", width=0,  stretch=NO)
        details_table.column("tmp_in", anchor=CENTER, width=140)
        details_table.column("hum_in", anchor=CENTER, width=130)
        details_table.column("light_in", anchor=CENTER, width=150)
        details_table.column("tmp_out", anchor=CENTER, width=130)
        details_table.column("hum_out", anchor=CENTER, width=120)
        details_table.column("light_out", anchor=CENTER, width=150)
        details_table.column("wind", anchor=CENTER, width=100)
        details_table.column("windows", anchor=CENTER, width=120)
        details_table.column("lighting", anchor=CENTER, width=130)
        details_table.column("time", anchor=CENTER, width=140)

        details_table.heading("#0", text="", anchor=CENTER)
        details_table.heading("tmp_in", text="Temp. wewn. [*C]", anchor=CENTER)
        details_table.heading("hum_in", text="Wilg. wewn. [%]", anchor=CENTER)
        details_table.heading(
            "light_in", text="Jasnosć wewn. [lux]", anchor=CENTER)
        details_table.heading(
            "tmp_out", text="Temp. zewn. [*C]", anchor=CENTER)
        details_table.heading("hum_out", text="Wilg. zwen. [%]", anchor=CENTER)
        details_table.heading(
            "light_out", text="Jasnosć zewn. [lux]", anchor=CENTER)
        details_table.heading("wind", text="Wiatr [m/s]", anchor=CENTER)
        details_table.heading("windows", text="Stan okiennic", anchor=CENTER)
        details_table.heading(
            "lighting", text="Stan oświetlenia", anchor=CENTER)
        details_table.heading("time", text="Czas", anchor=CENTER)

        measurements = db.get_gallery_measurements(galery_id)
        print("test")
        # for i in measurements:
        #     details_table.insert(parent='', index='end', iid=i, text='',
        #                          values=('20.0', '25', '350', '5.4', '45', '150', '3', 'Zamknięte', 'Włączone', '12/10/2021 16:3'+str(i)))
