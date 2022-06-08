from flask import request, render_template as render

class ControllerCaso:

    def controllerCaso():
       return render("client/casos.html")