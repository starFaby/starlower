from datetime import datetime
from flask import request, render_template as render, flash, redirect, url_for
from flask_login import current_user
from app.database.database import *

class ControllerUser:

    def controllerUsersList(page):
        page = page
        pages = 5
        users = User.query.order_by(User.id.asc()).paginate(page, pages,error_out=False)
        if users != []:
            if request.method == 'POST' and 'tag' in request.form:
                tag = request.form["tag"]
                search = "%{}%".format(tag)
                users = User.query.filter(User.cedula.like(search)).paginate(per_page=pages,error_out=False)
                return render("admin/adminUser.html", users=users, tag = tag)
            else:
                flash('Usuarios Listados', category='success') 
                return render("admin/adminUser.html", users = users)
        else:
            flash('No existe Usuarios', category='success')
            return render("admin/adminUser.html", users = users)
