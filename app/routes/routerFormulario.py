from flask import Blueprint
from app.controllers.controllerFormularios import ControllerFormulario
frml= Blueprint('frml', __name__)
frml.route('/frml', methods=['GET'])(ControllerFormulario.controllerFormularioList)