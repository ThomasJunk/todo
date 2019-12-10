# SPDX-License-Identifier: MIT
"""Resource represents the Resource
"""

from pony.orm import *
from database import db


class Resource(db.Entity):
    """Resource object

    Returns:
        object: resource
    """

    name = Required(str)

    def to_dict(self):
        """Dictionary representation
        """
        return {
            "name": self.name
        }
