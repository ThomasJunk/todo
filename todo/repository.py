"""ToDo Repository
"""

from tinydb import Query

import repository


class Repository(repository.Base):
    """ToDo repository

    Args:
        repository (object): Baseclass

    Returns:
        object: instance of the repository
    """

    def list(self):
        """Lists all todos

        Returns:
            generator: set of the items in the database
        """
        return (item for item in self.db)

    def get_by_id(self, id):
        """Retieves a specific ToDo

        Args:
            id (string): identifier of the todo

        Returns:
            object: ToDo
        """
        Todo = Query()
        item = self.db.search(Todo.id == id)
        return item

    def save(self, todo):
        """Saves a todo

        Args:
            todo (object): a todo

        Returns:
            object: saved todo
        """
        item = {"id": todo.id,
                "content": todo.content,
                "completed": todo.completed}
        self.db.insert(item)
        return item

    def delete(self, todo):
        """Deletes specific ToDo

        Args:
            todo (object): The ToDo to delete
        """

    def get_completed(self):
        """Retrieves completed ToDos
        """

    def get_incompleted(self):
        """Retrieves incompleted ToDos
        """
