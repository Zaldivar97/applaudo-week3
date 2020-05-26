import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from todolist_api.resources.todolist import TodoList
from config import mode

db = SQLAlchemy()

app = Flask(__name__)

api = Api(app)

api.add_resource(TodoList, '/todolist/<int(min=1):todo_list_id>')

if __name__ == '__main__':
    #env_mode = os.getenv('ENVIRONMENT','test')
    app.config.from_object(mode['dev'])
    db.init_app(app)
    app.run()
    