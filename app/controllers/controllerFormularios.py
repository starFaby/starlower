from datetime import datetime
from flask import request, render_template as render, flash, redirect, url_for
from sqlalchemy import null
from app.database.database import *


class ControllerFormulario:

    def controllerFormularioList():
        formulario = Formulario.query.all()
        if formulario != []:
            flash('Formularios Listados', category='success')
            return render("client/formularios.html", formulario=formulario)
        else:
            flash('No existe categorias', category='success')
            return render("client/formularios.html", formulario=formulario)
        
    


    
