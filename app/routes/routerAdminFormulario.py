from flask import Blueprint
from app.controllers.controllerAdminFormulario import ControllerAdminFormulario
adfrml= Blueprint('adfrml', __name__)
adfrml.route('/adfrml', methods=['GET'])(ControllerAdminFormulario.controllerAdminFormularioList)
adfrml.route('/adfrml', methods=['POST'])(ControllerAdminFormulario.onGetControllerAdminFormularioSave)
adfrml.route('/adfrml/<id>', methods=['GET', 'POST'])(ControllerAdminFormulario.onGetControllerAdminFormularioUpdate)