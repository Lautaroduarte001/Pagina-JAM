

class Enrollments():
    @classmethod
    def filter_instruments(self,db):
        instruments_per_song = {
            'cancion1':['Voz', 'Guitarra', 'Bajo', 'Bateria'],
            'cancion2':['Voz', 'Guitarra', 'Bajo', 'Bateria'],
            'cancion3':['Voz', 'Guitarra', 'Bajo', 'Bateria'],
            'cancion4':['Voz', 'Guitarra', 'Bajo', 'Bateria']
        }
        
        try:
            cursor = db.connection.cursor()
            sql = """SELECT song, instrument FROM inscripciones"""
            cursor.execute(sql)
            results = cursor.fetchall()

        except Exception as ex:
            raise Exception(ex)
        
        #Remove elements from dictionary if the song and instrument are in the table
        for song, instrument in results:
             if song in instruments_per_song and instrument in instruments_per_song[song]:
                instruments_per_song[song].remove(instrument)
        
        return instruments_per_song
    
    @classmethod
    def filter_songs(self, db, available_instruments):
        songs_list = {
            'cancion1': 'Tornado of Souls - Megadeth',
            'cancion2': 'Jump - EVH',
            'cancion3': 'Everlong - Foo Fighters',
            'cancion4': 'Smells Like Teen Spirit - Nirvana'
        }
        for song, instruments in available_instruments.items():
            if not instruments:
                if song in songs_list:
                    del songs_list[song]
        
        return songs_list
                    
                
    
    @classmethod
    def enroll_user(self, db, song, instrument, username):
        
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO inscripciones (song, instrument, username) VALUES (%s,%s,%s)"""
            cursor.execute(sql,(song, instrument, username))
            db.connection.commit()
            
        except Exception as ex:
            raise ex
        
        return "succes"
    
    
        

