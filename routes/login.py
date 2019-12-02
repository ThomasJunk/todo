# SPDX-License-Identifier: MIT
"""Login handler
"""

import falcon


class Login:
    """Login
    """

    def on_get(self, req, resp):
        """Handles GET requests"""
        session = req.context.session
        session["user"] = {"id": "123", "groups": ["user"]}
        resp.status = falcon.HTTP_200
        resp.media = {"message": "logged in"}
