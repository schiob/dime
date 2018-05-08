
import sqlite3
from dime import *

class SQlite(AbstractRepo):

    #conectar con bd
    def __init__(self):
        self.conexion = sqlite3.connect('dime.db')
        self.cursor = self.conexion.cursor()

    def GuardarVideo(self, video):
        # Insertar video
        v = (video.Nombre, video.Duracion, video.Canal, video.Fecha, video.Likes, video.Vistas, video.Descripcion)
        self.cursor.execute("INSERT INTO VIDEO (NOMBRE, DURACION,CANAL,FECHA,LIKES,VISTAS,DESCRIPCION) VALUES (?,?,?,?,?,?,?)", v)
        self.conexion.commit()#guarda cambios
        video.Id = self.cursor.lastrowid

        # Insertar categorias
        categorias = []
        if video.Categorias is not None:
            for cat in video.Categorias:
                categorias.append((video.Id, cat))
        if len(categorias) < 1:
            categorias.append((video.Id, "sin categoria"))
        self.cursor.executemany("INSERT INTO CATEGORIA (VIDEO_ID, NOMBRE) VALUES (?, ?)", categorias)
        self.conexion.commit()
        return video

    def MostrarLista(self):
        videos = []
        self.cursor.execute("SELECT * from VIDEO")
        for db_video in self.cursor.fetchall():
            video = Video(db_video[1], db_video[2], db_video[3], db_video[4], db_video[5], db_video[6], db_video[7], id=db_video[0], categorias=[])
            print(db_video)
            self.cursor.execute("SELECT * from CATEGORIA where VIDEO_ID=?", (str(video.Id),))
            for row in self.cursor.fetchall():
                print(row)
                video.Categorias.append(row[2])

            videos.append(video)

        return videos

    def MostrarVideo(self, id):
        self.cursor.execute("SELECT * from VIDEO where ID=?", str(id))
        db_video = self.cursor.fetchone()
        video = Video(db_video[1], db_video[2], db_video[3], db_video[4], db_video[5], db_video[6], db_video[7], id=db_video[0], categorias=[])

        self.cursor.execute("SELECT * from CATEGORIA where VIDEO_ID=?", (str(id),))
        for row in self.cursor.fetchall():
            video.Categorias.append(row[2])

        return video


    def ModificarVideo(self, video):
        t = (video.Nombre, video.Duracion, video.Canal, video.Fecha, video.Likes, video.Vistas, video.Descripcion, video.Id)
        self.cursor.execute("UPDATE VIDEO SET NOMBRE=?, DURACION=?, CANAL=?, FECHA=?, LIKES=?, VISTAS=?, DESCRIPCION=? where ID=?", t)
        self.conexion.commit()

        self.cursor.execute("DELETE from CATEGORIA where VIDEO_ID=?", (str(video.Id),))
        self.conexion.commit()
        # Insertar categorias
        categorias = []
        if video.Categorias is not None:
            for cat in video.Categorias:
                categorias.append((video.Id, cat))
        if len(categorias) < 1:
            categorias.append((video.Id, "sin categoria"))
        self.cursor.executemany("INSERT INTO CATEGORIA (VIDEO_ID, NOMBRE) VALUES (?, ?)", categorias)
        self.conexion.commit()
        return video


    def BorrarVideo(self, id_video):
        self.cursor.execute("DELETE from CATEGORIA where VIDEO_ID=?", (str(id_video),))
        self.cursor.execute("DELETE from VIDEO WHERE ID=?", (str(id_video),))
        self.conexion.commit()
        return True

    def Close(self):
        self.conexion.close()

if __name__ == '__main__':
    v = Video("nombre diferente", "13", "canal de prueba", "07/05/2018", 53, 100, "un videito chido", id=3, categorias=['una', 'y dos'])

    ana_db = SQlite()

    #Guardar video
    # db_video = ana_db.GuardarVideo(v)
    # print(db_video)

    # Get one video
    # video_de_query = ana_db.MostrarVideo(7)
    # print(video_de_query.Id)
    # print(video_de_query.Nombre)
    # print(video_de_query.Categorias)

    # ana_db.BorrarVideo(4)

    # ana_db.ModificarVideo(v)

    # Get All videos
    videos = ana_db.MostrarLista()
    for vid in videos:
        print(vid.Id, vid.Nombre, vid.Categorias)

    ana_db.Close()
