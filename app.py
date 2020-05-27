import flask_restful as rest

from todoListApi import app
from todoListApi.resources.todolist import TodoList

api = rest.Api(app)

api.add_resource(TodoList, '/todolists/<int(min=1):todo_list_id>')

if __name__ == '__main__':
    app.run()
