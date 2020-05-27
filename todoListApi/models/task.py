from todoListApi.models import Printable
from todoListApi import db


class TaskModel(db.Model, Printable):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    description = db.Column(db.Text)
    active = db.Column(db.Boolean)
    todo_list_id = db.Column(db.Integer,
                             db.ForeignKey('todo_list.todo_list_id',
                                           on_delete=db.CASCADE)
                             )
    todo_list = db.relationship(
        'Todo_list', backref=db.backref('tasks', lazy='dynamic')
    )

    def __init__(self, title: str, description: str, todo_list_id: int):
        self.title = title
        self.description = description
        self.todo_list_id = todo_list_id
