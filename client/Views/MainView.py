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

    def set_sensors_data(self,
                         in_temperatura: float, in_wilgotnosc: float, in_jasnosc: float,
                         out_temperatura: float, out_wilgotnosc: float,
                         out_wiatr: float, out_jasnosc: float,
                         okna_otwarte: bool, swiatla_wlaczone: bool
                         ):
        """
        Sluzy do aktualizacji na widoku informacji o stanie czujnikow
        """
        pass
