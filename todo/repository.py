# SPDX-License-Identifier: MIT
"""ToDo Repository
"""

from pony.orm import *
import uuid
import repository


class Repository(repository.Base):
    """ToDo repository

    Args:
        repository (object): Baseclass

    Returns:
        object: instance of the repository
    """

    @db_session
    def get_by_id(self, id):
        """Retieves a specific ToDo

        Args:
            id (string): identifier of the todo

        Returns:
            object: ToDo
        """
        return self.entity.select(lambda x: x.id == id)

    @db_session
    def create(self, content):
        uid = str(uuid.uuid4())
        t = self.entity(id=uid, body=content, completed=False)
        return t

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
