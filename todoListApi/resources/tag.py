from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from todoListApi.services.base_services import TagService, TagModel

class Tag(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True
                        )
    def get(self, name):
        tag = TagService.find_by_name(name)
        tag = tag.repr_json()
        return {'tag':tag}, 200
    
    def put(self, name):
        data = Tag.parser.parse_args()
        updated_tag = TagService.update(name, data['name'])
        updated_tag = updated_tag.repr_json()
        return {'updated_tag':updated_tag}, 200
    
    def delete(self, name):
        tag = TagService.remove(name)
        tag = tag.repr_json()
        return {'deleted_tag':tag}, 200

class Tags(Resource):
    def get(self):
        tags = TagService.get_all()
        tags = [tag.repr_json() for tag in tags]
        return {'tags':tags}, 200

    def post(self):
        data = Tag.parser.parse_args()
        new_tag = TagModel(data['name'])
        saved_tag = TagService.save(new_tag)
        saved_tag = saved_tag.repr_json()
        return {'saved_tag':saved_tag}, 201

class TagTask(Resource):
    def get(self, name):
        tasks = TagService.get_tasks_by_tag_name(name)
        tasks = [task.repr_json() for task in tasks]
        return {'tasks':tasks}, 200