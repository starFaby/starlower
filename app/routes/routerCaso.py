from flask import Blueprint
from app.controllers.controllerCaso import ControllerCaso
caso= Blueprint('caso', __name__)
caso.route('/caso', methods=['GET'])(ControllerCaso.controllerCaso)