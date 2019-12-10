# SPDX-License-Identifier: MIT
"""Action represents the Action
"""

from pony.orm import *
from database import db


class Action(db.Entity):
    """Action object

    Returns:
        object: Action
    """

    name = Required(str)

    def to_dict(self):
        """Dictionary representation
        """
        return {
            "name": self.name
        }
