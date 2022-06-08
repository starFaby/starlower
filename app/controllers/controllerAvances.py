from flask import request, render_template as render

class ControllerAvances:

    def controllerAvances():
       return render("client/avances.html")