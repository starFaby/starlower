from datetime import datetime
from flask import request, render_template as render, flash, redirect, url_for
from sqlalchemy import null
from app.database.database import *

class ControllerCaso:

    def controllerCasoList(id):
        caso = Caso.query.filter(Caso.categoriaid == id)
        return render("client/casos.html", caso = caso)


    def onGetcontrollerCasoInsert():
        avance = 3
        estado = 1
        createdat = datetime.now().strftime('%x')
        userid = request.form['txtUserId']
        casoid = request.form['txtCasoId']
        
        if avance != '' and estado != '' and createdat != '' and userid != '' and casoid != '':
            newusercaso = Usercaso(avance, estado, createdat, userid, casoid)
            db.session.add(newusercaso)
            db.session.commit()
            flash('Caso Asignado Correctamente', category='success')
            return render("index.html")
        else:
            flash('Error al crear caso', category='danger')
            return render("index.html")
        

