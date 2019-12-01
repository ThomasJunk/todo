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
    if "user" in req.context.session:
        return
    else:
        raise falcon.HTTPUnauthorized("User is not logged in")
