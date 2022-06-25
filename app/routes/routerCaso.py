from flask import Blueprint
from app.controllers.controllerCaso import ControllerCaso
caso= Blueprint('caso', __name__)
caso.route('/caso/<id>', methods=['GET'])(ControllerCaso.controllerCasoList)
# newcs = new caso
caso.route('/newcs', methods=['POST'])(ControllerCaso.onGetcontrollerCasoInsert) 