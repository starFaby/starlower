from flask import Blueprint
from app.controllers.controllerAdminConsultas import ControllerAdminConsultas
adcons= Blueprint('adcons', __name__)
adcons.route('/adcons', methods=['GET', 'POST'], defaults={"page": 1})(ControllerAdminConsultas.onGetAdminConsultas)
adcons.route('/adcons/<int:page>', methods=['GET', 'POST'])(ControllerAdminConsultas.onGetAdminConsultas)
adcons.route('/adcoup/<id>', methods=['GET','POST'])(ControllerAdminConsultas.controllerAdminClientUpdate)
adcons.route('/adcode/<id>', methods=['GET','POST'])(ControllerAdminConsultas.controllerAdminClientDelete)

