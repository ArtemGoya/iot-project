import tkinter as tk


class MainView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def set_controller(self, controller):
        """
        Ustawiamy kontroler
        """
        self.controller = controller

    def on_select_light_mode():
        """
        Wywoływany przy wyborze opcji oświetlenia
        """
        pass

    def on_select_window_mode():
        """
        Wywoływany przy wyborze opcji otwierania okien
        """
        pass

    def set_sensors_data():
        """
        Sluzy do aktualizacji na widoku informacji o stanie czujnikow
        """
