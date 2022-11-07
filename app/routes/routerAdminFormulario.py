from flask import Blueprint
from app.controllers.controllerAdminFormulario import ControllerAdminFormulario
adfrml= Blueprint('adfrml', __name__)
adfrml.route('/adfrml', methods=['GET', 'POST'], defaults={"page": 1})(ControllerAdminFormulario.controllerAdminFormularioList)
adfrml.route('/adfrml/<int:page>', methods=['GET', 'POST'])(ControllerAdminFormulario.controllerAdminFormularioList)
adfrml.route('/adfsave', methods=['POST'])(ControllerAdminFormulario.onGetControllerAdminFormularioSave)
adfrml.route('/upfrml/<id>', methods=['GET', 'POST'])(ControllerAdminFormulario.onGetControllerAdminFormularioUpdate)