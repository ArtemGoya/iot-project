from graphviz import view
from Services.GalleryManagerService import GelleryManagerService, Okna, Swiatla
from Views.MainView import MainView
from PhysicalPeriphery import *


class MainController():

    def __init__(self, view: MainView, galery_manager: GelleryManagerService):
        self.view = view
        self.galery_manager = galery_manager
        galery_manager.subscribe_state_changded(
            self.__notify_gamlery_manager_state_changed)

    def handle_window_chnage_mode(self, mode: Okna):
        pass

    def handle_lights_change_mode(self, mode: Swiatla):
        pass

    def __notify_gamlery_manager_state_changed(self):
        """
        Metoda wywoływana gdy zaktualizowal sie stan galerii
        """
        in_temperatura, in_wilgotnosc, in_jasnosc = get_internal_sensors_data()
        out_temperatura, out_wilgotnosc, out_wiatr, out_jasnosc = get_external_sensors_data()

        self.view.set_sensors_data(
            in_temperatura, in_wilgotnosc, in_jasnosc,
            out_temperatura, out_wilgotnosc, out_wiatr, out_jasnosc,
            self.galery_manager.get_okna_otwarte(),
            self.galery_manager.get_swiatla_wlaczone()
        )

        print("Jestem w konrolerze")
