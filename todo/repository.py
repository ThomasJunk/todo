# SPDX-License-Identifier: MIT
"""ToDo Repository
"""

import uuid

from pony.orm import *

import repository


class Repository(repository.Base):
    """ToDo repository

    Args:
        repository (object): Baseclass

    Returns:
        object: instance of the repository
    """

    @db_session
    def create(self, todo):
        t = self.entity(id=todo.id,
                        body=todo.content,
                        completed=todo.completed
                        )
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
