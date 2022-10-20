from datetime import datetime
from flask import request, render_template as render, flash, redirect, url_for
from sqlalchemy import null
from app.database.database import *


class ControllerAdminCateCaso:

    def controllerAdminCateCasoList():
        print("listando catecaso")
        cateCaso = Caso.query.all()
        categorias = Categoria.query.all()
        if cateCaso != [] or categorias != []:
            flash('Categorias Listadas', category='success')
            return render("admin/adminCateCaso.html", cateCaso=cateCaso, categorias=categorias)
        else:
            flash('No existe categorias', category='success')
            return render("admin/adminCateCaso.html", cateCaso=cateCaso, categorias=categorias)

    def onGetControllerAdminCateCasoSave():
        nombre = request.form['txtNombre']
        image = request.form['txtImage']
        detalle = request.form['txtDetalle']
        estado = request.form['selectEstado']
        createdat = datetime.now().strftime('%x')
        categoriaid = request.form['selectCategoria']
        if nombre != '' and image != '' and detalle != '' and estado != 'Elija...' and categoriaid != 'Elija...':
            newcatecaso = Caso(nombre, image, detalle,
                               estado, createdat, categoriaid)
            db.session.add(newcatecaso)
            db.session.commit()
            flash('Guardado Correctamente', category='success')
            return redirect(url_for('adcaca.controllerAdminCateCasoList'))
        else:
            flash('LLene los campos completos porfabor', category='success')
            return redirect(url_for('adcaca.controllerAdminCateCasoList'))

    def onGetControllerAdminCateCasoUpdate(id):
        caso = Caso.query.get(id)
        categorias = Categoria.query.all()
        if request.method == 'POST':
            caso.nombre = request.form['txtNombre']
            caso.image = request.form['txtImage']
            caso.detalle = request.form['txtDetalle']
            caso.estado = request.form['selectEstado']
            caso.categoriaid = request.form['selectCategoria']
            if caso.nombre != '' and caso.image != '' and caso.detalle != '' and caso.estado != 'Elija...' and caso.categoriaid != 'Elija...':
                db.session.commit()
                flash('Datos Actualizados', category='success')
                return redirect(url_for('adcaca.controllerAdminCateCasoList'))
            else:
                flash('Campos vacios llene porfabor', category='success')
                return redirect(url_for('adcaca.controllerAdminCateCasoList'))

        return render("modal/modalAdminCateCasoUpdate.html", caso=caso, categorias=categorias)

    def onGetControllerAdminCateCasoDelete(id):
        caso = Caso.query.get(id)
        if caso.id >= 0:
            db.session.delete(caso)
            db.session.commit()
            flash('Categoria eliminada', category='danger')
            return redirect(url_for('adcaca.controllerAdminCateCasoList'))
        else:
            flash('Error en el servidor', category='danger')
            return redirect(url_for('adcaca.controllerAdminCateCasoList'))
