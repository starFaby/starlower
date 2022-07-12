import engineio
from flask import request, render_template as render, redirect, url_for
from flask_login import current_user
from sqlalchemy import select
from app.database.database import *

class ControllerAvances:

    def controllerAvances():
        
        if current_user.is_authenticated:
            iduser = current_user.iduser
            avances = Usercaso.query.join(Caso.query).filter(Usercaso.userid == iduser).filter(Caso.id == Usercaso.casoid)
            #avances = Usercaso.query.join(Caso.query.all())
            cas = Caso.query
            for item in avances:
                print(item.avance)
            return render("client/avances.html", avances = avances )
        else:
            return redirect(url_for("loginin.onGetLogin"))