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
        tag = tag.serialize()
        return make_response(jsonify(tag), 200)
    
    def put(self, name):
        data = Tag.parser.parse_args()
        updated_tag = TagService.update(name, data['name'])
        updated_tag = updated_tag.serialize()
        return make_response(jsonify(updated_tag), 200)
    
    def delete(self, name):
        tag = TagService.remove(name)
        tag = tag.serialize()
        return make_response(jsonify(tag), 200)

class Tags(Resource):
    def get(self):
        tags = TagService.get_all()
        tags = [tag.serialize() for tag in tags]
        return make_response(jsonify(tags), 200)

    def post(self):
        data = Tag.parser.parse_args()
        new_tag = TagModel(data['name'])
        saved_tag = TagService.save(new_tag)
        saved_tag = saved_tag.serialize()
        return make_response(jsonify(saved_tag), 201)

class TagTask(Resource):
    def get(self, name):
        tasks = TagService.get_tasks_by_tag_name(name)
        tasks = [task.serialize() for task in tasks]
        return make_response(jsonify(tasks), 200)