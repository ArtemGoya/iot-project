import sqlite3
import time
import os


def create_database():
    if os.path.exists("iot.db"):
        os.remove("iot.db")
        print("An old database removed.")
    connection = sqlite3.connect("iot.db")
    cursor = connection.cursor()
    cursor.execute(""" CREATE TABLE galerie (
        Galeria_id INTEGER PRIMARY KEY,
        Nazwa TEXT
    )""")

    cursor.execute(""" CREATE TABLE pomiary (
        Pomiar_id INTEGER PRIMARY KEY,
        Galeria_id NOT NULL,
        Data_pomiaru DATE NOT NULL,
        TempWewn INTEGER,
        TempZewn INTEGER,
        WilgWewn INTEGER,
        WilgZewn INTEGER,
        JasnoscWewn INTEGER,
        jasnoscZewn INTEGER,
        OkienniceOtwarte BOOLEAN,
        OswietlenieWlaczone BOOLEAN,
        FOREIGN KEY(Galeria_id) REFERENCES galerie(Galeria_id)
    )""")

    connection.commit()
    connection.close()
    print("The new database created.")


if __name__ == "__main__":
    create_database()
