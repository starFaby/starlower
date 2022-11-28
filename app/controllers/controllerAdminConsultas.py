from datetime import datetime
from flask import request, render_template as render, flash, redirect, url_for
from app.database.database import *


class ControllerAdminConsultas:

    def onGetAdminConsultas(page):
        page = page
        pages = 5
        userConsul = Consulta.query.join(User , User.id == Consulta.userid).add_columns(Consulta.id, Consulta.fecha ,Consulta.hora, Consulta.detalle , Consulta.atendido ,Consulta.userid, User.nombres, User.apellidos).filter(Consulta.estado == 1).order_by(Consulta.id.asc()).paginate(page, pages,error_out=False)
        if userConsul != []:
            if request.method == 'POST' and 'tag' in request.form:
                tag = request.form["tag"]
                anio = tag[0:4]
                mes = tag[5:7]
                dia = tag[8:10]
                aux = f"{dia}/{mes}/{anio}"
                search = "%{}%".format(aux)
                userConsul = Consulta.query.join(User , User.id == Consulta.userid).add_columns(Consulta.id, Consulta.fecha ,Consulta.hora, Consulta.detalle ,Consulta.userid, User.nombres, User.apellidos).filter(Consulta.estado == 1).order_by(Consulta.id.asc()).filter(Consulta.fecha.like(search)).paginate(page, pages,error_out=False)
                return render("admin/adminConsultas.html", userConsul = userConsul)
            else:
                flash('Consultas Listadas', category='success')
                
                return render("admin/adminConsultas.html", userConsul=userConsul)
        else:
            flash('No Existe Consultas', category='success')
            return render("admin/adminConsultas.html", userConsul=userConsul)

    def controllerAdminClientUpdate(id):
        consul = Consulta.query.get(id)
        consul.atendido = "si"
        if consul.atendido != '':
            db.session.commit()
            flash('Datos Actualizados', category='success')
            return redirect(url_for('adcons.onGetAdminConsultas'))
        else:
            flash('Campos vacios llene porfabor', category='success')
            return redirect(url_for('adcons.onGetAdminConsultas'))


    def controllerAdminClientDelete(id):
        consul = Consulta.query.get(id)
        consul.estado = 0
        if consul.estado != '':
            db.session.commit()
            flash('Datos Actualizados', category='success')
            return redirect(url_for('adcons.onGetAdminConsultas'))
        else:
            flash('Campos vacios llene porfabor', category='success')
            return redirect(url_for('adcons.onGetAdminConsultas'))