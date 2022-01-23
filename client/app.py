
from tkinter import *
from Controllers.MainController import MainController
from Views.MainView import MainView
from Services.GalleryManagerService import GelleryManagerService
from BasicGui import BasicGui

LOOP_INTERVAL = 1_000

class App(BasicGui):
    
    def gallery(self):
        self.color = "SystemButtonFace"
        
        self.createLayout()
        
        
    def createLayout(self):
        Frame(self.robocze, height=90, background="#fff").grid(column=0, row=0, rowspan=1, columnspan=4)
        Frame(self.robocze, height=20, width=55, background="#fff").grid(column=0, row=1, rowspan=1)
        self.createLeftFrame()
        Frame(self.robocze, height=50, width=55, background="#fff").grid(column=2, row=1, rowspan=1)
        self.createRightFrame()
        
    
    def createLeftFrame(self):
        detectorsData = Frame(self.robocze, height=600, width=400, background=self.color, highlightbackground="black", highlightthickness=2)
        detectorsData.grid(column=1, row=1, rowspan=1)
        detectorsLabel = Label(detectorsData, width=25, height=1, text="Dane z czujników", font =("Helvetica", 25), bg="#fff")
        detectorsLabel.grid(row=0, column=0, columnspan=2)
        outDetectorsLabel = Label(detectorsData, width=25, height=1, text="Zewnętrzynych:", font =("Helvetica", 30), bg="#fff")
        outDetectorsLabel.grid(row=1, column=0, columnspan=1)

    def createRightFrame(self):
        pheripheralsData = Frame(self.robocze, height=600, width=400, background=self.color, highlightbackground="black", highlightthickness=2)
        pheripheralsData.grid(column=3, row=1, rowspan=1)

        
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
        print("test")

    def runLoop():
        loop()
        app.after(LOOP_INTERVAL, runLoop)

    app.after(LOOP_INTERVAL, runLoop)
    app.mainloop()
