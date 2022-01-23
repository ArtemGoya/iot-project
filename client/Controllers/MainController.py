from Services.GalleryManagerService import GelleryManagerService


class MainController():

    def __init__(self, view, galery_manager: GelleryManagerService):
        self.view = view
        self.galery_manager = galery_manager
        # uwaga prawwdopodobne wykrzaczenie
        galery_manager.subscribe_state_changded(
            self.notify_gamlery_manager_state_changed)


    def notify_gamlery_manager_state_changed(self):
        """
        Metoda wywoływana gdy zaktualizowal sie stan galerii
        """
        print("Jestem w konrolerze")
        pass
