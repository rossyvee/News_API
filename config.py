import os
from instance import config

API_KEY = config.API_KEY
NEWS_BASE_URL='https://newsapi.org/v2'


class Config:
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    '''
    dev
    '''
DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}