class Serializable:
    def serialize(self):
        serializable_dict = self.__dict__
        if '_sa_instance_state' in serializable_dict:
            del serializable_dict['_sa_instance_state']
        return serializable_dict