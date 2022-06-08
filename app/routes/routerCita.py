from flask import Blueprint
from app.controllers.controllerCita import ControllerCita
cita= Blueprint('cita', __name__)
cita.route('/cita', methods=['GET'])(ControllerCita.controllerCita)