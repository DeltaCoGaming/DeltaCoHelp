from flask import Flask
from app.mainblue.views import mainblue
from app.extrablue.views import extrablue
from app.errorsblue.views import errorsblue
from datetime import timedelta
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(weeks=2)

    app.register_blueprint(mainblue)  # No URL prefix here
    app.register_blueprint(extrablue, url_prefix='/extrablue')
    app.register_blueprint(errorsblue, url_prefix='/errorsblue')
    
    return app
