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
    def list(self):
        """Lists all items

        Returns:
            generator: set of the items in the database
        """
        return select(e for e in self.entity)[:]

    @db_session
    def save(self, item):
        commit()
        return item
