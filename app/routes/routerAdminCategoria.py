from flask import Blueprint
from app.controllers.controllerAdminCategoria import ControllerAdminCategoria
adcate= Blueprint('adcate', __name__)
adcate.route('/adcate', methods=['GET'])(ControllerAdminCategoria.controllerAdminCategoriaList)
adcate.route('/new', methods=['POST'])(ControllerAdminCategoria.onGetControllerAdminCategoriaSave)
adcate.route('/delete/<id>', methods=['GET'])(ControllerAdminCategoria.onGetControllerAdminCategoriaDelete)
adcate.route('/update/<id>', methods=['GET', 'POST'])(ControllerAdminCategoria.onGetControllerAdminCategoriaUpdate)

