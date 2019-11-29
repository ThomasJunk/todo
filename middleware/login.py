from functools import wraps
import falcon


def login_required(req, resp, resource, params):
    """Checks whether user is logged in

    Args:
        req (object): Request
        resp (object): Response
        resource (object): Ressource accessed
        params (object): Params
    """
    session = session = req.env["beaker.session"]
    if not "user" in session:
        raise falcon.HTTPUnauthorized("User is not logged in")
    req.context.session = session
