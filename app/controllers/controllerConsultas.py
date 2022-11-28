from datetime import datetime
from flask import request, render_template as render, flash, redirect, url_for
from flask_login import current_user
from app.database.database import *


class ControllerConsultas:
    def onGetConsultas(page):
        page = page
        pages = 5
        if current_user.is_authenticated:
            userid = current_user.iduser
            consult = Consulta.query.order_by(Consulta.id.asc()).filter(Consulta.estado == 1).filter(Consulta.userid == userid).paginate(page, pages,error_out=False)
            if consult != []:
                if request.method == 'POST' and 'tag' in request.form:
                    tag = request.form["tag"]
                    anio = tag[0:4]
                    mes = tag[5:7]
                    dia = tag[8:10]
                    aux = f"{dia}/{mes}/{anio}"
                    search = "%{}%".format(aux)
                    consult = Consulta.query.filter(Consulta.fecha.like(search)).filter(Consulta.estado == 1).filter(Consulta.userid == userid).paginate(per_page=pages,error_out=False)
                    return render("client/consultas.html", consult=consult, tag = tag)
                else:
                    return render("client/consultas.html", consult=consult)
            else:
                flash('No Existe Consultas', category='info')
                return render("client/consultas.html", consult=consult)
            
        else:
            flash('Deve logiarse Primero', category='danger')
            return redirect(url_for("loginin.onGetLogin"))

    def onGetConsultasSave():
        
        fecha = request.form['txtDate']
        hora = request.form['txtHora']
        detalle = request.form['txtDetalle']
        atendido = "no"

        save = True

        if fecha != '' and hora != '' and detalle != '':
            anio = fecha[0:4]
            mes = fecha[5:7]
            dia = fecha[8:10]
            fechafin = f"{dia}/{mes}/{anio}"
            estado = 1
            createdat = datetime.now().strftime('%d/%m/%Y')
            userid = current_user.iduser
            consult = Consulta.query.filter(Consulta.fecha == fechafin)
            for item in consult:
                if fechafin == item.fecha or fechafin != item.fecha:
                    if hora != item.hora:
                        save = True
                        break
                    else:
                        save = False
                        break
            if save:
                newConsulta = Consulta(fechafin, hora , detalle, atendido, estado,createdat, userid)
                db.session.add(newConsulta)
                db.session.commit()
                flash('Consulta Asignada', category='success')
                return redirect(url_for("consul.onGetConsultas")) 
            else:
                flash('Ya existe la Hora', category='success')
                return redirect(url_for("consul.onGetConsultas")) 
        else:
            flash('Datos Vacios', category='danger')
            return redirect(url_for("consul.onGetConsultas"))
