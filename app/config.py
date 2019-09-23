import os
class Config:
    #QUOTES_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json '
    SECRET_KEY='2wnd56mdj6hcmnc7cxn'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lilibeth:1234@localhost/quotes'
    SQLALCHEMY_TRACK_MODIFICATIONS = True 

class ProdConfig(Config):

    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):

    DEBUG = True
