# SPDX-License-Identifier: MIT
"""User Service
"""

import secrets

from passlib.hash import argon2

import groups
import service


class UserExists(Exception):
    """Exception thrown when user exists

    Args:
        Exception (object): Baseclass
    """


class Service(service.Base):
    """User service

    Args:
        service (object): Baseclass
    """

    def clear_password(self, user):
        """clears password

        Args:
            u (object): user

        Returns:
            object: clean user
        """
        user.password = ""
        return user

    def list(self):
        """Lists all users

        Returns:
            generator: set of the items in the database
        """
        users = map(lambda entity: self.model(
            **entity.to_dict()), self.repository.list())
        cleared = map(lambda user: self.clear_password(user), users)
        return cleared

    def create_new_user(self, login, password):
        """Creates a new user

        Args:
            login(string): user login
            password(string): password

        Raises:
            UserExists: Exception

        Returns:
            object: User
        """
        pw_hash = argon2.using(rounds=5).hash(password)
        exists = self.repository.exists(login)
        if exists:
            raise UserExists()
        usr = self.model(login=login,
                         password=pw_hash,
                         groups=groups.default_groups
                         )
        result = self.repository.save(usr)
        return self.clear_password(self.model(**result.to_dict()))

    def grant_login(self, login, password):
        """Checks whether login and password match

        Args:
            login(string): user login
            password(string): password

        Returns:
            bool: Login granted
        """
        dummy = secrets.token_urlsafe(16)
        pw_hash = argon2.using(rounds=5).hash(dummy)
        user = self.repository.get_user_by_login(login)
        if not user:
            return argon2.verify(password, pw_hash)
        return argon2.verify(password, user.password)
