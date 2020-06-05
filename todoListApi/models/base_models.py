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
    

    def __init__(self, name: str, todo_list_id=None):
        self.name = name

    def repr_json(self):
        return dict(
            id=self.todo_list_id,
            name=self.name,
            tasks=getattr(self, 'tasks')
        )


class TagModel(db.Model, Serializable):
    __tablename__ = 'tag'
    tag_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name: str):
        self.name = name
    
    def repr_json(self):
        return dict(
            id=self.tag_id,
            name=self.name
        )


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
                               'tasks', lazy=True)
                           )
    todo_list = db.relationship(
        'TodoListModel', backref=db.backref(
            'tasks',
            lazy=True,
            cascade='all, delete')
    )

    def __init__(self, title: str, description: str, todo_list_id: TodoListModel = None):
        self.title = title
        self.description = description
        #self.todo_list_id = todo_list_id

    def repr_json(self):
        return dict(
            id=self.task_id,
            title=self.title,
            description=self.description,
            tags=self.tags
        )
