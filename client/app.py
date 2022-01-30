from tkinter import *
from Controllers.MainController import MainController
from Views.MainView import MainView
from Services.GalleryManagerService import GelleryManagerService

LOOP_INTERVAL = 500


if __name__ == '__main__':
    root = Tk()
    root.title("System monitorowania i kontroli środowiska galerii")
    galery_manager = GelleryManagerService()

    view = MainView(root)
    controller = MainController(view, galery_manager)
    view.set_controller(controller)

    def loop():
        galery_manager.loop()
        print("main loop tick")

    def runLoop():
        loop()
        root.after(LOOP_INTERVAL, runLoop)

    root.after(LOOP_INTERVAL, runLoop)
    root.mainloop()
