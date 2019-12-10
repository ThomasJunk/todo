# SPDX-License-Identifier: MIT
"""ACL represents the ACL
"""
from pony.orm import *

from database import db

from .actions import Action
from .groups import Group
from .resources import Resource


class ACL(db.Entity):
    """ACL object

    Returns:
        object: ACL
    """

    resource = Required(Resource)
    group = Required(Group)
    action = Required(Action)

    def to_dict(self):
        """Dictionary representation
        """
        return {
            "resource": self.resource,
            "group": self.group,
            "action": self.action
        }
