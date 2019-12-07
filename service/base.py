# SPDX-License-Identifier: MIT
"""Baseclass for services
"""


class Base:
    """Baseclass for repositories
    """

    def __init__(self, repository, log, model):
        self.repository = repository
        self.log = log
        self.model = model

    def list(self):
        """Lists all items

        Returns:
            generator: set of the items in the database
        """
        result = self.repository.list()
        return map(lambda entity: self.model(**entity.to_dict()), result)

    def get_by_id(self, id):
        """Retieves a specific item by id

        Args:
            id (string): identifier of the todo

        Returns:
            object: item
        """
        result = self.repository.get_by_id(id)
        return self.model(**result.to_dict())

    def save(self, item):
        """Saves an item

        Args:
            item (object): an item

        Returns:
            object: saved item
        """
        result = self.repository.save(item)
        return self.model(**result.to_dict())

    def delete(self, item):
        """Deletes specific item

        Args:
            item (object): The item to delete
        """
