from todolist_api.models.todolist import TodoListModel, db


class TodoListService(cls, todo_list_id):
    @staticmethod
    def find_by_id(todo_list_id):
        return TodoListModel.query.filter_by(todo_list_id=todo_list_id)

    @staticmethod
    def save(todolist):
        #update and insert
        db.session.add(todolist)
        db.session.commit()
        return todolist

    @staticmethod
    def remove(todolist):
        db.session.delete(todolist)
        db.session.commit()
        return todolist
