from flask import jsonify
from flask_restful import Resource, reqparse
from todolist_api.services.base_services import TodoListService


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
            return jsonify(todo_list)
        return {'message':'Not found'}, 404    