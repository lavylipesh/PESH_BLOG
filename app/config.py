import os
class Config:
    #QUOTES_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json '
    SECRET_KEY='2wnd56mdj6hcmnc7cxn'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lilibeth:1234@localhost/quotes'
    SQLALCHEMY_TRACK_MODIFICATIONS = True 
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):

    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):

    DEBUG = True
