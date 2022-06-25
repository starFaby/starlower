from flask import Blueprint
from app.controllers.controllerAdminCateCaso import ControllerAdminCateCaso
# admin - actegoria - caso
adcaca= Blueprint('adcaca', __name__)
adcaca.route('/adcaca', methods=['GET'])(ControllerAdminCateCaso.controllerAdminCateCasoList)
adcaca.route('/newcc', methods=['POST'])(ControllerAdminCateCaso.onGetControllerAdminCateCasoSave)
#adcaca.route('/delete/<id>', methods=['GET'])(ControllerAdminCategoria.onGetControllerAdminCategoriaDelete)
#adcaca.route('/update/<id>', methods=['GET', 'POST'])(ControllerAdminCategoria.onGetControllerAdminCategoriaUpdate)

