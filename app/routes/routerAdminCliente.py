from flask import Blueprint
from app.controllers.controllerAdminClient import ControllerAdminClient
adcli= Blueprint('adcli', __name__)
adcli.route('/adcli/<id>', methods=['GET'])(ControllerAdminClient.controllerAdminClientList)
