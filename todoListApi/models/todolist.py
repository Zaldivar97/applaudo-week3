from todoListApi import db
from todoListApi.models import Serializable


tags = db.Table('todo_list_tag',
                db.Column('todo_list_id', db.Integer,
                          db.ForeignKey('todo_list.todo_list_id'),
                          primary_key=True),
                db.Column('tag_id', db.Integer,
                          db.ForeignKey('tag.tag_id'),
                          primary_key=True)
                )


class TodoListModel(db.Model, Serializable):
    __tablename__ = 'todo_list'

    todo_list_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    todo_list_tags = db.relationship('TagModel', secondary=tags,
                                     backref=db.backref(
                                         'todo_lists', lazy=True)
                                     )

    def __init__(self, name: str, todo_list_id=None):
        self.todo_list_id = todo_list_id
        self.name = name


class TagModel(db.Model, Serializable):
    __tablename__ = 'tag'
    tag_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name: str):
        self.name = name

