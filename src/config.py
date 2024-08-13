class Config:
    SECRET_KEY = 'B!1we6g745*67ld8sg4645%^^'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456789'
    MYSQL_DB = 'jam'
    
config = {
    'development':DevelopmentConfig
}
