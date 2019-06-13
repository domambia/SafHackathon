# configurations 


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/mpesa"
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    DEBUG = True

class Developement(Config):
    pass 


class Deployment(Config):
    pass

    