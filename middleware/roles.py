"""Middleware concerned with user roles
"""

from functools import wraps
import falcon


def admin_role(func):
    """Admin role decorator

    Args:
        func (function): route

    Returns:
        function: route
    """
    @wraps(func)
    def wrapped(*args, **kwargs):
        _, req, resp = args
        session = session = req.env["beaker.session"]
        if not "user" in session:
            resp.status = falcon.falcon.HTTPUnauthorized(
                "User is not logged in")
            return
        user = session["user"]
        if not "admin" in user["groups"]:
            resp.status = falcon.HTTPUnauthorized("User is not allowed")
            return
        req.context.session = session
        return func(*args, **kwargs)
    return wrapped
