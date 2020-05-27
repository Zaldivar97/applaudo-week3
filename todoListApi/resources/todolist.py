from flask import jsonify
from flask_restful import Resource, reqparse
from todoListApi.services.base_services import TodoListService
from todoListApi.models.todolist import TodoListModel


class TodoList(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True)
    parser.add_argument('tag',
                        type=int,
                        required=False)

    def get(self, todo_list_id):
        todo_list = TodoListService.find_by_id(todo_list_id)
        if todo_list:
            return jsonify(todo_list.serialize())
        return {'message': 'Not found'}, 404

    def put(self, todo_list_id):
        data = TodoList.parser.parse_args()
        todo_list = TodoListService.find_by_id(todo_list_id)
        if todo_list:
            todo_list.name = data['name']
            updated_todolist = TodoListService.save(todo_list)

            return updated_todolist.serialize(), 200
        else:
            new_todolist = TodoListModel(data['name'], todo_list_id)
            new_todolist = TodoListService.save(new_todolist)
            return new_todolist.serialize(), 200

    def delete(self, todo_list_id):
        todo_list_to_delete = TodoListService.find_by_id(todo_list_id)
        if todo_list_to_delete:
            deleted_todo_list = TodoListService.remove(todo_list_to_delete)
            return deleted_todo_list.serialize(), 200
        return {'message': 'Not found'}, 404