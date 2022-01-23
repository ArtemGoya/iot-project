
from PhysicalPeriphery import *
from enum import Enum
import Services.MqttClientService as mqtt_client

# tryby otwarcia okna


class Okna(Enum):
    OTWARTE = 1
    ZAMKNIETE = 2
    AUTO = 3

# tryb pracy swiatel


class Swiatla(Enum):
    WLACZONE = 1
    WYLOCZAONE = 2
    AUTO = 3


class GelleryManagerService():
    """
    Klasa będzie zarzącać peryferiami raspbbery pi
    a takrze przechowywac dane o ich stanie
    """

    def __init__(self):
        self.callbacks = []

    def get_light_mode():
        pass

    def get_window_mode():
        pass

    def subscribe_state_changded(self, callback):
        self.callbacks.append(callback)

    def loop(self):
        """
        tu poleci logika zarzadania peryferiami
        """
        print("test service")
        for fn in self.callbacks:
            fn()
