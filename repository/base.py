# SPDX-License-Identifier: MIT
"""Baseclass for repositories
"""

from pony.orm import *


class Base:
    """Baseclass for repositories
    """

    def __init__(self, entity, log):
        self.entity = entity
        self.log = log

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
    def list(self):
        """Lists all items

        Returns:
            generator: set of the items in the database
        """
        return select(e for e in self.entity)[:]

    @db_session
    def save(self, item):
        result = self.entity(**item.to_dict())
        return result
