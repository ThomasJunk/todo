"""Baseclass for services
"""

# pylint: disable = invalid-name, too-few-public-methods


class Base:
    """Baseclass for repositories
    """

    def __init__(self, repository, log):
        self.repository = repository
        self.log = log

    def list(self):
        """Lists all items

        Returns:
            generator: set of the items in the database
        """
        return self.repository.list()

    def get_by_id(self, id):
        """Retieves a specific item by id

        Args:
            id (string): identifier of the todo

        Returns:
            object: item
        """
        return self.repository.get_by_id(id)

    def save(self, item):
        """Saves an item

        Args:
            item (object): an item

        Returns:
            object: saved item
        """
        return self.repository.save(item)

    def delete(self, item):
        """Deletes specific item

        Args:
            item (object): The item to delete
        """
