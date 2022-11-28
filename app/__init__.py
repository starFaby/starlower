from flask import Flask
from flask_login import LoginManager
from .config.config import Config
from app.database.database import db, ma
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from app.routes.routerAuth import auth
from app.routes.routerAdminCategoria import adcate
from app.routes.routerLoginIn import loginin
from app.routes.routerLogout import logout
from app.routes.routerDataBase import createdb
from app.routes.routerStart import start
from app.routes.routerCategoria import categoria
from app.routes.routerCaso import caso
from app.routes.routerAvances import avances
from app.routes.routerQuienesSomos import qsomos
from app.routes.routerAdminCateCaso import adcaca
from app.routes.routerAdminUserCaso import usca
from app.routes.routerFormulario import frml
from app.routes.routerAdminFormulario import adfrml 
from app.routes.routerAdminUser import userall 
from app.routes.routerConsultas import consul 
from app.routes.routerAdminConsultas import adcons 
from app.routes.routerAdminCliente import adcli 
from app.middlewares.authLogin import UserModel

loginManager = LoginManager()
loginManager.loginView = 'auth.authLoginIn'

@loginManager.user_loader
def loadUser(username):
    return UserModel.get(username)

def apprun():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(auth)
    app.register_blueprint(createdb)
    app.register_blueprint(loginin)
    app.register_blueprint(logout)
    app.register_blueprint(adcate)
    app.register_blueprint(start)
    app.register_blueprint(categoria)
    app.register_blueprint(caso)
    app.register_blueprint(avances)
    app.register_blueprint(qsomos)
    app.register_blueprint(adcaca)
    app.register_blueprint(usca)
    app.register_blueprint(frml)
    app.register_blueprint(adfrml)
    app.register_blueprint(userall)
    app.register_blueprint(consul)
    app.register_blueprint(adcons)
    app.register_blueprint(adcli)
    loginManager.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    bootstrap = Bootstrap(app)
    fa = FontAwesome(app)
    return app



