import sqlite3
import time
import os

if os.path.exists("iot.db"):
    os.remove("iot.db")
    print("An old database removed.")
        
connection = sqlite3.connect("iot.db")

def create_database():
    cursor = connection.cursor()
    cursor.execute(""" CREATE TABLE galerie (
        Galeria_id INTEGER PRIMARY KEY,
        Nazwa TEXT
    )""")

    cursor.execute(""" CREATE TABLE pomiary (
        Pomiar_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Galeria_id INTEGER NOT NULL,
        Data_pomiaru TEXT NOT NULL,
        TempWewn INTEGER,
        TempZewn INTEGER,
        WilgWewn INTEGER,
        WilgZewn INTEGER,
        JasnoscWewn INTEGER,
        jasnoscZewn INTEGER,
        wiatr INTEGER,
        OkienniceOtwarte BOOLEAN,
        OswietlenieWlaczone BOOLEAN,
        FOREIGN KEY(Galeria_id) REFERENCES galerie(Galeria_id)
    )""")

    connection.commit()
    print("The new database created.")


def get_gallery_measurements(galery_id: int):
    cursor = connection.cursor()
    cursor.execute("""
            SELECT * FROM pomiary
            WHERE Galeria_id = :id;
        """, {"id": galery_id})
    return cursor.fetchall()


def get_galleries():
    cursor = connection.cursor()
    cursor.execute("""
            SELECT * FROM galerie
        """)
    return cursor.fetchall()
    

def seed_database():
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO galerie VALUES (?,?);""",
                   (1, "Galeria Amber")
                   )
    cursor.execute("""INSERT INTO galerie VALUES (?,?);""",
                   (2, "Galeria Stonka")
                   )
    connection.commit()
    save_measure("1,15.0,55,900.0,5.0,18.4,55,250.0,True,True")
    save_measure("1,15.2,53,900.0,5.0,18.3,55,250.0,True,True")

    #0 str(GALLERY_ID) + "," +
    #1 str(temp_external) + "," +
    #2 str(hum_external) + "," +
    #3 str(light_external) + "," +
    #4 str(wind_external) + "," +
    #5 str(temp_internal) + "," +
    #6 str(hum_internal) + "," +
    #7 str(light_internal) + "," +
    #8 str(is_opened_windows) + "," +
    #9 str(is_light_on))

def save_measure(message: str):
    connection = sqlite3.connect("iot.db")
    parameters = (message.split(","))
    cursor = connection.cursor()
    cursor.execute("INSERT INTO pomiary VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?)",
                   (parameters[0],time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),parameters[5],parameters[1],
                    parameters[6],parameters[2],parameters[7],parameters[3],
                    parameters[4],eval(parameters[8]),eval(parameters[9])))
    connection.commit()
    connection.close()
    
    



if __name__ == "__main__":
    create_database()
