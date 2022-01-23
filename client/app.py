import tkinter as tk
from Controllers.MainController import MainController
from Views.MainView import MainView
from Services.GalleryManagerService import GelleryManagerService

LOOP_INTERVAL = 1_000


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gallery Controler")


if __name__ == '__main__':
    app = App()

    galery_manager = GelleryManagerService()

    view = MainView(app)
    controller = MainController(view, galery_manager)
    view.set_controller(controller)

    def loop():
        galery_manager.loop()
        print("main loop tick")

    def runLoop():
        loop()
        app.after(LOOP_INTERVAL, runLoop)

    app.after(LOOP_INTERVAL, runLoop)
    app.mainloop()
