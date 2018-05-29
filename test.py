from dime import *
																																																																																																																																																															from ana_db import SQlite
from raul_youtube import AppYoutube
from time import sleep
import unittest
from unittest.mock import Mock 

class TestYouTube(unittest.TestCase):

	def setUp(self):
		self.yt = AppYoutube()
		self.videomock = Mock(Id = 12, Nombre = "Ed Sheeran - Thinking Out Loud - Español - Yo antes de Ti", Duracion = "PT4M51S", Canal = "wasted girly.",  Fecha= "2017-03-22T19:48:45.000Z", Likes = self.yt.InfoVideo("https://www.youtube.com/watch?v=UFBgl3h0pXY").Likes, Vistas = self.yt.InfoVideo("https://www.youtube.com/watch?v=UFBgl3h0pXY").Vistas, Descripcion ='Cancion Thinking Out Loud en español by Ed Sheeran\nEspero que les guste :) :heart_suit:')
		self.video = Video(self.videomock.Nombre,self.videomock.Duracion,self.videomock.Canal,self.videomock.Fecha,self.videomock.Likes,self.videomock.Vistas,self.videomock.Descripcion)
		self.sql = SQlite()
		self.sql.GuardarVideo(self.video)
		#self.sql.MostrarLista(self)

		self.video1 = Video('uno',13,'lunes', "28 mayo 2018", 5000, 10000,'mal video')
	def tearDown(self):
		pass

	def test_Video(self):
		print("test_Video")
		self.assertEqual(self.video1.Nombre, ('uno'))
		self.assertEqual(self.video1.Duracion, 13 )
		self.assertEqual(self.video1.Canal, 'lunes' )
		self.assertEqual(self.video1.Fecha, "28 mayo 2018" )
		self.assertEqual(self.video1.Likes, 5000 )
		self.assertEqual(self.video1.Vistas, 10000 )
		self.assertEqual(self.video1.Descripcion, 'mal video' )

		self.assertNotEqual(self.video1.Nombre, ('dos'))
		self.assertNotEqual(self.video1.Duracion, 0 )
		self.assertNotEqual(self.video1.Canal, '' )
		self.assertNotEqual(self.video1.Fecha, '8' )
		self.assertNotEqual(self.video1.Likes, "!!" )
		self.assertNotEqual(self.video1.Vistas, 10 )
		self.assertNotEqual(self.video1.Descripcion, 'buen video' )


	def test_GuardarVideo(self):
		print("test_guardar")
		#self.assertNotEqual(self.GuardarVideo(self.yt,self.sql,"https://www.youtube.com/watch?v=UFBgl3h0pXY"),155)
		self.assertIsInstance(self.sql.GuardarVideo(self.video), Video)

	def test_Muestra(self):
		print("test_Mostrar")
		#self.assertIsInstance(self.sql.MostrarLista(12),Video)
if __name__ == '__main__':
	unittest.main() 
