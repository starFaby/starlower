from flask import Blueprint
from app.controllers.controllerConsultas import ControllerConsultas
consul= Blueprint('consul', __name__)
consul.route('/consul', methods=['GET', 'POST'], defaults={"page": 1})(ControllerConsultas.onGetConsultas)
consul.route('/consul/<int:page>', methods=['GET', 'POST'])(ControllerConsultas.onGetConsultas)
consul.route('/cssave', methods=['POST'])(ControllerConsultas.onGetConsultasSave)
