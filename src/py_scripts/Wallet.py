class Wallet():
    @classmethod
    def check_drepa_coins(self,db,username):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT drepa_coins FROM users WHERE username = '{}' 
            """.format(username)
            cursor.execute(sql)
            row = cursor.fetchone()
            return row
        except Exception as ex:
            raise Exception(ex)
    
    