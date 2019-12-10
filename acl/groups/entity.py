# SPDX-License-Identifier: MIT
"""Group represents the usergroup
"""

from pony.orm import *
from database import db


class Group(db.Entity):
    """Group object

    Returns:
        object: group
    """

    name = Required(str)

    def to_dict(self):
        """Dictionary representation
        """
        return {
            "name": self.name
        }
