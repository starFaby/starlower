from flask import Blueprint
from app.controllers.controllerAdminUsers import ControllerUser
userall= Blueprint('userall', __name__)
userall.route('/userall', methods=['GET', 'POST'], defaults={"page": 1})(ControllerUser.controllerUsersList)
userall.route('/userall/<int:page>', methods=['GET', 'POST'])(ControllerUser.controllerUsersList)