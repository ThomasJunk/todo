# SPDX-License-Identifier: MIT
"""User Service
"""

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

    def __init__(self, repository, log, model, cryptoservice):
        self.repository = repository
        self.log = log
        self.model = model
        self.cryptoservice = cryptoservice

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
        pw_hash = self.cryptoservice.hash_password(password)
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
        dummy_password = self.cryptoservice.generate_dummytoken()
        dummy_hash = self.cryptoservice.hash_password(dummy_password)
        user = self.repository.get_user_by_login(login)
        if not user:
            return self.cryptoservice.verify_password(password, dummy_hash)
        return self.cryptoservice.verify_password(password, user.password)
