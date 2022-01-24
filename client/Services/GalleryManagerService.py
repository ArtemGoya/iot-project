from PhysicalPeriphery import *
from enum import Enum
#import Services.MqttClientService as mqtt_client

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
        self.__swiatla_wlaczone = False
        self.__okna_otwarte = False
        self.__tryb_swiatel = Swiatla.WYLOCZAONE
        self.__tryb_okien = Okna.ZAMKNIETE

        self.__maksymalna_jasnosc_w_srodku = 300
        self.__minimalna_jasnosc_w_srodku = 200

        self.__max_wiatr = 10  # maxymalny wiatr przy jamim można otworzyć okna
        # minimalna temperatura zewn przy jakiej można otwierać okna
        self.__min_temperatura_zewn = 0
        # docelowa temperatura utrzymywana w pomieszczeniu
        self.__temperatura_docelowa = 21
        self.__wilg_docelowa = 60  # docelowa wilgotność utrzymywana w pomieszczeniu

    def get_okna_otwarte(self) -> bool:
        return self.__okna_otwarte

    def get_tryb_okien(self) -> Okna:
        return self.__tryb_okien

    def set_tryb_okien(self, value):
        if value == Okna.OTWARTE:
            set_windows(otwarte=True)
            self.__okna_otwarte = True
        elif value == Okna.ZAMKNIETE:
            set_windows(otwarte=False)
            self.__okna_otwarte = False
        self.__tryb_okien = value

    def get_swiatla_wlaczone(self) -> bool:
        return self.__swiatla_wlaczone

    def get_tryb_swiatel(self) -> Swiatla:
        return self.__tryb_swiatel

    def set_tryb_swiatel(self, value):
        if value == Swiatla.WLACZONE:
            set_light(wlaczone=True)
            self.__swiatla_wlaczone = True
        elif value == Swiatla.WYLOCZAONE:
            set_light(wlaczone=False)
            self.__swiatla_wlaczone = False
        self.__tryb_swiatel = value

    def subscribe_state_changded(self, callback):
        self.callbacks.append(callback)

    def loop(self):
        """
        tu poleci logika zarzadania peryferiami
        """
        print("Galeryy menager loop")

        in_temperatura, in_wilgotnosc, in_jasnosc = get_internal_sensors_data()
        out_temperatura, out_wilgotnosc, out_wiatr, out_jasnosc = get_external_sensors_data()

        # logika automatycznego wł/wył świateł
        if self.__tryb_swiatel == Swiatla.AUTO:
            if self.__swiatla_wlaczone == True and self.__maksymalna_jasnosc_w_srodku < in_jasnosc:
                set_light(wlaczone=False)
                self.__swiatla_wlaczone = False
            elif self.__minimalna_jasnosc_w_srodku > in_jasnosc:
                set_light(wlaczone=True)
                self.__swiatla_wlaczone = True

        # logika otwierania/zamykania okiennic
        if self.__tryb_okien == Okna.AUTO:
            # warunki zamknięcia okna
            if self.__okna_otwarte == True and (                                # gdy okna są otwarte i
                    # wiatr jest za silny
                    self.__max_wiatr < out_wiatr
                    # lub temperatura zewn jest za niska
                    or self.__min_temperatura_zewn < out_temperatura
                    # temperatura wewn jest niższa od docelowej
                    or self.__temperatura_docelowa > in_temperatura
                    # i temperatura na zewnątrz jest niższa niż w środku
                    and out_temperatura < in_temperatura
                    # to samo dla wilgotności
                    or self.__wilg_docelowa > in_wilgotnosc
                    and out_wilgotnosc < in_wilgotnosc
            ):
                set_windows(otwarte=False)
                self.__okna_otwarte = False
            # w innym wypadku staramy się trzymać okna otwarte
            elif self.__okna_otwarte == False:
                set_light(wlaczone=True)
                self.__swiatla_wlaczone = True

        # mozna tu wysylac dane przez mqtt

        for fn in self.callbacks:
            fn()
