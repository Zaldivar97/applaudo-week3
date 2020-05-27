from todoListApi.models.todolist import TodoListModel, db


class TodoListService():
    @staticmethod
    def find_by_id(todo_list_id):
        return TodoListModel.query.get(todo_list_id)

    @staticmethod
    def save(todolist):
        #update and insert        
        db.session.add(todolist)
        db.session.commit()
       #db.session.refresh(todolist)
        return todolist

    @staticmethod
    def remove(todolist):
        db.session.delete(todolist)
        db.session.commit()
        return todolist

    @staticmethod
    def remove_by_id(todo_list_id):
        x = TodoListModel.query.filter_by(todo_list_id=todo_list_id).delete()
        db.session.commit()
        print('[WARNING]: ',x)