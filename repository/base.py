# SPDX-License-Identifier: MIT
"""Baseclass for repositories
"""

# pylint: disable = invalid-name, too-few-public-methods


class Base:
    """Baseclass for repositories
    """

    def __init__(self, database, log):
        self.db = database
        self.log = log

    def list(self):
        """Lists all items

        Returns:
            generator: set of the items in the database
        """
        return (item for item in self.db)

    def save(self, item):
        """Saves a item

        Args:
            item (object): am item

        Returns:
            object: saved item
        """
        self.db.insert(item.to_dict())
        return item
