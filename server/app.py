import database as db

from tkinter import *
from Views.MainServerView import MainServerView

LOOP_INTERVAL = 500
if __name__ == '__main__':
    #db.create_database()
    root = Tk()
    root.title("System monitorowania środowisk galerii")

    view = MainServerView(root)

    def loop():
        print("main loop tick")

    def runLoop():
        loop()
        root.after(LOOP_INTERVAL, runLoop)

    root.after(LOOP_INTERVAL, runLoop)
    root.mainloop()