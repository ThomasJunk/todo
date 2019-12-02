# SPDX-License-Identifier: MIT
"""Todo represents a Todo
"""
import uuid
from database import db
from pony.orm import *


class Todo(db.Entity):
    """The actual Todo
    """
    id = PrimaryKey(str)
    body = Required(str)
    completed = Optional(bool)

    @property
    def is_completed(self):
        """Gives status of completion

        Returns:
            bool: status
        """
        return self.completed

    @property
    def content(self):
        """content shows content of the ToDo

        Returns:
            string: its content
        """
        return self.body

    def toggle_status(self):
        """Toggles completed status
        """
        self.completed = not self.completed

    @content.setter
    def content(self, body):
        self.body = body

    def to_dict(self):
        """Dictionary representation
        """
        return {
            "id": self.id,
            "content": self.body,
            "completed": self.completed
        }

    def __repr__(self):
        return f"todo: {self.body[0:10]} complete: {self.completed}"
