from decouple import config
from flask import Flask
from flask_login import LoginManager # Add this line
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from src.accounts.views import accounts_bp
from src.core.views import core_bp

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)