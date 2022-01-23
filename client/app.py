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
        title=Frame(self.robocze, height=90, background="#fff")
        title.grid(column=0, row=0, rowspan=1, columnspan=4)
        titleVal = Label(title, height=4, text="Galeria handlowa Amber", font =("Helvetica", 25), bg="#fff")
        titleVal.grid(row=3, column=0, columnspan=1)
        Frame(self.robocze, height=20, width=55, background="#fff").grid(column=0, row=1, rowspan=1)
        self.createLeftFrame()
        Frame(self.robocze, height=50, width=55, background="#fff").grid(column=2, row=1, rowspan=1)
        self.createRightFrame()
        
    
    def createLeftFrame(self):
        detectorsData = Frame(self.robocze, height=600, width=400, background=self.color, highlightbackground="black", highlightthickness=2)
        detectorsData.grid(column=1, row=1, rowspan=1)
        detectorsLabel = Label(detectorsData, width=15, height=3, text="Dane z czujników", font =("Helvetica", 15), bg=self.color)
        detectorsLabel.grid(row=0, column=0, columnspan=2)
        outDetectorsLabel = Label(detectorsData, width=20, height=2, text="Zewnątrz:", font =("Helvetica", 20), bg=self.color)
        outDetectorsLabel.grid(row=1, column=0, columnspan=2)
        outTempLabel = Label(detectorsData, width=15, height=2, text="Temperatura:", font =("Helvetica", 12), bg=self.color)
        outTempLabel.grid(row=2, column=0, columnspan=1)
        outTempValLabel = Label(detectorsData, width=15, height=2, text="0*C", font =("Helvetica", 12), bg=self.color)
        outTempValLabel.grid(row=2, column=1, columnspan=1)
        outHumLabel = Label(detectorsData, width=15, height=2, text="Wilgotność:", font =("Helvetica", 12), bg=self.color)
        outHumLabel.grid(row=3, column=0, columnspan=1)
        outHumValLabel = Label(detectorsData, width=15, height=2, text="32%", font =("Helvetica", 12), bg=self.color)
        outHumValLabel.grid(row=3, column=1, columnspan=1)
        outLightLabel = Label(detectorsData, width=15, height=2, text="Oświetlenie:", font =("Helvetica", 12), bg=self.color)
        outLightLabel.grid(row=4, column=0, columnspan=1)
        outLightValLabel = Label(detectorsData, width=15, height=2, text="250 lux", font =("Helvetica", 12), bg=self.color)
        outLightValLabel.grid(row=4, column=1, columnspan=1)
        outWindLabel = Label(detectorsData, width=15, height=2, text="Temperatura:", font =("Helvetica", 12), bg=self.color)
        outWindLabel.grid(row=5, column=0, columnspan=1)
        outWindValLabel = Label(detectorsData, width=15, height=2, text="0*C", font =("Helvetica", 12), bg=self.color)
        outWindValLabel.grid(row=5, column=1, columnspan=1)
        
        inDetectorsLabel = Label(detectorsData, width=20, height=2, text="Wewnątrz:", font =("Helvetica", 20), bg=self.color)
        inDetectorsLabel.grid(row=6, column=0, columnspan=2)
        inTempLabel = Label(detectorsData, width=15, height=2, text="Temperatura:", font =("Helvetica", 12), bg=self.color)
        inTempLabel.grid(row=7, column=0, columnspan=1)
        inTempValLabel = Label(detectorsData, width=15, height=2, text="23*C", font =("Helvetica", 12), bg=self.color)
        inTempValLabel.grid(row=7, column=1, columnspan=1)
        inHumLabel = Label(detectorsData, width=15, height=2, text="Wilgotność:", font =("Helvetica", 12), bg=self.color)
        inHumLabel.grid(row=8, column=0, columnspan=1)
        inHumValLabel = Label(detectorsData, width=15, height=2, text="20%", font =("Helvetica", 12), bg=self.color)
        inHumValLabel.grid(row=8, column=1, columnspan=1)
        inLightLabel = Label(detectorsData, width=15, height=2, text="Oświetlenie:", font =("Helvetica", 12), bg=self.color)
        inLightLabel.grid(row=9, column=0, columnspan=1)
        inLightValLabel = Label(detectorsData, width=15, height=2, text="500 lux", font =("Helvetica", 12), bg=self.color)
        inLightValLabel.grid(row=9, column=1, columnspan=1)
        
        Label(detectorsData, width=15, height=2, text="", font =("Helvetica", 12), bg=self.color).grid(row=10, column=1, columnspan=1)
        
        
        

    def createRightFrame(self):
        peripheralsData = Frame(self.robocze, height=600, width=400, background=self.color, highlightbackground="black", highlightthickness=2)
        peripheralsData.grid(column=3, row=1, rowspan=1)
        periphealsLabel = Label(peripheralsData, width=15, height=3, text="Kontrola", font =("Helvetica", 15), bg=self.color)
        periphealsLabel.grid(row=0, column=0, columnspan=2)
        lightningLabel = Label(peripheralsData, width=20, height=2, text="Oświetlenie:", font =("Helvetica", 20), bg=self.color)
        lightningLabel.grid(row=1, column=0, columnspan=2)
        lightningStateLabel = Label(peripheralsData, width=15, height=2, text="Stan:", font =("Helvetica", 12), bg=self.color)
        lightningStateLabel.grid(row=2, column=0, columnspan=1)
        lightningStateValLabel = Label(peripheralsData, width=15, height=2, text="Włączone", font =("Helvetica", 12), bg=self.color)
        lightningStateValLabel.grid(row=2, column=1, columnspan=1)
        lightningModeLabel = Label(peripheralsData, width=15, height=2, text="Tryb:", font =("Helvetica", 12), bg=self.color)
        lightningModeLabel.grid(row=3, column=0, columnspan=1)
        
        WindowsLabel = Label(peripheralsData, width=20, height=2, text="Okiennice:", font =("Helvetica", 20), bg=self.color)
        WindowsLabel.grid(row=4, column=0, columnspan=2)
        WindowsStateLabel = Label(peripheralsData, width=15, height=2, text="Stan:", font =("Helvetica", 12), bg=self.color)
        WindowsStateLabel.grid(row=5, column=0, columnspan=1)
        WindowsStateValLabel = Label(peripheralsData, width=15, height=2, text="Otwarte", font =("Helvetica", 12), bg=self.color)
        WindowsStateValLabel.grid(row=5, column=1, columnspan=1)
        WindowsModeLabel = Label(peripheralsData, width=15, height=2, text="Tryb:", font =("Helvetica", 12), bg=self.color)
        WindowsModeLabel.grid(row=6, column=0, columnspan=1)
        
        Label(peripheralsData, width=15, height=9, text="", font =("Helvetica", 12), bg=self.color).grid(row=7, column=1, columnspan=1)

        
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

