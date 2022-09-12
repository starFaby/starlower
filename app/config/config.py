import os
class Config:
    SECRET_KEY = 'starfaby'
    #---------------------------------------
    #-------servicio local-------------
    #---------------------------------------
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/lawerstar'
    #---------------------------------------
    #-------servicio en la nube-------------
    #---------------------------------------
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://uez9l7gzjykxiueb:wKOaTSdauIOy9f5W9I7h@brjdc5b3vysmljkebacf-mysql.services.clever-cloud.com/brjdc5b3vysmljkebacf'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

