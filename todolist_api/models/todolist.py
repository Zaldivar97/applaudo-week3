from todolist_api.models import Printable
from app import db


class TodoListModel(db.Model, Printable):
    __tablename__ = 'todo_list'

    todo_list_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    todo_list_tags = db.relationship('TagModel', secondary=tags,
                                     backref=db.backref(
                                         'todo_lists', lazy=True)
                                     )

    def __init__(self, name: str):
        self.name = name


class TagModel(db.Model, Printable):
    tag_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name: str):
        self.name = name


tags = db.Table('todo_list_tag',
                db.Column('todo_list_id', db.Integer,
                          db.ForeignKey('todo_list.id'),
                          primary_key=True),
                db.Column('tag_id', db.Integer,
                          db.ForeignKey('tag_id'),
                          primary_key=True)
                )
