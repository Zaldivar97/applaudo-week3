from todoListApi import db
from todoListApi.models import Serializable


tags_association = db.Table('task_tag',
                            db.Column('task_id', db.Integer,
                                      db.ForeignKey('task.task_id'),
                                      primary_key=True),
                            db.Column('tag_id', db.Integer,
                                      db.ForeignKey('tag.tag_id'),
                                      primary_key=True)
                            )


class TodoListModel(db.Model, Serializable):
    __tablename__ = 'todo_list'

    todo_list_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
    #tasks = db.relationship('TaskModel', backref='todo_list')

    def __init__(self, name: str, todo_list_id=None):
        self.todo_list_id = todo_list_id
        self.name = name
    
    def __repr__(self):
        print('[CALLED]--------------')
        return str(self.serialize())

class TagModel(db.Model, Serializable):
    __tablename__ = 'tag'
    tag_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name: str):
        self.name = name


class TaskModel(db.Model, Serializable):
    __tablename__ = 'task'
    Serializable.__ignore__.append('tags')

    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(40), unique=True)
    description = db.Column(db.Text)
    active = db.Column(db.Boolean, default=True)
    todo_list_id = db.Column(db.Integer,
                             db.ForeignKey('todo_list.todo_list_id')
                             )
    tags = db.relationship('TagModel', secondary=tags_association,
                           backref=db.backref(
                               'task', lazy=True)
                           )
    todo_list = db.relationship(
        'TodoListModel', backref=db.backref(
            'tasks',
            lazy='dynamic',
            cascade='all, delete')
    )

    def __init__(self, title: str, description: str, todo_list_id: TodoListModel = None):
        self.title = title
        self.description = description
        #self.todo_list_id = todo_list_id