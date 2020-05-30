from flask_migrate import Migrate
from todoListApi import app, db
from todoListApi.models.base_models import TagModel, TodoListModel, TaskModel

migrate = Migrate(app, db)
