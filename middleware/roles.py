# SPDX-License-Identifier: MIT
"""Middleware concerned with user roles
"""

import falcon


def required_role(req, resp, resource, params, role):
    """Checks whether user is admin

    Args:
        req (object): Request
        resp (object): Response
        resource (object): Ressource accessed
        params (object): Params
    """
    session = req.context.session
    if not role in session:
        raise falcon.HTTPUnauthorized("User is not logged in")
    user = session["user"]
    if not role in user["groups"]:
        raise falcon.HTTPUnauthorized("User is not allowed")
    req.context.session = session
