import engineio
from flask import request, render_template as render, redirect, url_for, flash
from flask_login import current_user
from app.database.database import *

class ControllerAvances:

    def controllerAvances():
        
        if current_user.is_authenticated:
            iduser = current_user.iduser
            avances = Usercaso.query.join(Caso, Usercaso.casoid == Caso.id).add_columns(Usercaso.avance, Caso.nombre).filter(Usercaso.userid == iduser)
            if avances.count() != 0:
                flash('Avances Listados', category='success')
                return render("client/avances.html", avances = avances )
            else :
                flash('Aun no has elegido un caso ', category='info')
                return render("client/avances.html", avances = avances )
        else:
            flash('Deve logiarse Primero', category='danger')
            return redirect(url_for("loginin.onGetLogin"))