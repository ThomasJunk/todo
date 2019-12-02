# SPDX-License-Identifier: MIT
"""User Repository
"""
import repository
from .user import User
from pony.orm import db_session, commit


class Repository(repository.Base):
    """User Repository

    Args:
        repository (object): Base class

    Returns:
        object: Instance of repository
    """
    @db_session
    def exists(self, login):
        """Checks whether user exists

        Args:
            login (string): login
        """
        users = self.get_user_by_login(login)
        return len(users) > 0

    @db_session
    def save(self, password, login, groups):
        user = User(login=login, password=password, usergroups=groups)
        return user

    @db_session
    def get_user_by_login(self, login):
        """Retrieves user by login

        Args:
            login (string): the login
        """
        return self.entity.select(lambda x: x.login == login)
