from flask import request, render_template as render

class ControllerCita:

    def controllerCita():
       return render("client/citas.html")