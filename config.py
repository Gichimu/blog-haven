class Config:

    QUOTE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'




class DevConfig(Config):
    Debug=True


class ProdConfig(Config):
    pass

config_options = {
    'production' : ProdConfig,
    'development' : DevConfig
}