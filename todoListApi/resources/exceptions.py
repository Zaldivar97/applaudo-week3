class ResourceDoesNotExist(Exception):
    def __init__(self, message="Resource does not exists"):
        self.message = message
        super().__init__(self.message)

class BadRequest(Exception):
    def __init__(self, message="The request has an error"):
        self.message = message
        super().__init__(self.message)
