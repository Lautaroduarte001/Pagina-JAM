from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    
    def __init__(self, id, username,password,fullname="", email="",mobile_number="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
        self.mobile_number = mobile_number
        
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    
    @classmethod
    def create_hashed_password(self, password):
        hashed_password = generate_password_hash(password)
        return hashed_password
    