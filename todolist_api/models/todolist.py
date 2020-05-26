from app import db


class TodoListModel(db.Model):
    __tablename__ = 'todo_list'

    todo_list_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return str(self.__dict__)    

    @classmethod
    def test(cls):
        return cls.query.all()