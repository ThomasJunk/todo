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
    usergroups = Required(StrArray)

    @property
    def groups(self):
        """Returns usergroups

        Returns:
            frozenset: usergroups
        """
        return frozenset(self.usergroups)

    def add_group(self, group):
        """Adds user to group

        Args:
            group (string): group name
        """
        if group in self.usergroups:
            return
        self.usergroups.add(group)

    def del_group(self, group):
        """removes user from group

        Args:
            group (string): group name
        """
        self.usergroups.remove(group)

    def to_dict(self):
        """Dictionary representation
        """
        return {
            "login": self.login,
            "groups": list(self.usergroups),
            "password": self.password
        }
