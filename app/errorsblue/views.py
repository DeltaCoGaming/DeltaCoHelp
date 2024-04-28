from flask import Blueprint, render_template

errorsblue = Blueprint('errorsblue', __name__)

@errorsblue.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


