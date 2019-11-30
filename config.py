class Config:

    pass




class DevConfig(Config):
    Debug=True


class ProdConfig(Config):
    pass

config_options = {
    'production' : ProdConfig,
    'development' : DevConfig
}