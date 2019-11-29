"""User handler
"""

import json

import falcon

import todo

from .base import RouteBase


class User(RouteBase):
    """Handles routes for User

    Args:
        RouteBase (object): Base class
    """

    def on_get(self, req, resp):
        """GET request

        Args:
            req (object): request
            resp (resp): response
        """
        users = self.service.list()
        resp.media = list(users)

    def on_post(self, req, resp):
        """POST request

        Args:
            req (object): request
            resp (resp): response
        """
        user = req.media.get("user")
        try:
            item = self.service.create_new_user(
                user["login"], user["password"])
            resp.media = item.to_dict()
        except:
            resp.status = falcon.HTTP_409
