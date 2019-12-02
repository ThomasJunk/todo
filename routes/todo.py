# SPDX-License-Identifier: MIT
"""Todo handler
"""

import falcon

import todo
from middleware import login_required

from .base import RouteBase


class Todo(RouteBase):
    """Handles Todos

    Args:
        RouteBase (object): Baseclass
    """

    @falcon.before(login_required)
    def on_get(self, req, resp):
        """GET request

        Args:
            req (object): request
            resp (resp): response
        """
        todos = self.service.list()
        result = map(lambda x: x.to_dict(), todos)
        resp.media = list(result)

    @falcon.before(login_required)
    def on_post(self, req, resp):
        """POST request

        Args:
            req (object): request
            resp (resp): response
        """
        t = req.media.get("todo")
        if t is None:
            resp.status = falcon.HTTP_400
            resp.body = '{message: "Todo object not in request"}'
            return
        item = self.service.create(t["content"])
        resp.media = item.to_dict()
