from flask import Blueprint
from app.controllers.controllerAvances import ControllerAvances
avances= Blueprint('avances', __name__)
avances.route('/avances', methods=['GET','POST'])(ControllerAvances.controllerAvances)