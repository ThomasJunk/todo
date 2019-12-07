# SPDX-License-Identifier: MIT
"""User handler
"""


import falcon

from middleware import login_required
from user import UserExists

from .base import RouteBase


class User(RouteBase):
    """Handles routes for User

    Args:
        RouteBase (object): Base class
    """

    @falcon.before(login_required)
    def on_get(self, req, resp):
        """GET request

        Args:
            req (object): request
            resp (resp): response
        """
        users = self.service.list()
        resp.media = [u.to_dict() for u in users]

    @falcon.before(login_required)
    def on_post(self, req, resp):
        """POST request

        Args:
            req (object): request
            resp (resp): response
        """
        user = req.media.get("user")
        if user is None:
            resp.status = falcon.HTTP_400
            resp.body = '{message: "User object not in request"}'
            return
        try:
            item = self.service.create_new_user(
                user["login"], user["password"])
            resp.media = item.to_dict()
        except UserExists:
            resp.body = '{message: "User exisits"}'
            resp.status = falcon.HTTP_409
