from tkinter import *
from Controllers.MainController import MainController
from Views.MainView import MainView
from Services.GalleryManagerService import GelleryManagerService
from BasicGui import BasicGui

LOOP_INTERVAL = 1_000

class App(BasicGui):
    pass
    
        
if __name__ == '__main__':
    root = Tk()
    root.title("System monitorowania i kontroli środowiska galerii")
    app = App(master=root)
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

