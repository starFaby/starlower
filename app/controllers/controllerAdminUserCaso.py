from datetime import datetime
from flask import request, render_template as render, flash, redirect, url_for
from sqlalchemy import null
from app.database.database import *


class ControllerAdminUserCaso:

    def controllerAdminUserCasoList():
        userCasos = Usercaso.query.join(Caso, Usercaso.casoid == Caso.id).join(User , User.id == Usercaso.userid).add_columns(Usercaso.id, User.nombres, User.apellidos, Caso.nombre, Usercaso.avance, Usercaso.createdat)
        if userCasos != []:
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



    
