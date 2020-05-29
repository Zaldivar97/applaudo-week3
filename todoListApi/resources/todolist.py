from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from todoListApi.services.base_services import TodoListService
from todoListApi.models.base_models import TodoListModel


class TodoList(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True)
    parser.add_argument('tag',
                        type=int,
                        required=False)

    #frontend dev should replace 'space' with %20
    def get(self, todo_list_name):
        todo_list = TodoListService.find_by_name(todo_list_name)
        if todo_list:
            response = todo_list.serialize()
            tasks = [task.serialize() for task in todo_list.tasks.all()]
            response['tasks'] = tasks
            return make_response(jsonify(response), 200)
        return {'message': 'Not found'}, 404

    def put(self, todo_list_name):
        data = parser.parse_args()
        todo_list = TodoListService.find_by_id(todo_list_name)
        if todo_list:
            todo_list.name = data['name']
            updated_todolist = TodoListService.save(todo_list)
            return updated_todolist.serialize(), 200
        return {'message': 'Not found'}, 404

    def delete(self, todo_list_name):
        todo_list_to_delete = TodoListService.find_by_name(todo_list_name)
        if todo_list_to_delete:
            deleted_todo_list = TodoListService.remove(todo_list_to_delete)
            return deleted_todo_list.serialize(), 200
        return {'message': 'Not found'}, 404


class TodoLists(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True)
    parser.add_argument('tag',
                        type=int,
                        required=False)

    def get(self):
        todolists = TodoListModel.query.all()
        todolists_transformed = list(
            map(lambda current_list: current_list.serialize(),
                todolists))

        return make_response(jsonify(todolists=todolists_transformed), 200)

    def post(self):
        data = TodoList.parser.parse_args()
        name = data['name']
        tag = data['tag']
        todo_list_to_save = TodoListModel(name)
        saved_todolist = TodoListService.save(todo_list_to_save)
        return make_response(jsonify(saved_todolist.serialize()),
                             200
                             )
