from datetime import datetime
from flask import request, render_template as render, flash, redirect, url_for
from flask_login import current_user
from app.database.database import *


class ControllerAdminUserCaso:

    def controllerAdminUserCasoList(page):
        page = page
        pages = 5
        userCasos = Usercaso.query.join(Caso, Usercaso.casoid == Caso.id).join(User , User.id == Usercaso.userid).add_columns(Usercaso.id, User.nombres, User.apellidos, Caso.nombre, Usercaso.avance, Usercaso.userid, Usercaso.createdat).filter(Usercaso.estado == 1).order_by(Caso.id.asc()).paginate(page, pages,error_out=False)
        
        if userCasos != []:
            if request.method == 'POST' and 'tag' in request.form:
                tag = request.form["tag"]
                search = "%{}%".format(tag)
                userCasos = Usercaso.query.join(Caso, Usercaso.casoid == Caso.id).join(User , User.id == Usercaso.userid).add_columns(Usercaso.id, User.nombres, User.apellidos, Caso.nombre, Usercaso.avance, Usercaso.userid, Usercaso.createdat).filter(Usercaso.estado == 1).filter(Caso.nombre.like(search)).paginate(per_page=pages,error_out=False)
                return render("admin/adminUserCaso.html", userCasos=userCasos, tag = tag)
            else:
                flash('Categorias Listadas', category='success')
                return render("admin/adminUserCaso.html", userCasos=userCasos)
        else:
            flash('No existe categorias', category='success')
            return render("admin/adminUserCaso.html", userCasos=userCasos)
        
    def onGetControllerAdminUserCasoUpdate(id):
        userCaso = Usercaso.query.get(id)
        if request.method == 'POST':
            userCaso.avance = request.form['txtAvance']
            if userCaso.avance != '':
                db.session.commit()
                flash('Datos Actualizados', category='success')
                return redirect(url_for('usca.controllerAdminUserCasoList'))
            else:
                flash('Campos vacios llene porfabor', category='success')
                return redirect(url_for('usca.controllerAdminUserCasoList'))

        return render("modal/modalAdminUserCasoUpdate.html", userCaso = userCaso)

    def onGetControllerAdminUserCasoDelete(id):
        if current_user.is_authenticated:
            usercaso = Usercaso.query.get(id)
            usercaso.estado = 0
            if usercaso.estado != '':
                db.session.commit()
                flash('Dato Eliminado', category='success')                  
                return redirect(url_for('usca.controllerAdminUserCasoList'))
            else:
                flash('Campos vacios llene porfabor', category='success')
                return redirect(url_for('usca.controllerAdminUserCasoList'))
        else:
            flash('Deve logiarse Primero', category='danger')
            return redirect(url_for("loginin.onGetLogin"))

    
