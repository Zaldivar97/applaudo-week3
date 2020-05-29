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
        todo_list = TodoListModel.query.filter_by(name=todo_list_name).first()
        if not todo_list:
            raise ResourceDoesNotExist(
                'To-do list with the given name does not exist'
            )
        return todo_list

    @staticmethod
    def update(data, todo_list_name):
        todo_list = TodoListModel.query.filter_by(name=todo_list_name).first()
        if not todo_list:
            raise ResourceDoesNotExist(
                'To-do list with the given name does not exist'
            )
        todo_list.name = data['name']
        save_entity(todo_list)
        return todo_list

    @staticmethod
    def save(todolist: TodoListModel):
        #update and insert
        save_entity(todolist)
        return todolist

    @staticmethod
    def remove(todo_list_name):
        todo_list_to_delete = TodoListService.find_by_name(todo_list_name)
        if not todo_list_to_delete:
            raise ResourceDoesNotExist(
                'To-do list with the given name does not exist'
            )
        delete(todo_list_to_delete)
        return todo_list_to_delete


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
        if data['tags']:
            tags = TaskService.get_tags_by_name(data['tags']).all()
            task.tags = tags
        save_entity(task)
        return task

    @classmethod
    def save(cls, todo_list_name, task: TaskModel, tags):
        #update and insert
        todo_list = TodoListService.find_by_name(todo_list_name)
        if not todo_list:
            raise ResourceDoesNotExist('Parent to-do list does not exists')
        task.todo_list = todo_list
        if tags:
            tag_list = TaskService.get_tags_by_name(tags)
            task.tags = tag_list.all()
        save_entity(task)
        return task

    @staticmethod
    def get_all(todo_list_name):
        todo_list = TodoListService.find_by_name(todo_list_name)
        if not todo_list:
            raise ResourceDoesNotExist('Parent to-do list does not exists')
        tasks = todo_list.tasks
        return tasks

    @staticmethod
    def remove(todo_list_name, task_title):
        task = TaskService.find_task_by_title(todo_list_name, task_title)
        if not task:
            raise ResourceDoesNotExist('Parent to-do list does not exists')
        deleted_task = delete(task)
        return task


class TagService():

    @staticmethod
    def find_by_name(tag_name):
        tag = TagModel.query.filter_by(name=tag_name).first()
        if not tag:
            raise ResourceDoesNotExist(
                'Tag with the given name does not exist'
            )
        return tag

    @staticmethod
    def update(tag_name, new_tag_name):
        tag = TagService.find_by_name(tag_name)
        if not tag:
            raise ResourceDoesNotExist(
                'Tag with the given name does not exist'
            )
        tag.name = new_tag_name
        save_entity(tag)
        return tag

    @staticmethod
    def remove(tag_name):
        tag = TagService.find_by_name(tag_name)
        if not tag:
            raise ResourceDoesNotExist(
                'Tag with the given name does not exist'
            )
        delete(tag)
        return tag

    @staticmethod
    def save(tag):
        save_entity(tag)
        return tag

    @staticmethod
    def get_all():
        return TagModel.query.all()

    @staticmethod
    def get_tasks_by_tag_name(name):
        tag = TagService.find_by_name(name)
        if not tag:
            raise ResourceDoesNotExist(
                'Tag with the given name does not exist'
            )
        return tag.tasks
