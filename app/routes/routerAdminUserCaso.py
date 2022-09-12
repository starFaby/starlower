from flask import Blueprint
from app.controllers.controllerAdminUserCaso import ControllerAdminUserCaso
usca= Blueprint('usca', __name__)
usca.route('/usca', methods=['GET'])(ControllerAdminUserCaso.controllerAdminUserCasoList)
usca.route('/updat/<id>', methods=['GET', 'POST'])(ControllerAdminUserCaso.onGetControllerAdminUserCasoUpdate)

