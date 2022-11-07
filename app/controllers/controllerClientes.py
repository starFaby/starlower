from datetime import datetime
from flask import request, render_template as render, flash, redirect, url_for
from flask_login import current_user
from app.database.database import *


class ControllerClientes:

    def controllerClientsList(id):
        if current_user.is_authenticated:
            user = User.query.get(id)
            if user != []:
                flash('Usuarios Listadas', category='success')
                return render("client/clientes.html", user=user)
            else:
                flash('No existe Usuarios', category='success')
                return render("client/clientes.html", user=user)

        else:
            flash('Deve logiarse Primero', category='danger')
            return redirect(url_for("loginin.onGetLogin"))


    