# SPDX-License-Identifier: MIT
"""Provides access to the User internals
"""
from .repository import Repository
from .service import Service, UserExists
from .user import User


def create_Service(db, log):
    """Injects db connection and sets up service

    Args:
        db (object): Database
        log (object): logger

    Returns:
        object: User Handler
    """
    repo = Repository(db.table("users"), log)
    srv = Service(repo, log)
    return srv
