import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.eviron.get('SECRET_KEY')
    FLASKY_ADMIN = os.eviron.get('FLASKY_ADMIN')
    
    @staticmethod
    def init_app(app):
        pass
        
class DevelopmentConfig(Config):
    DEBUG=True
    

config={'default': DevelopmentConfig}