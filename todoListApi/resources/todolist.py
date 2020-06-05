from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from todoListApi.services.base_services import TodoListService
from todoListApi.models.base_models import TodoListModel
import json


class TodoList(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True)

    # frontend dev should replace 'space' with %20
    def get(self, todo_list_name):
        todo_list = TodoListService.find_by_name(todo_list_name)
        return {'todolist':todo_list.repr_json()}, 200

    def put(self, todo_list_name):
        data = TodoList.parser.parse_args()
        todo_list = TodoListService.update(data, todo_list_name)
        return {'todolist':todo_list.repr_json()}, 200

    def delete(self, todo_list_name):
        deleted_todo_list = TodoListService.remove(todo_list_name)
        return {'todo_list':deleted_todo_list.repr_json()}, 200


class TodoLists(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True)

    def get(self):
        todolists = TodoListModel.query.all() 
        todolist = [todo_list.repr_json() for todo_list in todolists]   
        return {'todolists':todolists}, 200

    def post(self):
        data = TodoList.parser.parse_args()
        name = data['name']
        todo_list_to_save = TodoListModel(name)
        saved_todo_list = TodoListService.save(todo_list_to_save)
        return {'todo_list':saved_todo_list.repr_json()}, 201
