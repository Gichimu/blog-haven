import os

class Config:
    '''
    The parent config class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'gysh'

    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS =  True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
class DevConfig(Config):
    '''
    The child config class that defines the default settings for the development environment
    '''
    Debug=True


class ProdConfig(Config):
    '''
    The child configuration class that defines the settings for the production environment
    '''
    pass

config_options = {
    'production' : ProdConfig,
    'development' : DevConfig
}