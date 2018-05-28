from apiclient.discovery import build
from dime import Video
from dime import AbstractYoutube
import emoji

class AppYoutube(AbstractYoutube):
    def InfoVideo(self, url):

        API_KEY = 'AIzaSyAWrA1AR0ffrdvlPFF0Z5LhsJdfAFjhEPw'
        youtube = build('youtube', 'v3', developerKey=API_KEY)

        ids = url[32:43]
        results = youtube.videos().list(id=ids, part='snippet').execute()
        for result in results.get('items', []):
            NombreCanal = emoji.demojize(result['snippet']['channelTitle'])
            Titulo = emoji.demojize(result['snippet']['title'])
            Descripcion = emoji.demojize(result['snippet']['description'])
            Publicacion = result['snippet']['publishedAt']


        results1 = youtube.videos().list(id=ids, part='statistics').execute()
        for result2 in results1.get('items', []):
            Likes = result2['statistics']['likeCount']
            Vistas = result2['statistics']['viewCount']


        results4 = youtube.videos().list(id=ids, part='contentDetails').execute()
        for result5 in results4.get('items', []):
            Duracion = result5['contentDetails']['duration']

        return Video(Titulo, NombreCanal, Descripcion, Publicacion, Likes, Vistas, Duracion)

if __name__ == '__main__':
    y = AppYoutube()
    vid = y.InfoVideo('https://www.youtube.com/watch?v=L688sHqXL2A')

    print(vid.Nombre)
