from flask import Blueprint
from app.controllers.controllerAdminUserCaso import ControllerAdminUserCaso
usca= Blueprint('usca', __name__)
usca.route('/usca', methods=['GET', 'POST'], defaults={"page": 1})(ControllerAdminUserCaso.controllerAdminUserCasoList)
usca.route('/usca/<int:page>', methods=['GET', 'POST'])(ControllerAdminUserCaso.controllerAdminUserCasoList)
usca.route('/updat/<id>', methods=['GET', 'POST'])(ControllerAdminUserCaso.onGetControllerAdminUserCasoUpdate)
usca.route('/deluc/<id>', methods=['GET'])(ControllerAdminUserCaso.onGetControllerAdminUserCasoDelete)

