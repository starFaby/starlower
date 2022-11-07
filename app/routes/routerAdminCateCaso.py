from flask import Blueprint
from app.controllers.controllerAdminCateCaso import ControllerAdminCateCaso
# admin - categoria - caso
adcaca= Blueprint('adcaca', __name__)
adcaca.route('/adcaca', methods=['GET', 'POST'], defaults={"page": 1})(ControllerAdminCateCaso.controllerAdminCateCasoList)
adcaca.route('/adcaca/<int:page>', methods=['GET', 'POST'])(ControllerAdminCateCaso.controllerAdminCateCasoList)
adcaca.route('/newcc', methods=['POST'])(ControllerAdminCateCaso.onGetControllerAdminCateCasoSave)
adcaca.route('/delcc/<id>', methods=['GET'])(ControllerAdminCateCaso.onGetControllerAdminCateCasoDelete)
adcaca.route('/upcc/<id>', methods=['GET', 'POST'])(ControllerAdminCateCaso.onGetControllerAdminCateCasoUpdate)

