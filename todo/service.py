# SPDX-License-Identifier: MIT
"""Todo Service
"""
import service


class Service(service.Base):
    """Service for ToDos

    Args:
        service (object): Baseclass
    """

    def create(self, content):
        """creates new todo

        Args:
            content (string): The actual todo

        Returns:
            ToDo: a todo object
        """
        return self.repository.create(content)

    def get_completed(self):
        """gets completed ToDos
        """

    def get_incompleted(self):
        """gets incompleted ToDos
        """
