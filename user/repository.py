# SPDX-License-Identifier: MIT
"""User Repository
"""
import repository
from tinydb import Query


class Repository(repository.Base):
    """User Repository

    Args:
        repository (object): Base class

    Returns:
        object: Instance of repository
    """

    def exists(self, login):
        """Checks whether user exists

        Args:
            login (string): login
        """
        User = Query()
        return self.db.count(User.login == login) > 0

    def get_user_by_login(self, login):
        """Retrieves user by login

        Args:
            login (string): the login
        """
        User = Query()
        item = self.db.search(User.login == login)
        return item
