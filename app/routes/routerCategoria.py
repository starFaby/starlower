from flask import Blueprint
from app.controllers.controllerCategoria import ControllerCategoria
categoria= Blueprint('categoria', __name__)
categoria.route('/categoria', methods=['GET'])(ControllerCategoria.onGetControllerList)