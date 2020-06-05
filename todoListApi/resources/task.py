from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from todoListApi.models.base_models import TodoListModel, TaskModel
from todoListApi.services.base_services import TaskService, TodoListService


class Task(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('title',
                        type=str,
                        required=True
                        )

    parser.add_argument('description',
                        type=str,
                        required=True
                        )

    parser.add_argument('tags',
                        type=str,
                        action='append',
                        required=False
                        )

    def get(self, todo_list_name, task_title):
        tasks = TaskService.find_task_like(todo_list_name, task_title)
        tasks = [task.repr_json() for task in tasks]
        return {'tasks': tasks}, 200

    def put(self, todo_list_name, task_title):

        data = Tasks.parser.parse_args()

        updated_task = TaskService.update(
            data, todo_list_name, task_title
        )

        return {'task': updated_task.repr_json()}, 200

    def delete(self, todo_list_name, task_title):
        deleted_task = TaskService.remove(todo_list_name, task_title)
        return {'task': deleted_task.repr_json()}, 200


class Tasks(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('title',
                        type=str,
                        required=True
                        )

    parser.add_argument('description',
                        type=str,
                        required=True
                        )

    parser.add_argument('tags',
                        type=str,
                        action='append',
                        required=False
                        )

    def get(self, todo_list_name):
        tasks = TaskService.get_all(todo_list_name)
        tasks = [task.repr_json() for task in tasks]
        return {'tasks': tasks}, 200

    def post(self, todo_list_name):
        data = Tasks.parser.parse_args()
        new_task = TaskModel(data['title'], data['description'])
        saved_task = TaskService.save(todo_list_name, new_task, data['tags'])
        return {'saved_task': saved_task.repr_json()}, 201
