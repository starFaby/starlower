from datetime import datetime
from flask import request, render_template as render, flash, redirect, url_for
from numpy import imag
from sqlalchemy import null
from app.database.database import *


class ControllerAdminFormulario:

    def controllerAdminFormularioList():
        formulario = Formulario.query.all()
        print(formulario)
        if formulario != []:
            flash('Formularios Listados', category='success')
            return render("admin/adminFormulario.html", formulario=formulario)
        else:
            flash('No existe categorias', category='success')
            return render("admin/adminFormulario.html", formulario=formulario)
        

    def onGetControllerAdminFormularioSave():
        nombre = request.form['txtNombre']
        image = request.form['txtImage']
        detalle = request.form['txtDetalle']
        url = request.form['txtUrl']
        estado = request.form['selectEstado']
        createdat = datetime.now().strftime('%x')
        userid = 1
        if nombre != '' and image != '' and detalle != '' and url != '' and estado != 'Elija...':
            newformulario = Formulario(nombre, image, detalle, url, estado, createdat, userid)
            db.session.add(newformulario)
            db.session.commit()
            flash('Guardado Correctamente', category='success')
            return redirect(url_for('adfrml.controllerAdminFormularioList'))
        else:
            flash('LLene los campos completos porfabor', category='success')
            return redirect(url_for('adfrml.controllerAdminFormularioList'))

    def onGetControllerAdminFormularioUpdate(id):
        formulario = Formulario.query.get(id)
        if request.method == 'POST':
            formulario.nombre = request.form['txtNombre']
            formulario.image = request.form['txtImage']
            formulario.detalle = request.form['txtDetalle']
            formulario.url = request.form['txtUrl']
            formulario.estado = request.form['selectEstado']
            if formulario.nombre != '' and formulario.image != '' and formulario.detalle != '' and formulario.url != '' and formulario.estado != 'Elija...':
                db.session.commit()
                flash('Datos Actualizados', category='success')
                return redirect(url_for('adfrml.controllerAdminFormularioList'))
            else:
                flash('Campos vacios llene porfabor', category='success')
                return redirect(url_for('adfrml.controllerAdminFormularioList'))

        return render("modal/modalAdminFormularioUpdate.html", formulario = formulario)
