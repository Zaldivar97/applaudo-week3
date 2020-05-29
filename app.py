import flask_restful as rest
from flask import make_response

from todoListApi import app
from todoListApi.resources.todolist import TodoList, TodoLists
from todoListApi.resources.task import Task, Tasks
from todoListApi.resources.tag import Tag, Tags, TagTask
from todoListApi.resources.exceptions import ResourceDoesNotExist
from todoListApi.models import OutputEncoder, json

api = rest.Api(app)

api.add_resource(TodoList,
                 '/todolists/<string(minlength=1):todo_list_name>/'
                 )
api.add_resource(TodoLists,
                 '/todolists/'
                 )
api.add_resource(
    Task,
    '/todolists/<string(minlength=1):todo_list_name>/tasks/<string(minlength=2):task_title>/'
)
api.add_resource(
    Tasks,
    '/todolists/<string(minlength=1):todo_list_name>/tasks/'
)
api.add_resource(Tag,
                 '/tags/<string(minlength=2):name>/'
                 )

api.add_resource(TagTask,
                 '/tags/<string(minlength=2):name>/tasks'
                 )

api.add_resource(Tags,
                 '/tags'
                 )


@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data, cls=OutputEncoder), code)
    resp.headers.extend(headers or {})
    return resp


@app.errorhandler(ResourceDoesNotExist)
def handler(exc):
    return {'message': exc.message}, 404


if __name__ == '__main__':
    app.run()
