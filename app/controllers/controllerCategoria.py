from flask import request, render_template as render
from app.database.database import *

class ControllerCategoria:

    def onGetControllerList():
        categorias = Categoria.query.all()
        return render('client/categoria.html', categorias=categorias)
       
    def onGetControllerListOne():
        pass

    def onGetControllerInsert():
        pass