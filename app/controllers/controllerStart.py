from flask import request, render_template as render

class ControllerStart:

    def start():
       return render("index.html")