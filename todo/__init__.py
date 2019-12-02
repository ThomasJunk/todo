# SPDX-License-Identifier: MIT
"""Provides access to the ToDo internals
"""


from .repository import Repository
from .service import Service
from .todo import Todo as New


def create_Service(db, log):
    """Injects db connection and sets up service

    Args:
        db (object): Database

    Returns:
        object: ToDo Handler
    """
    todo_repository = Repository(db.table("todos"), log)
    todo_service = Service(todo_repository, log)
    return todo_service
