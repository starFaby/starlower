from flask import Blueprint
from app.controllers.controllerQuienesSomos import ControllerQuienesSomos
qsomos= Blueprint('qsomos', __name__)
qsomos.route('/qsomos', methods=['GET'])(ControllerQuienesSomos.controllerQuienesSomos)