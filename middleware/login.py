# SPDX-License-Identifier: MIT
"""Guarding for login

Raises:
    falcon.HTTPUnauthorized: In case the user is not logged in
"""
import falcon


def login_required(req, resp, resource, params):
    """Checks whether user is logged in

    Args:
        req (object): Request
        resp (object): Response
        resource (object): Ressource accessed
        params (object): Params
    """
    session = req.context.session
    if "user" in session:
        return
    else:
        raise falcon.HTTPUnauthorized("User is not logged in")
