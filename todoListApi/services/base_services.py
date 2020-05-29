from sqlalchemy import func
from todoListApi.models.base_models import TodoListModel, TaskModel, TagModel, db
from todoListApi.resources.exceptions import ResourceDoesNotExist


def delete(entity):
    db.session.delete(entity)
    db.session.commit()


def save_entity(entity):
    db.session.add(entity)
    db.session.commit()
    db.session.refresh(entity)


class TodoListService():
    @staticmethod
    def find_by_name(todo_list_name):
        return TodoListModel.query.filter_by(name=todo_list_name).first()

    @staticmethod
    def save(todolist: TodoListModel):
        #update and insert
        db.session.add(todolist)
        db.session.commit()
        db.session.refresh(todolist)
        return todolist

    @staticmethod
    def remove(todolist: TodoListModel):
        db.session.delete(todolist)
        db.session.commit()
        return todolist


class TaskService():
    @staticmethod
    def find_task_like(todo_list_name, title_pattern):
        tasks = db.session.query(TaskModel).join(TodoListModel)\
            .filter(TodoListModel.name == todo_list_name)\
            .filter(TaskModel.title.like(f'%{title_pattern}%'))\
            .all()
        if not tasks:
            raise ResourceDoesNotExist(
                'Task(s) with the given title does not exists')
        return tasks

    @staticmethod
    def find_task_by_title(todo_list_name, title):
        return db.session.query(TaskModel).join(TodoListModel)\
            .filter(TodoListModel.name == todo_list_name)\
            .filter(TaskModel.title == title)\
            .first()

    @staticmethod
    def get_tags_by_name(tag_names):
        tag_list = TagModel.query.filter(TagModel.name.in_(tag_names))
        return tag_list

    @classmethod
    def update(cls, data, todo_list_name, task_title):
        task = TaskService.find_task_by_title(todo_list_name, task_title)
        if not task:
            raise ResourceDoesNotExist('Task does not exist')
        title = data['title']
        description = data['description']
        task.title = title
        task.description = description
        tags = TaskService.get_tags_by_name(data['tags'])
        task.tags = TaskService.get_tags_by_name(data['tags']).all()
        save_entity(task)
        return task

    @classmethod
    def save(cls, todo_list_name, task: TaskModel, tags):
        #update and insert
        todo_list = TodoListService.find_by_name(todo_list_name)
        if not todo_list:
            raise ResourceDoesNotExist('Parent to-do list does not exists')
        task.todo_list = todo_list
        tag_list = TaskService.get_tags_by_name(tags)
        task.tags = tag_list.all()
        save_entity(task)
        return task

    @staticmethod
    def get_all(todo_list_name):
        todo_list = TodoListService.find_by_name(todo_list_name)
        if not todo_list:
            raise ResourceDoesNotExist('Parent to-do list does not exists')
        tasks = todo_list.tasks.all()
        for task in tasks:
            tags_transformed = []
            for tag in task.tags:
                if tag:
                    tags_transformed.append(tag.serialize())
            task.tag = tags_transformed
        tasks = [task.serialize() for task in tasks]
        return tasks

    @staticmethod
    def remove(todo_list_name, task_title):
        task = TaskService.find_task_by_title(todo_list_name, task_title)
        if not task:
            raise ResourceDoesNotExist('Parent to-do list does not exists')
        deleted_task = delete(task)
        return task
