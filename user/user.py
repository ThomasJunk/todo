# SPDX-License-Identifier: MIT
"""User represents the user
"""


class User:
    """User object

    Returns:
        object: user
    """

    def __init__(self, login, password, groups):
        self.login = login
        self.password = password
        self.usergroups = groups

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
