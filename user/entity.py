# SPDX-License-Identifier: MIT
"""User represents the user
"""

from pony.orm import *
from database import db


class User(db.Entity):
    """User object

    Returns:
        object: user
    """

    login = Required(str)
    password = Required(str)
    groups = Required(StrArray)

    def to_dict(self):
        """Dictionary representation
        """
        return {
            "login": self.login,
            "groups": list(self.groups),
            "password": self.password
        }
