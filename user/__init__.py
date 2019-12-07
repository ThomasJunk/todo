# SPDX-License-Identifier: MIT
"""Provides access to the User internals
"""
from .entity import User as Entity
from .repository import Repository
from .service import Service, UserExists
from .user import User


def create_Service(log):
    """Injects db connection and sets up service

    Args:
        db (object): Database
        log (object): logger

    Returns:
        object: User Handler
    """
    repo = Repository(Entity, log)
    srv = Service(repo, log, User)
    return srv
