class Config:
    '''
    The parent config class
    '''




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