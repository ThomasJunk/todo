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
