import os

import flask
import flask_sqlalchemy as sql

from config import mode

db = sql.SQLAlchemy()

app = flask.Flask(__name__)

app.config.from_object(mode['dev'])
db.init_app(app)
