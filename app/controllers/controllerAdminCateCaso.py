from datetime import datetime
from flask import request, render_template as render, flash, redirect, url_for
from sqlalchemy import null
from app.database.database import *


class ControllerAdminCateCaso:

    def controllerAdminCateCasoList():
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
            newcatecaso = Caso(nombre, image, detalle,estado, createdat, categoriaid)
            db.session.add(newcatecaso)
            db.session.commit()
            flash('Guardado Correctamente', category='success')
            return redirect(url_for('adcaca.controllerAdminCateCasoList'))
        else:
            flash('LLene los campos completos porfabor', category='success')
            return redirect(url_for('adcaca.controllerAdminCategoriaList'))

    def onGetControllerAdminCateCasoUpdate(id):
        categoria = Categoria.query.get(id)
        if request.method == 'POST':
            categoria.nombre = request.form['txtNombre']
            categoria.image = request.form['txtImage']
            categoria.detalle = request.form['txtDetalle']
            categoria.estado = request.form['selectEstado']
            if categoria.nombre != '' and categoria.image != '' and categoria.detalle != '' and categoria.estado != 'Elija...':
                db.session.commit()
                flash('Datos Actualizados', category='success')
                return redirect(url_for('adcate.controllerAdminCategoriaList'))
            else:
                flash('Campos vacios llene porfabor', category='success')
                return redirect(url_for('adcate.controllerAdminCategoriaList'))

        return render("modal/modalAdminCateUpdate.html", categoria = categoria)

    def onGetControllerAdminCateCasoDelete(id):
        categoria = Categoria.query.get(id)
        if categoria.id >= 0:
            db.session.delete(categoria)
            db.session.commit()
            flash('Categoria eliminada', category='danger')
            return redirect(url_for('adcate.controllerAdminCategoriaList'))
        else:
            flash('Error en el servidor', category='danger')
            return redirect(url_for('adcate.controllerAdminCategoriaList'))

    
