import json


class Serializable:
    __ignore__ = ['_sa_instance_state']

    def serialize(self):
        properties = self.__dict__
        filtered_properties = filter(
            lambda dictionary: dictionary[0] not in self.__ignore__,
            properties.items())
        return dict(filtered_properties)


class OutputEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'repr_json'):
            return obj.repr_json()
        else:
            return json.JSONEncoder.default(self, obj)
