import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import mode

db = SQLAlchemy()

app = Flask(__name__)

@app.route('/')
def test():
    from todolist_api.models.todolist import TodoListModel
    print(TodoListModel.test())

if __name__ == '__main__':
    #env_mode = os.getenv('ENVIRONMENT','test')
    app.config.from_object(mode['dev'])
    db.init_app(app)
    app.run()
    