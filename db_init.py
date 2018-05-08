#base de datos con sqlite3
#_AnaCazares_ = u"Proyecto"
import sqlite3

def main():
    conexion = sqlite3.connect('dime.db')
    cursor = conexion.cursor()

    #crear tabla VIDEO
    cursor.execute('''CREATE TABLE VIDEO
                    (ID integer PRIMARY KEY,
                    NOMBRE TEXT NOT NULL,
                    DURACION TEXT NOT NULL,
                    CANAL TEXT NOT NULL,
                    FECHA TEXT NOT NULL,
                    LIKES INTEGER NOT NULL,
                    VISTAS INTEGER NOT NULL,
                    DESCRIPCION TEXT NOT NULL)''')

    #crear tabla CATEGORIA
    cursor.execute('''CREATE TABLE CATEGORIA
                    (ID integer PRIMARY KEY,
                    VIDEO_ID INTEGER NOT NULL,
                    NOMBRE TEXT NOT NULL,
                    FOREIGN KEY (VIDEO_ID) REFERENCES VIDEO (ID))''')

    conexion.close()

if __name__ == "__main__":
    main()
