import database as db
import MqttReceiver

from tkinter import *
from Views.MainServerView import MainServerView

LOOP_INTERVAL = 3000

if __name__ == '__main__':
    #db.create_database()
    root = Tk()
    root.title("System monitorowania środowisk galerii")

    db.create_database()
    db.seed_database()

    view = MainServerView(root)
    MqttReceiver.run_receiver()

    def loop():
        # print("main loop tick")
        view.update_data()
        pass

    def runLoop():
        loop()
        root.after(LOOP_INTERVAL, runLoop)

    root.after(LOOP_INTERVAL, runLoop)
    root.mainloop()
