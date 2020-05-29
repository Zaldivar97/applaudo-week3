class Serializable:
    __ignore__ = ['_sa_instance_state']

    def serialize(self):
        properties = self.__dict__
        filtered_properties = filter(
            lambda dictionary: dictionary[0] not in self.__ignore__,
            properties.items())
        return dict(filtered_properties)
