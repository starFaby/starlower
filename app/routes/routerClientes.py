from flask import Blueprint
from app.controllers.controllerClientes import ControllerClientes
clients= Blueprint('clients', __name__)
clients.route('/clients/<id>', methods=['GET'])(ControllerClientes.controllerClientsList)