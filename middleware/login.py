from functools import wraps
import falcon


def login_required(func):
    """login required decorator

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
            resp.status = falcon.HTTPUnauthorized("User is not logged in")
            return
        req.context.session = session
        return func(*args, **kwargs)
    return wrapped
