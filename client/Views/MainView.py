import tkinter as tk
from Services.GalleryManagerService import Swiatla, Okna


class MainView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def set_controller(self, controller):
        """
        Ustawiamy kontroler
        """
        self.controller = controller

    def on_select_light_mode(self):
        """
        Wywoływany przy wyborze opcji oświetlenia
        """
        # tu widok kontroluje
        self.controller.handle_lights_change_mode(Swiatla.WLACZONE)

    def on_select_window_mode(self):
        """
        Wywoływany przy wyborze opcji otwierania okien
        """
        self.controller.handle_window_chnage_mode(Okna.ZAMKNIETE)

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
