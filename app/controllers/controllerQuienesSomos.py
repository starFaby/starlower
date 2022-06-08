from flask import request, render_template as render

class ControllerQuienesSomos:

    def controllerQuienesSomos():
       return render("client/quienesSomos.html")