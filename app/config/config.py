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
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://starlower:*#0101star0101#*@starlower.mysql.pythonanywhere-services.com/starlower$default'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #---------------------------------------
    #-------estructura-------------
    #---------------------------------------
    #---------------app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://<mysql_username>:<mysql_password>@<mysql_host>:<mysql_port>/<mysql_db>'

