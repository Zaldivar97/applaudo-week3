import flask_restful as rest


from todoListApi import app
from todoListApi.resources.todolist import TodoList, TodoLists
from todoListApi.resources.task import Task, Tasks
from todoListApi.resources.tag import Tag, Tags, TagTask
from todoListApi.resources.exceptions import ResourceDoesNotExist, BadRequest

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


@app.errorhandler(ResourceDoesNotExist)
def handler(exc):
    return {'message': exc.message}, 404


'''@app.errorhandler(BadRequest)
    def handler(exc):
        return {'message': exc.message}, 400'''

if __name__ == '__main__':
    app.run()
