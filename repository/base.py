"""Baseclass for repositories
"""

# pylint: disable = invalid-name, too-few-public-methods


class Base:
    """Baseclass for repositories
    """

    def __init__(self, database):
        self.db = database
