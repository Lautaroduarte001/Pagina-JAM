class Votes():
    @classmethod
    def votes_counter(cls, db):
        lista_canciones = {
            'cancion1': 'Tornado of Souls - Megadeth',
            'cancion2': 'Jump - EVH',
            'cancion3': 'Everlong - Foo Fighters',
            'cancion4': 'Smells Like Teen Spirit - Nirvana'
        }
        try:
            cursor = db.connection.cursor()
            sql = """SELECT song, COUNT(*) AS cantidad
                    FROM votaciones
                    GROUP BY song;"""
            cursor.execute(sql)

            # Crear un diccionario para almacenar los valores por canción
            valores_por_cancion = {}
            for row in cursor.fetchall():
                cancion_id, cantidad = row
                # Obtener el nombre de la canción a partir del diccionario
                nombre_cancion = lista_canciones.get(cancion_id, 'Canción desconocida')
                valores_por_cancion[nombre_cancion] = cantidad

            return valores_por_cancion

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def check_user_vote(self, db, username):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT * FROM votaciones WHERE username = '{}'""".format(username)
            cursor.execute(sql)
            voted_user = cursor.fetchone()
            if voted_user:
                return True
            else:
                return False
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def fetch_user_votes(self, db, username):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT * FROM votaciones WHERE username = '{}'""".format(username)
            cursor.execute(sql)
            voted_songs = [row[1] for row in cursor.fetchall()]
            return voted_songs

        except Exception as ex:
            raise Exception(ex)
        
        
    @classmethod
    def fetch_song_votes(self,db,song):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT votes FROM votaciones WHERE song = '{}' 
            """.format(song)
            cursor.execute(sql)
            row = cursor.fetchone()
            return row
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_song_vote(self,db,song,username):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO votaciones (song,username) VALUES (%s,%s) 
            """
            cursor.execute(sql,(song, username))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_user_vote(self,db,song,username):
        try:
            cursor = db.connection.cursor()
            sql = """DELETE FROM votaciones WHERE song = %s AND username = %s;
            """
            cursor.execute(sql,(song, username))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)