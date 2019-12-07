# SPDX-License-Identifier: MIT
"""Provides access to the ToDo internals
"""


from .entity import Todo as Entity
from .repository import Repository
from .service import Service
from .todo import Todo


def create_Service(log):
    """Injects db connection and sets up service

    Args:
        db (object): Database

    Returns:
        object: ToDo Handler
    """
    todo_repository = Repository(Entity, log)
    todo_service = Service(todo_repository, log, Todo)
    return todo_service
