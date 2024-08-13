from models.entities.User import User

class ModelUser():
    
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT user_id, username, password, fullname FROM users
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],User.check_password(row[2],user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT user_id, username, fullname, email, mobile_number FROM users
                    WHERE user_id = '{}'""".format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                logged_user=User(row[0],row[1], None, row[2],row[3],row[4])
                return logged_user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def check_existing_username(cls, db, username):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT user_id FROM users WHERE username = '{}'""".format(username)
            cursor.execute(sql)
            row = cursor.fetchone()
            return row is not None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def create_new_user(self, db, username, password, fullname, email, mobile_number, drepa_coins):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO users (username, password, fullname, email, mobile_number, drepa_coins) 
                    VALUES (%s,%s,%s,%s,%s,%s)
            """
            cursor.execute(sql,(username,password,fullname,email,mobile_number, drepa_coins))
            db.connection.commit()
            print("Succesfull Insert")
        except Exception as ex:
            raise Exception(ex)
