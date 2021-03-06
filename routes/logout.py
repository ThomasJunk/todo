# SPDX-License-Identifier: MIT
"""Logout handler
"""

import falcon
from middleware import login_required


class Logout:
    """Logout
    """
    @falcon.before(login_required)
    def on_get(self, req, resp):
        """Handles GET requests"""
        session = req.context.session
        session.delete()
        resp.status = falcon.HTTP_200  # This is the default status
        resp.media = {"message": "logged out"}
