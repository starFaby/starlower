from flask import Blueprint
from app.controllers.controllerStart import ControllerStart
start= Blueprint('start', __name__)
start.route('/start', methods=['GET'])(ControllerStart.start)